# 代码生成时间: 2025-08-23 15:10:50
import numpy as np
import pandas as pd

"""
A data cleaning and preprocessing tool using Python and NumPy.
This tool is designed to handle various data cleaning and
preprocessing tasks, such as handling missing values,
scaling data, and encoding categorical variables.
"""

class DataCleaner:
    """A class to perform data cleaning and preprocessing tasks."""

    def __init__(self, data):
        """Initialize the DataCleaner with raw data."""
        if not isinstance(data, pd.DataFrame):
            raise ValueError("Data must be a pandas DataFrame.")
        self.data = data

    def handle_missing_values(self, strategy='mean'):
        "