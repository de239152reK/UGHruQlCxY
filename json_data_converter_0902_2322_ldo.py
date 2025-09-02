# 代码生成时间: 2025-09-02 23:22:11
import json
import numpy as np
"""
JSON数据格式转换器，用于将JSON格式的数据转换为NumPy数组。
"""

def json_to_numpy(json_data):
    """
    将JSON格式的数据转换为NumPy数组。

    参数:
    json_data (str): JSON格式的字符串数据。

    返回:
    numpy.ndarray: 转换后的NumPy数组。

    抛出:
    ValueError: 当JSON数据格式不正确时。
    """
    try:
        # 解析JSON数据
        data = json.loads(json_data)
        # 将数据转换为NumPy数组
        return np.array(data)
    except json.JSONDecodeError:
        raise ValueError("JSON数据格式不正确")


def main():
    """
    主函数，用于演示JSON数据格式转换器的使用。
    """
    # 示例JSON数据
    json_data = '[1, 2, 3, 4, 5]'

    try:
        # 将JSON数据转换为NumPy数组
        numpy_array = json_to_numpy(json_data)
        print("转换后的NumPy数组: ", numpy_array)
    except ValueError as e:
        print("错误: ", e)

if __name__ == "__main__":
    main()