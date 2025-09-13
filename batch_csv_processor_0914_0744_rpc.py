# 代码生成时间: 2025-09-14 07:44:55
import numpy as np
import pandas as pd
import os
from glob import glob

"""
CSV文件批量处理器

该程序可以批量处理指定目录下的所有CSV文件，支持基本的数据操作如读取、处理和保存。
"""

def process_csv_files(directory: str, output_directory: str):
    """
    处理指定目录下的所有CSV文件
    
    参数：
    directory: 包含CSV文件的目录路径
    output_directory: 处理后的CSV文件存储目录路径
    """
    # 确保输出目录存在
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    # 读取目录下的所有CSV文件
    csv_files = glob(os.path.join(directory, '*.csv'))
    for file_path in csv_files:
        try:
            # 读取CSV文件
            df = pd.read_csv(file_path)
            
            # 这里可以添加对数据的处理逻辑，例如：
            # df['column_name'] = df['column_name'].apply(some_function)
            
            # 保存处理后的CSV文件
            output_file_path = os.path.join(output_directory, os.path.basename(file_path))
            df.to_csv(output_file_path, index=False)
            print(f"Processed file: {file_path} -> {output_file_path}")
        except Exception as e:
            print(f"Error processing file: {file_path}. Error: {e}")


def some_function(value):
    """
    示例函数，用于演示如何在数据上应用自定义函数
    """
    # 这里可以实现具体的数据处理逻辑
    return value * 2

if __name__ == '__main__':
    # 示例用法
    directory = input("请输入包含CSV文件的目录路径：")
    output_directory = input("请输入处理后的CSV文件存储目录路径：")
    process_csv_files(directory, output_directory)