import os
import re
import argparse
import json
import requests
import time
from typing import List, Tuple
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def call_ollama_api(text: str, model: str = "aispin/qwen2.5-7b-instruct-abliterated-v2.q4_k_s.gguf", api_base: str = "http://localhost:11434") -> str:
    """使用Ollama的HTTP API获取AI判断结果"""
    prompt = f"""
I need you to help me determine whether the following text needs to be translated.
Please analyze this text and determine if it falls into the following categories that do not require translation:
1. File name
2. human name or pure number or pure symbol
3. such as ["xxx.anm", "x", "1","井上 茉莉","-", "P.y", "女仆耐力：2998.736", "女仆耐力：3"] these should be removed
Please just reply "TRANSLATE" or "NO_TRANSLATE" without adding any extra content.
The text to determine: "{text}"
    """
    api_url = f"{api_base}/api/generate"
    # api_url = f"http://127.0.0.1:5000/v1/chat/completions"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    # payload = {
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": prompt
    #         }
    #     ],
    #     "mode": "instruct",
    #     "stream": False
    # }
    headers = {
        "Content-Type": "application/json"
    }

    response = requests.post(api_url, json=payload, headers=headers)
    if response.status_code != 200:
        if response.status_code == 400 or response.status_code == 500 or response.status_code == 422:
            print(f"API调用错误: {response.status_code}")
            print(response.text)
            exit(1)
        print(f"API调用错误: {response.status_code}")
        print(response.text)
        return "TRANSLATE"
    response.raise_for_status()
    result = response.json()
    print(result)
    response_text = result.get("response", "").strip()

    # 简单解析结果
    if "NO_TRANSLATE" in response_text:
        return "NO_TRANSLATE"
    else:
        return "TRANSLATE"

# def split_text(text: str, max_length: int = 200) -> List[str]:
#     """将文本分割成适当的块进行处理"""
#     # 使用自然段落或行进行分割
#     chunks = []
#     lines = text.split('\n')
#
#     current_chunk = ""
#     for line in lines:
#         if not line.strip():  # 跳过空行
#             continue
#
#         if len(current_chunk) + len(line) <= max_length:
#             current_chunk += line + '\n'
#         else:
#             if current_chunk:
#                 chunks.append(current_chunk.strip())
#             current_chunk = line + '\n'
#
#     if current_chunk:
#         chunks.append(current_chunk.strip())
#
#     return chunks

def split_text(text: str, max_length: int = 200) -> List[str]:
    """将文本按行分割成块"""
    chunks = []
    lines = text.split('\n')

    for line in lines:
        stripped_line = line.strip()
        if stripped_line:  # 跳过空行
            chunks.append(stripped_line)

    return chunks

def process_chunk(chunk: str, model: str, api_base: str, pattern: str) -> Tuple[str, bool, str]:
    """处理单个文本块，返回文本、是否保留的标志和移除原因"""
    # 使用正则表达式预过滤
    if re.match(pattern, chunk.strip()):
        return (chunk, False, "预过滤移除")

    # 使用AI判断
    result = call_ollama_api(chunk, model, api_base)
    if result == "TRANSLATE":
        return (chunk, True, "AI判断保留")
    else:
        return (chunk, False, "AI判断移除")

def filter_text_file(input_file: str, output_file: str, model: str, api_base: str, workers: int) -> dict:
    """处理单个输入文件，过滤掉不需要翻译的内容"""
    # 确保输出目录存在
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # 读取输入文件
    try:
        with open(input_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        # 尝试使用其他编码
        try:
            with open(input_file, 'r', encoding='shift-jis') as f:
                content = f.read()
        except UnicodeDecodeError:
            print(f"无法读取文件 {input_file}，跳过处理")
            return {
                "total": 0,
                "kept": 0,
                "pre_filter": 0,
                "ai_filter": 0,
                "error": "编码错误"
            }

    # 分割文本
    chunks = split_text(content)
    if not chunks:
        print(f"文件 {input_file} 为空或只包含空行，跳过处理")
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("")
        return {
            "total": 0,
            "kept": 0,
            "pre_filter": 0,
            "ai_filter": 0,
            "error": "空文件"
        }

    # 预先过滤明显不需要翻译的内容
    pattern = r'^([a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9]{2,4}|x=[\-\d\.]+\s+y=[\-\d\.]+\s+z=[\-\d\.]+)$'

    # 使用线程池并行处理
    filtered_chunks = []
    pre_filter_count = 0
    ai_filter_count = 0
    kept_count = 0

    print(f"开始处理文件: {input_file} ({len(chunks)} 个文本块)")

    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = [executor.submit(process_chunk, chunk, model, api_base, pattern) for chunk in chunks]

        for i, future in enumerate(futures):
            chunk, keep, reason = future.result()

            if reason == "预过滤移除":
                pre_filter_count += 1
                print(f"[{input_file}][{i+1}/{len(chunks)}] 预过滤移除: {chunk}")
            elif reason == "AI判断移除":
                ai_filter_count += 1
                print(f"[{input_file}][{i+1}/{len(chunks)}] AI判断移除: {chunk}")
            else:
                kept_count += 1
                filtered_chunks.append(chunk)
                print(f"[{input_file}][{i+1}/{len(chunks)}] AI判断保留: {chunk}")

    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(filtered_chunks))

    results = {
        "total": len(chunks),
        "kept": kept_count,
        "pre_filter": pre_filter_count,
        "ai_filter": ai_filter_count,
        "error": None
    }

    print(f"\n文件 {input_file} 处理完成:")
    print(f"  - 保留: {kept_count}/{len(chunks)} 个文本块")
    print(f"  - 预过滤移除: {pre_filter_count} 个")
    print(f"  - AI判断移除: {ai_filter_count} 个")
    print(f"过滤后内容已保存至: {output_file}")

    return results

def process_directory(input_dir: str, output_dir: str, model: str, api_base: str, workers: int, extensions: List[str]) -> None:
    """批量处理目录下的所有文本文件"""
    # 确保输出目录存在
    os.makedirs(output_dir, exist_ok=True)

    # 获取所有文件
    input_path = Path(input_dir)
    all_files = list(input_path.rglob('*'))

    # 过滤出指定扩展名的文件
    text_files = [f for f in all_files if f.is_file() and (not extensions or f.suffix.lower() in extensions)]

    if not text_files:
        print(f"在 {input_dir} 中没有找到符合条件的文件")
        return

    print(f"在 {input_dir} 中找到 {len(text_files)} 个文件等待处理")

    # 处理统计
    total_stats = {
        "files_processed": 0,
        "files_error": 0,
        "total_chunks": 0,
        "kept_chunks": 0,
        "pre_filtered_chunks": 0,
        "ai_filtered_chunks": 0,
        "start_time": time.time()
    }

    # 处理每个文件
    for input_file in text_files:
        # 构建输出文件路径
        rel_path = input_file.relative_to(input_path)
        output_file = Path(output_dir) / rel_path

        # 处理文件
        result = filter_text_file(str(input_file), str(output_file), model, api_base, workers)

        # 更新统计
        if result.get("error"):
            total_stats["files_error"] += 1
        else:
            total_stats["files_processed"] += 1
            total_stats["total_chunks"] += result["total"]
            total_stats["kept_chunks"] += result["kept"]
            total_stats["pre_filtered_chunks"] += result["pre_filter"]
            total_stats["ai_filtered_chunks"] += result["ai_filter"]

    # 计算处理时间
    elapsed_time = time.time() - total_stats["start_time"]

    # 输出总体统计
    print("\n" + "="*50)
    print(f"目录处理完成: {input_dir} -> {output_dir}")
    print(f"处理时间: {elapsed_time:.2f} 秒")
    print(f"处理文件: {total_stats['files_processed']} 个成功, {total_stats['files_error']} 个失败")
    print(f"文本块总数: {total_stats['total_chunks']} 个")
    print(f"  - 保留: {total_stats['kept_chunks']} 个 ({total_stats['kept_chunks']/total_stats['total_chunks']*100:.1f}%)")
    print(f"  - 预过滤移除: {total_stats['pre_filtered_chunks']} 个 ({total_stats['pre_filtered_chunks']/total_stats['total_chunks']*100:.1f}%)")
    print(f"  - AI判断移除: {total_stats['ai_filtered_chunks']} 个 ({total_stats['ai_filtered_chunks']/total_stats['total_chunks']*100:.1f}%)")
    print("="*50)

def main():
    parser = argparse.ArgumentParser(description='使用本地AI过滤文件夹中不需要翻译的文本内容')
    parser.add_argument('--input', '-i', required=True, help='输入文件或目录路径')
    parser.add_argument('--output', '-o', required=True, help='输出文件或目录路径')
    parser.add_argument('--model', '-m', default='aispin/qwen2.5-7b-instruct-abliterated-v2.q4_k_s.gguf', help='Ollama模型名称')
    parser.add_argument('--api', '-a', default='http://localhost:11434', help='Ollama API地址')
    parser.add_argument('--workers', '-w', type=int, default=4, help='并行处理的线程数')
    parser.add_argument('--extensions', '-e', nargs='+', default=['.txt', '.ini', '.cfg', '.json', '.xml', '.csv'],
                        help='要处理的文件扩展名列表，如 .txt .ini .cfg')

    args = parser.parse_args()

    # 规范化文件扩展名
    extensions = [ext if ext.startswith('.') else f'.{ext}' for ext in args.extensions]

    print(f"使用模型: {args.model}")
    print(f"API地址: {args.api}")
    print(f"并行线程数: {args.workers}")
    print(f"处理的文件类型: {', '.join(extensions)}")

    # 检查输入路径是文件还是目录
    if os.path.isfile(args.input):
        # 单文件处理
        os.makedirs(os.path.dirname(args.output), exist_ok=True)
        filter_text_file(args.input, args.output, args.model, args.api, args.workers)
    else:
        # 目录处理
        process_directory(args.input, args.output, args.model, args.api, args.workers, extensions)

if __name__ == "__main__":
    main()