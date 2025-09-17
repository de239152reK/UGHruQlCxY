# 代码生成时间: 2025-09-18 05:41:06
import json
import numpy as np
# TODO: 优化性能

"""
JSON数据格式转换器

该程序用于将JSON格式的数据转换为NumPy数组，或将NumPy数组转换回JSON格式。
提供错误处理和用户友好的接口。
"""

class JsonConverter:
# TODO: 优化性能
    """JSON数据格式转换器类"""

    def __init__(self):
        """初始化转换器"""
        pass

    def json_to_numpy(self, json_data):
        """将JSON数据转换为NumPy数组

        Args:
            json_data (str): JSON格式的字符串

        Returns:
            numpy.ndarray: 转换后的NumPy数组

        Raises:
            ValueError: 如果JSON数据格式不正确
        """
        try:
# 扩展功能模块
            data = json.loads(json_data)
            return np.array(data)
        except json.JSONDecodeError as e:
            raise ValueError("Invalid JSON data") from e

    def numpy_to_json(self, numpy_array):
# 改进用户体验
        """将NumPy数组转换为JSON数据

        Args:
            numpy_array (numpy.ndarray): NumPy数组

        Returns:
            str: 转换后的JSON格式字符串

        Raises:
            TypeError: 如果输入不是NumPy数组
        """
        if not isinstance(numpy_array, np.ndarray):
            raise TypeError("Input must be a NumPy array")
        return json.dumps(numpy_array.tolist())

# 示例用法
if __name__ == "__main__":
    json_converter = JsonConverter()

    # JSON转NumPy
    json_data = '[1, 2, 3, 4, 5]'
    try:
        numpy_array = json_converter.json_to_numpy(json_data)
        print("NumPy Array:", numpy_array)
    except ValueError as e:
# 改进用户体验
        print(e)

    # NumPy转JSON
    try:
        json_result = json_converter.numpy_to_json(numpy_array)
        print("JSON Result:", json_result)
    except TypeError as e:
        print(e)