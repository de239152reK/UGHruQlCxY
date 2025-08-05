# 代码生成时间: 2025-08-05 10:23:33
import numpy as np

"""
Math Calculator is a Python module that provides a set of mathematical functions
using the NumPy library. It is designed to be easily understandable, maintainable,
and extensible, following Python best practices.
"""

class MathCalculator:
    """Mathematical operations using NumPy."""

    def add(self, a, b):
        """Add two numbers.
        
        Args:
            a (float): First number.
            b (float): Second number.
# 添加错误处理
        
        Returns:
            float: The sum of a and b.
        """
        return np.add(a, b)

    def subtract(self, a, b):
        """Subtract two numbers.
        
        Args:
            a (float): First number.
            b (float): Second number.
        
        Returns:
            float: The difference between a and b.
        """
        return np.subtract(a, b)

    def multiply(self, a, b):
        """Multiply two numbers.
        
        Args:
            a (float): First number.
            b (float): Second number.
        
        Returns:
# FIXME: 处理边界情况
            float: The product of a and b.
        """
        return np.multiply(a, b)

    def divide(self, a, b):
        """Divide two numbers with error handling.
# NOTE: 重要实现细节
        
        Args:
# 增强安全性
            a (float): Numerator.
            b (float): Denominator.
        
        Returns:
            float: The quotient of a divided by b.
        
        Raises:
            ZeroDivisionError: If b is zero.
        """
        if b == 0:
            raise ZeroDivisionError('Cannot divide by zero.')
        return np.divide(a, b)
# 增强安全性

    def power(self, a, b):
        """Calculate the power of a number.
        
        Args:
            a (float): Base number.
            b (float): Exponent.
# 优化算法效率
        
        Returns:
            float: The result of a raised to the power of b.
        """
        return np.power(a, b)

    def square_root(self, a):
        """Calculate the square root of a number.
        
        Args:
            a (float): The number to take the square root of.
        
        Returns:
            float: The square root of a.
        """
# NOTE: 重要实现细节
        return np.sqrt(a)
# FIXME: 处理边界情况

# Example usage
if __name__ == '__main__':
    calc = MathCalculator()
    print("Addition: 5 + 3 =", calc.add(5, 3))
    print("Subtraction: 5 - 3 =", calc.subtract(5, 3))
    print("Multiplication: 5 * 3 =", calc.multiply(5, 3))
    try:
# NOTE: 重要实现细节
        print("Division: 5 / 3 =", calc.divide(5, 3))
        print("Division: 5 / 0 =", calc.divide(5, 0))
    except ZeroDivisionError as e:
        print("Error:", e)
    print("Power: 5 ^ 3 =", calc.power(5, 3))
    print("Square Root: sqrt(9) =", calc.square_root(9))
# 扩展功能模块
