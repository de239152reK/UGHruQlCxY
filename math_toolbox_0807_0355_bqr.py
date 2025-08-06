# 代码生成时间: 2025-08-07 03:55:02
import numpy as np"""
Math Toolbox: A collection of mathematical calculation tools using Python and NumPy.
# 添加错误处理
"""

# Define a class for the math toolbox
class MathToolbox:
# 增强安全性
    """
    A class containing various mathematical operations.
    """
# 扩展功能模块
    def __init__(self):
        """Initialize the MathToolbox instance."""
# 改进用户体验
        pass

    def add(self, x, y):
# NOTE: 重要实现细节
        """Add two numbers.

        Args:
# 扩展功能模块
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The sum of x and y.
        """
        return x + y

    def subtract(self, x, y):
        """Subtract two numbers.

        Args:
            x (float): The first number.
            y (float): The second number.

        Returns:
            float: The difference of x and y.
        """
        return x - y

    def multiply(self, x, y):
        """Multiply two numbers.

        Args:
# FIXME: 处理边界情况
            x (float): The first number.
# FIXME: 处理边界情况
            y (float): The second number.

        Returns:
            float: The product of x and y.
        """
        return x * y

    def divide(self, x, y):
        """Divide two numbers.

        Args:
            x (float): The numerator.
            y (float): The denominator.

        Returns:
# 改进用户体验
            float: The quotient of x and y.
        
        Raises:
            ValueError: If the denominator is zero.
        """
        if y == 0:
# 增强安全性
            raise ValueError("Cannot divide by zero.")
        return x / y

    def power(self, x, y):
        """Raise a number to a power.

        Args:
            x (float): The base.
            y (float): The exponent.

        Returns:
            float: The result of x raised to the power of y.
        """
        return np.power(x, y)

    def sqrt(self, x):
        """Calculate the square root of a number.

        Args:
            x (float): The number.
# NOTE: 重要实现细节

        Returns:
            float: The square root of x.
        
        Raises:
# 增强安全性
            ValueError: If the number is negative.
        """
        if x < 0:
            raise ValueError("Cannot calculate square root of a negative number.")
        return np.sqrt(x)

# Example usage:
if __name__ == '__main__':
    toolbox = MathToolbox()
    print("Addition: 5 + 3 =", toolbox.add(5, 3))
    print("Subtraction: 5 - 3 =", toolbox.subtract(5, 3))
    print("Multiplication: 5 * 3 =", toolbox.multiply(5, 3))
    try:
        print("Division: 5 / 3 =", toolbox.divide(5, 3))
        print("Square root: sqrt(9) =", toolbox.sqrt(9))
    except ValueError as e:
        print(e)