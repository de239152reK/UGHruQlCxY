# 代码生成时间: 2025-09-01 02:49:19
import numpy as np
import unittest

"""
A simple unit testing framework using Python and NumPy.
This framework is designed to be easy to understand, with clear structure,
appropriate error handling, and necessary comments and documentation.
It follows Python best practices and ensures maintainability and scalability.
"""

class NumericalTest(unittest.TestCase):
    """Test class for numerical operations using NumPy."""

    def test_addition(self):
        """Test NumPy addition."""
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        expected_result = np.array([5, 7, 9])
        self.assertTrue(np.array_equal(np.add(a, b), expected_result),
                        f"Expected {expected_result}, got {np.add(a, b)}")

    def test_subtraction(self):
        """Test NumPy subtraction."""
        a = np.array([10, 20, 30])
        b = np.array([4, 5, 6])
        expected_result = np.array([6, 15, 24])
        self.assertTrue(np.array_equal(np.subtract(a, b), expected_result),
                        f"Expected {expected_result}, got {np.subtract(a, b)}")

    def test_multiplication(self):
        """Test NumPy multiplication."""
        a = np.array([1, 2, 3])
        b = np.array([4, 5, 6])
        expected_result = np.array([4, 10, 18])
        self.assertTrue(np.array_equal(np.multiply(a, b), expected_result),
                        f"Expected {expected_result}, got {np.multiply(a, b)}")

    def test_division(self):
        """Test NumPy division."""
        a = np.array([10, 20, 30])
        b = np.array([2, 5, 6])
        expected_result = np.array([5.0, 4.0, 5.0])
        self.assertTrue(np.allclose(np.divide(a, b), expected_result),
                        f"Expected {expected_result}, got {np.divide(a, b)}")

    def test_power(self):
        """Test NumPy power."""
        a = np.array([1, 2, 3])
        b = np.array([2, 3, 4])
        expected_result = np.array([1, 8, 81])
        self.assertTrue(np.array_equal(np.power(a, b), expected_result),
                        f"Expected {expected_result}, got {np.power(a, b)}")

# Run the unit tests
if __name__ == '__main__':
    unittest.main(argv=[''], verbosity=2, exit=False)