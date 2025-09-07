# 代码生成时间: 2025-09-07 16:29:58
import numpy as np
import unittest

"""自动化测试套件，用于测试numpy相关的操作。"""

# 定义一个测试类，继承自unittest.TestCase
class NumPyTests(unittest.TestCase):
    """测试numpy基本操作的测试类。"""
    
    # 测试numpy array创建
    def test_create_array(self):
        """测试创建numpy array是否正确。"""
        array = np.array([1, 2, 3])
        self.assertIsInstance(array, np.ndarray)
        self.assertEqual(array.shape, (3,))

    # 测试numpy array求和
    def test_sum_array(self):
        """测试numpy array求和是否正确。"""
        array = np.array([1, 2, 3])
        self.assertEqual(np.sum(array), 6)

    # 测试numpy array维度
    def test_array_shape(self):
        """测试numpy array的维度是否正确。"""
        array_1d = np.array([1, 2, 3])
        array_2d = np.array([[1, 2], [3, 4]])
        self.assertEqual(array_1d.shape, (3,))
        self.assertEqual(array_2d.shape, (2, 2))

    # 测试numpy array切片
    def test_array_slicing(self):
        """测试numpy array切片是否正确。"""
        array = np.array([1, 2, 3, 4, 5])
        sliced_array = array[1:4]
        self.assertEqual(sliced_array.tolist(), [2, 3, 4])

    # 测试numpy array广播机制
    def test_array_broadcasting(self):
        """测试numpy array广播机制是否正确。"""
        array_1d = np.array([1, 2, 3])
        array_2d = np.array([[1], [2], [3]])
        result = np.add(array_1d, array_2d)
        self.assertEqual(result.tolist(), [[2, 3, 4], [3, 4, 5], [4, 5, 6]])

    # 测试numpy array转置
    def test_array_transpose(self):
        """测试numpy array转置是否正确。"""
        array = np.array([[1, 2], [3, 4]])
        transposed_array = array.T
        self.assertEqual(transposed_array.tolist(), [[1, 3], [2, 4]])

    # 测试numpy array错误处理
    def test_array_error_handling(self):
        """测试numpy array错误处理是否正确。"""
        with self.assertRaises(ValueError):
            np.array([1, 2, 3], dtype='i2')  # 会引发ValueError，因为int类型不能表示太大的值

# 运行测试套件
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)