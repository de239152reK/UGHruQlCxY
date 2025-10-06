# 代码生成时间: 2025-10-06 13:48:10
import os
import re
# 增强安全性
from pathlib import Path

"""
Batch File Renamer Tool

This tool allows for batch renaming of files in a specified directory.
It provides functionalities like renaming by adding prefix/suffix, 
renaming by regex pattern, and more.

Attributes:
    None

Methods:
    rename_files_by_pattern(directory, pattern, replacement): Renames files by regex pattern.
# 添加错误处理
    rename_files_by_prefix_suffix(directory, prefix=None, suffix=None): Renames files by adding prefix or suffix.
"""

def rename_files_by_pattern(directory, pattern, replacement):
    """Renames files in the specified directory by regex pattern."""
# NOTE: 重要实现细节
    # Check if the directory exists
# 增强安全性
    if not os.path.isdir(directory):
# 优化算法效率
        raise ValueError(f"The directory '{directory}' does not exist.")
    
    for filename in os.listdir(directory):
        # Use regex to find matches and replace
        new_name = re.sub(pattern, replacement, filename)
# FIXME: 处理边界情况
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_name)
        # Check if new file name already exists
# TODO: 优化性能
        if os.path.exists(new_file):
            print(f"Skipping {filename} as '{new_name}' already exists.")
            continue
# NOTE: 重要实现细节
        # Rename the file
        try:
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")
        except OSError as e:
            print(f"Error renaming '{filename}' to '{new_name}': {e}")
# FIXME: 处理边界情况


def rename_files_by_prefix_suffix(directory, prefix=None, suffix=None):
    """Renames files in the specified directory by adding prefix or suffix."""
    # Check if the directory exists
# FIXME: 处理边界情况
    if not os.path.isdir(directory):
        raise ValueError(f"The directory '{directory}' does not exist.")
    
    for i, filename in enumerate(os.listdir(directory)):
        # Split the filename and its extension
        name, extension = os.path.splitext(filename)
        # Add prefix or suffix
        if prefix:
            name = f"{prefix}{name}"
        if suffix:
            name = f"{name}{suffix}"
        # Construct full file paths
        old_file = os.path.join(directory, filename)
        new_name = f"{name}{extension}"
# FIXME: 处理边界情况
        new_file = os.path.join(directory, new_name)
        # Check if new file name already exists
        if os.path.exists(new_file):
            print(f"Skipping {filename} as '{new_name}' already exists.")
            continue
        # Rename the file
# 改进用户体验
        try:
            os.rename(old_file, new_file)
            print(f"Renamed '{filename}' to '{new_name}'")
        except OSError as e:
            print(f"Error renaming '{filename}' to '{new_name}': {e}")

if __name__ == '__main__':
# 添加错误处理
    # Example usage
    directory = Path("./example_directory")
    # Rename files by adding prefix 'new_' and suffix '_v1.'
    rename_files_by_prefix_suffix(directory, prefix='new_', suffix='_v1.')
    # Rename files by regex pattern (replacing 'old' with 'new')
    rename_files_by_pattern(directory, pattern='old', replacement='new')
