#!/usr/bin/env python3
import os
import re
import shutil
from datetime import datetime

def convert_daily_to_posts():
    # 设置源目录和目标目录
    source_dir = './Daily'
    target_dir = './_posts'
    
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)
    
    # 遍历源目录中的所有文件
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file.endswith('.md'):
                # 获取文件完整路径
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # 提取年份目录
                year_match = re.search(r'Daily/(\d{4})', root)
                if not year_match:
                    print(f"跳过文件 {file_path}：无法提取年份")
                    continue
                year = year_match.group(1)
                
                # 解析文件名，提取日期和标题
                # 处理两种文件名格式：YYYYMMDD-标题.md 或 YYYY-MM-DD-标题.md
                date_title_pattern = re.compile(r'^(\d{4})(\d{2})(\d{2})-(.+?)\.md$')
                date_title_pattern_dash = re.compile(r'^(\d{4})-(\d{2})-(\d{2})-(.+?)\.md$')
                
                match = date_title_pattern.match(file)
                if match:
                    year_file, month, day, title = match.groups()
                    # 确保年份一致
                    if year_file != year:
                        print(f"跳过文件 {file_path}：文件名年份与目录年份不一致")
                        continue
                else:
                    match = date_title_pattern_dash.match(file)
                    if match:
                        year_file, month, day, title = match.groups()
                        if year_file != year:
                            print(f"跳过文件 {file_path}：文件名年份与目录年份不一致")
                            continue
                    else:
                        print(f"跳过文件 {file_path}：文件名格式不符合要求")
                        continue
                
                # 从文件内容中提取标题
                content_lines = content.split('\n')
                if content_lines and content_lines[0].startswith('# '):
                    markdown_title = content_lines[0][2:].strip()
                    # 删除内容中的标题行
                    content = '\n'.join(content_lines[1:])
                else:
                    # 如果没有标题行，使用文件名作为标题
                    markdown_title = title.replace('-', ' ').title()
                
                # 提取日期（如果文件内容中有）
                date_in_content = None
                for line in content_lines[1:3]:  # 检查前几行
                    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', line)
                    if date_match:
                        date_in_content = date_match.group(1)
                        # 删除内容中的日期行
                        content = content.replace(line + '\n', '')
                        break
                
                # 构建日期字符串
                date_str = date_in_content if date_in_content else f"{year}-{month}-{day}"
                
                # 创建YAML Front Matter
                front_matter = f"""---
title: "{markdown_title}"
date: {date_str}
category: Daily
tags: [daily]
---
"""
                
                # 合并内容
                new_content = front_matter + content
                
                # 构建新文件名
                new_filename = f"{date_str}-{title}.md"
                new_file_path = os.path.join(target_dir, new_filename)
                
                # 检查文件是否已存在
                if os.path.exists(new_file_path):
                    print(f"跳过文件 {file_path}：目标文件 {new_filename} 已存在")
                    continue
                
                # 写入新文件
                with open(new_file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                
                print(f"转换完成：{file_path} -> {new_file_path}")
    
    print("\n转换完成！")

if __name__ == "__main__":
    convert_daily_to_posts()