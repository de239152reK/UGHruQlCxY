# 代码生成时间: 2025-10-08 02:43:24
import os
import re
from pathlib import Path
import numpy as np

"""
A batch file renamer tool that renames files in a specified directory
based on a given pattern.

Attributes:
    None

Methods:
    rename_files(directory, pattern, replacement): Renames files in the directory
    based on the provided pattern and replacement.
"""

def rename_files(directory, pattern, replacement):
    """
    Renames files in the specified directory based on the given pattern.

    Args:
        directory (str): The directory path where files are located.
        pattern (str): The pattern to match in the file names.
        replacement (str): The replacement string for matched patterns.

    Returns:
        None
    """
    # Convert directory path to a Path object for easy path manipulation
    path = Path(directory)

    # Check if the directory exists
    if not path.is_dir():
        raise ValueError(f"The directory {directory} does not exist.")

    # Iterate over each file in the directory
    for file in path.iterdir():
        # Check if it's a file
        if file.is_file():
            # Get the file name and extension
            file_name = file.stem
            file_ext = file.suffix

            # Replace the pattern in the file name with the replacement string
            new_name = re.sub(pattern, replacement, file_name)

            # Construct the full new file path
            new_file_path = path / f"{new_name}{file_ext}"

            # Check if the new file name already exists to avoid overwriting files
            if new_file_path.exists():
                print(f"Skipping {file_name}{file_ext}, as new file name already exists.")
                continue

            # Rename the file
            try:
                file.rename(new_file_path)
                print(f"Renamed {file_name}{file_ext} to {new_name}{file_ext}")
            except Exception as e:
                print(f"Error renaming {file_name}{file_ext}: {str(e)}")

# Example usage
if __name__ == '__main__':
    # Specify the directory containing the files to rename
    directory = 'path_to_your_directory'
    # Specify the pattern to match in file names
    pattern = 'old_name'
    # Specify the replacement string for the matched pattern
    replacement = 'new_name'

    # Call the rename_files function
    rename_files(directory, pattern, replacement)