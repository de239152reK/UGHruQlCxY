# 代码生成时间: 2025-08-11 13:47:59
import hashlib
import numpy as np

"""
哈希值计算工具
使用Python和NumPy框架，实现哈希值计算功能。
该工具支持SHA256、SHA512等多种哈希算法。

使用方法：
1. 从字符串或文件中读取数据
2. 选择哈希算法
3. 计算哈希值并返回结果
"""

def calculate_hash(data, algorithm='sha256'):
    """计算数据的哈希值
    
    参数：
    data (str or bytes): 待计算哈希值的数据
    algorithm (str): 哈希算法名称，默认为'sha256'
        支持的算法包括：'sha256', 'sha512', 'md5', 'sha1'
    
    返回：
    str: 计算得到的哈希值（十六进制字符串）
    
    异常：
    - ValueError: 未知的哈希算法
    """
    if not isinstance(data, (str, bytes)):
        raise TypeError("数据类型必须是字符串或字节序列")
    
    # 将字符串数据转换为字节序列
    if isinstance(data, str):
        data = data.encode('utf-8')
    
    # 选择哈希算法
    hash_algorithms = {
        'sha256': hashlib.sha256,
        'sha512': hashlib.sha512,
        'md5': hashlib.md5,
        'sha1': hashlib.sha1
    }
    
    if algorithm not in hash_algorithms:
        raise ValueError(f"未知的哈希算法：{algorithm}")
    
    # 计算哈希值
    hash_func = hash_algorithms[algorithm]
    hash_value = hash_func(data).hexdigest()
    
    return hash_value


# 从文件中读取数据
def read_data_from_file(file_path):
    """从文件中读取数据
    
    参数：
    file_path (str): 文件路径
    
    返回：
    bytes: 文件内容
    
    异常：
    - FileNotFoundError: 文件不存在
    - PermissionError: 文件读取权限不足
    """
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"文件不存在：{file_path}")
    except PermissionError:
        raise PermissionError(f"文件读取权限不足：{file_path}")


# 示例用法
if __name__ == '__main__':
    # 计算字符串的哈希值
    string_data = "Hello, World!"
    print("字符串哈希值：", calculate_hash(string_data))
    
    # 计算文件的哈希值
    file_path = "example.txt"
    try:
        file_data = read_data_from_file(file_path)
        print("文件哈希值：", calculate_hash(file_data))
    except (FileNotFoundError, PermissionError) as e:
        print(e)