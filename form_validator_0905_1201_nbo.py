# 代码生成时间: 2025-09-05 12:01:39
import numpy as np

"""
This module provides a basic form validator using Python and NumPy.
It checks if form data (represented as a dictionary) satisfies
various constraints, such as data type, value range, and presence."""

class FormDataValidator:
    """
    A class to validate form data against defined constraints.
    """
    def __init__(self):
        # Constraints dictionary
        self.constraints = {}

    def add_constraint(self, field_name, constraint_func):
        """
        Add a constraint function to the constraints dictionary.
        :param field_name: The name of the field to add constraint for.
        :param constraint_func: A function that takes a value and returns True if the value
                              satisfies the constraint, False otherwise.
        """
        self.constraints[field_name] = constraint_func

    def validate(self, form_data):
        """
        Validate the form data against the constraints.
        :param form_data: A dictionary containing the form data to validate.
        :return: A tuple containing a list of valid fields and a list of error messages.
        """
        valid_fields = []
        error_messages = []
        for field_name, value in form_data.items():
            if field_name in self.constraints:
                try:
                    if self.constraints[field_name](value):
                        valid_fields.append(field_name)
                    else:
                        error_messages.append(f"Invalid value for field '{field_name}': {value}")
                except Exception as e:
                    error_messages.append(f"Error validating field '{field_name}': {str(e)}")
            else:
                error_messages.append(f"No constraint defined for field '{field_name}'")
        return valid_fields, error_messages

# Example constraint functions
def is_positive(value):
    """
    Check if a value is a positive number.
    :param value: The value to check.
    :return: True if the value is positive, False otherwise.
    """
    return np.isreal(value) and value > 0

def is_string(value):
    """
    Check if a value is a string.
    :param value: The value to check.
    :return: True if the value is a string, False otherwise.
    """
    return isinstance(value, str)

# Usage example
if __name__ == '__main__':
    validator = FormDataValidator()
    validator.add_constraint('field1', is_positive)
    validator.add_constraint('field2', is_string)

    form_data = {
        'field1': -10,
        'field2': 'Hello World',
        'field3': 5,  # No constraint defined
    }

    valid_fields, error_messages = validator.validate(form_data)
    print('Valid fields:', valid_fields)
    print('Error messages:', error_messages)