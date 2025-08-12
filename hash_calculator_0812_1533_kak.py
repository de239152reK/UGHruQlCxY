# 代码生成时间: 2025-08-12 15:33:42
import hashlib
import numpy as np

"""
哈希值计算工具
"""

def calculate_hash(data, algorithm='sha256', encoding='utf-8', output_format='hexdigest'):
    """
    计算给定数据的哈希值
    
    参数:
    data (str or bytes): 输入数据
    algorithm (str): 哈希算法，默认为'sha256'
    encoding (str): 输入数据编码，默认为'utf-8'
    output_format (str): 输出格式，默认为'hexdigest'
    
    返回:
    str: 计算得到的哈希值
    
    异常:
    ValueError: 如果algorithm不支持
    """
    # 支持的哈希算法列表
    supported_algorithms = [
        'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512'
    ]
    
    # 检查algorithm是否支持
    if algorithm not in supported_algorithms:
        raise ValueError(f"不支持的算法: {algorithm}. 支持的算法: {supported_algorithms}")
    
    # 将输入数据转换为bytes
    if isinstance(data, str):
        data = data.encode(encoding)
    
    # 创建哈希对象
    hash_object = hashlib.new(algorithm, data)
    
    # 根据output_format返回哈希值
    if output_format == 'hexdigest':
        return hash_object.hexdigest()
    elif output_format == 'digest':
        return hash_object.digest()
    else:
        raise ValueError(f"不支持的output_format: {output_format}. 支持的格式: 'hexdigest', 'digest'")


def main():
    """
    程序入口函数
    """
    # 示例数据
    data = "Hello, World!"
    
    # 计算哈希值
    try:
        hash_value = calculate_hash(data)
        print(f"哈希值（sha256）: {hash_value}")
        
        # 计算其他算法的哈希值
        hash_value = calculate_hash(data, algorithm='md5')
        print(f"哈希值（md5）: {hash_value}")
    except ValueError as e:
        print(f"错误: {e}")

def __str__(self):
    return f"hash_calculator: {self}"

def __init__(self):
    pass

def __del__(self):
    pass

def __repr__(self):
    return self.__str__()

def __lt__(self, other):
    pass

def __le__(self, other):
    pass

def __eq__(self, other):
    pass

def __ne__(self, other):
    pass

def __gt__(self, other):
    pass

def __ge__(self, other):
    pass

def __hash__(self):
    import sys
    return hash(id(self))
# 测试
if __name__ == '__main__':
    main()