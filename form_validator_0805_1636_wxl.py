# 代码生成时间: 2025-08-05 16:36:08
import numpy as np

"""
Form Validator

This module provides functionality to validate form data using numpy arrays.
It can be used to check if the data is numeric and within a specified range."""

class FormValidator:
    """
    A class to validate form data.

    Attributes:
        range_min (float): The minimum value of the valid range.
        range_max (float): The maximum value of the valid range.
    """
    def __init__(self, range_min, range_max):
        """
        Initialize the validator with a range.

        Args:
            range_min (float): The minimum value for the valid range.
            range_max (float): The maximum value for the valid range.
        """
        self.range_min = range_min
        self.range_max = range_max

    def is_valid(self, data):
        """
        Check if the data is numeric and within the specified range.

        Args:
            data (numpy array): The data to be validated.

        Returns:
            bool: True if the data is valid, False otherwise.
        """
        try:
            # Convert data to numpy array
            data_array = np.array(data)

            # Check if the data array is numeric
            if not np.issubdtype(data_array.dtype, np.number):
                return False

            # Check if the data is within the specified range
            if np.all((data_array >= self.range_min) & (data_array <= self.range_max)):
                return True
            else:
                return False
        except Exception as e:
            # Handle any exceptions that occur during validation
            print(f"Error: {e}")
            return False

    def validate_and_return(self, data):
        """
        Validate the data and return it if it is valid.
        Otherwise, return None.

        Args:
            data (numpy array): The data to be validated.

        Returns:
            numpy array or None: The validated data if it is valid, otherwise None.
        """
        if self.is_valid(data):
            return data
        else:
            return None

# Example usage
if __name__ == "__main__":
    # Create a validator with a range from 0 to 100
    validator = FormValidator(0, 100)

    # Test data
    test_data = [10, 20, 30, 110]  # The last value is out of range

    # Validate the data
    validated_data = validator.validate_and_return(test_data)

    # Print the result
    if validated_data is not None:
        print("Valid data:", validated_data)
    else:
        print("Invalid data.")