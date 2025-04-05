import os
import re
import argparse
from typing import List, Tuple
import subprocess
import json
import requests

def call_ollama(text: str, model: str = "aispin/qwen2.5-7b-instruct-abliterated-v2.q4_k_s.gguf") -> str:
    """调用Ollama API获取AI判断结果"""
    prompt = f"""
I need you to help me determine whether the following text needs to be translated.
Please analyze this text and determine whether it belongs to the following categories that do not need to be translated:
1. File name (such as xxx.anm, xxx.txt, etc.)
2. Variable name or code snippet
3. Coordinate value or value (such as x=1.65)
4. pure number or meaning less
5. Repeated content (such as 坐标：123，坐标：456)
Please just reply "yes" or "no" without adding any explanation.
text: "{text}"
    """

    cmd = ["ollama", "run", model, prompt]
    result = subprocess.run(cmd, capture_output=True, text=True)
    response = result.stdout.strip()

    # 简单解析结果
    if "no" in response:
        return "NO_TRANSLATE"
    else:
        return "TRANSLATE"

def call_ollama_api(text: str, model: str = "aispin/qwen2.5-7b-instruct-abliterated-v2.q4_k_s.gguf", api_base: str = "http://localhost:11434") -> str:
    """使用Ollama的HTTP API获取AI判断结果"""
    prompt = f"""
I need you to help me determine whether the following text needs to be translated.
Please analyze this text and determine whether it belongs to the following categories that do not need to be translated:
1. File name (such as xxx.anm, xxx.txt, etc.)
2. Variable name or code snippet
3. Coordinate value or value (such as x=1.65)
4. pure number or meaning less
5. Repeated content (such as 坐标：123，坐标：456)
Please just reply "yes" or "no" without adding any explanation.
text: "{text}"
"""

    api_url = f"{api_base}/api/generate"
    payload = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(api_url, json=payload)
        response.raise_for_status()
        result = response.json()
        response_text = result.get("response", "").strip()

        # 简单解析结果
        if "NO_TRANSLATE" in response_text:
            return "NO_TRANSLATE"
        else:
            return "TRANSLATE"
    except Exception as e:
        print(f"API调用错误: {e}")
        # 出错时默认保留文本
        return "TRANSLATE"



def split_text(text: str, max_length: int = 200) -> List[str]:
    """将文本分割成适当的块进行处理"""
    # 使用自然段落或行进行分割
    chunks = []
    lines = text.split('\n')

    current_chunk = ""
    for line in lines:
        if len(current_chunk) + len(line) <= max_length:
            current_chunk += line + '\n'
        else:
            if current_chunk:
                chunks.append(current_chunk.strip())
            current_chunk = line + '\n'

    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def filter_text(input_file: str, output_file: str, model: str = "qwen:7b", confidence_threshold: float = 0.8) -> None:
    """处理输入文件，过滤掉不需要翻译的内容"""
    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 分割文本
    chunks = split_text(content)

    # 预先过滤明显不需要翻译的内容
    pattern = r'([a-zA-Z0-9_\-\.]+\.[a-zA-Z0-9]{2,4}|x=[\-\d\.]+\s+y=[\-\d\.]+\s+z=[\-\d\.]+)'
    filtered_chunks = []

    for chunk in chunks:
        # 使用正则表达式预过滤
        if re.match(pattern, chunk.strip()):
            print(f"预过滤移除: {chunk}")
            continue

        # 使用AI判断
        result = call_ollama(chunk, model)

        if result == "TRANSLATE":
            filtered_chunks.append(chunk)
            print(f"保留: {chunk}")
        else:
            print(f"AI判断移除: {chunk}")

    # 写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(filtered_chunks))

    print(f"处理完成。原始文本行数: {len(chunks)}, 过滤后行数: {len(filtered_chunks)}")

def main():
    parser = argparse.ArgumentParser(description='使用本地AI过滤不需要翻译的文本内容')
    parser.add_argument('--input', '-i', required=True, help='输入文件路径')
    parser.add_argument('--output', '-o', required=True, help='输出文件路径')
    parser.add_argument('--model', '-m', default='qwen:7b', help='Ollama模型名称')

    args = parser.parse_args()

    print(f"开始处理文件: {args.input}")
    print(f"使用模型: {args.model}")

    filter_text(args.input, args.output, args.model)

    print(f"文本过滤完成，结果已保存至: {args.output}")

if __name__ == "__main__":
    main()