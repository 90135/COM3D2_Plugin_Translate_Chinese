#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import json
import argparse

def txt_to_json(line, source_mode=False):
    """将单行文本转换为键值对"""
    parts = line.rstrip('\n').split('\t', 1)
    key = parts[0].rstrip()
    value = key if source_mode else (parts[1].replace('\t', '') if len(parts) > 1 else '')
    return key, value

def json_to_txt(key, value):
    """将键值对转换为文本行"""
    return f"{key}\t{value}" if value else key

def process_file(input_path, output_path, mode, source_mode=False):
    """处理单个文件的转换"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            if mode == 'txt2json':
                data = {}
                for line in f:
                    if line.strip():  # 跳过空行
                        k, v = txt_to_json(line, source_mode)
                        data[k] = v
                with open(output_path, 'w', encoding='utf-8') as out:
                    json.dump(data, out, ensure_ascii=False, indent=4)
            else:
                with open(output_path, 'w', encoding='utf-8') as out:
                    data = json.load(f)
                    for k, v in data.items():
                        out.write(json_to_txt(k, v) + '\n')
        return True
    except Exception as e:
        print(f"处理文件 {os.path.basename(input_path)} 时出错: {str(e)}")
        return False

def batch_convert(input_dir, output_dir, mode, source_mode=False):
    """批量转换目录中的文件"""
    os.makedirs(output_dir, exist_ok=True)
    converted = 0

    for filename in os.listdir(input_dir):
        input_path = os.path.join(input_dir, filename)
        if os.path.isfile(input_path):
            # 生成输出文件名
            if mode == 'txt2json' and filename.endswith('.txt'):
                output_filename = f"{os.path.splitext(filename)[0]}.json"
            elif mode == 'json2txt' and filename.endswith('.json'):
                output_filename = f"{os.path.splitext(filename)[0]}.txt"
            else:
                continue

            output_path = os.path.join(output_dir, output_filename)
            if process_file(input_path, output_path, mode, source_mode):
                converted += 1
                print(f"成功转换: {filename} -> {output_filename}")

    print(f"\n总计转换文件: {converted} 个")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='文本与JSON双向转换工具')
    parser.add_argument('mode',
                        choices=['txt2json', 'json2txt'],
                        help='转换模式: txt2json 或 json2txt')
    parser.add_argument('-i', '--input',
                        required=True,
                        help='输入目录路径')
    parser.add_argument('-o', '--output',
                        required=True,
                        help='输出目录路径')
    # 添加 source 模式选项
    parser.add_argument('-s', '--source',
                        action='store_true',
                        help='启用源模式（值=键名）')

    args = parser.parse_args()

    print("开始转换...")
    batch_convert(args.input, args.output, args.mode, args.source)
    print(f"\n转换完成！结果保存在：{args.output}")