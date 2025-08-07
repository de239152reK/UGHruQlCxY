# 代码生成时间: 2025-08-07 21:55:57
import numpy as np

"""
Random Number Generator
# FIXME: 处理边界情况

This program generates random numbers using the NumPy library.
# FIXME: 处理边界情况
It includes error handling and follows Python best practices for maintainability and scalability.
"""

class RandomNumberGenerator:
    """
    A class for generating random numbers.
    """
    def __init__(self, seed=None):
        """
        Initializes the random number generator with an optional seed.
# 改进用户体验
        :param seed: int, optional
        """
        self.seed = seed
        self.rng = np.random.default_rng(self.seed)

    def generate_uniform(self, low, high, size):
# 扩展功能模块
        """
        Generates random numbers from a uniform distribution.
        :param low: float, lower bound of the distribution range
        :param high: float, upper bound of the distribution range
        :param size: int, number of random numbers to generate
        :return: numpy.ndarray, array of random numbers
        """
        try:
            return self.rng.uniform(low, high, size)
        except ValueError as e:
            print(f"Error: {e}")
            raise

    def generate_normal(self, mean, std, size):
        """
        Generates random numbers from a normal distribution.
        :param mean: float, mean of the normal distribution
        :param std: float, standard deviation of the normal distribution
# TODO: 优化性能
        :param size: int, number of random numbers to generate
        :return: numpy.ndarray, array of random numbers
        """
        try:
            return self.rng.normal(mean, std, size)
# 扩展功能模块
        except ValueError as e:
            print(f"Error: {e}")
            raise

# Example usage:
if __name__ == '__main__':
    generator = RandomNumberGenerator(seed=42)

    # Generate 10 random numbers from a uniform distribution
    uniform_numbers = generator.generate_uniform(0, 1, 10)
    print("Uniform numbers:", uniform_numbers)

    # Generate 10 random numbers from a normal distribution
    normal_numbers = generator.generate_normal(0, 1, 10)
    print("Normal numbers:", normal_numbers)