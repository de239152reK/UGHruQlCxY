# 代码生成时间: 2025-09-20 18:13:09
import os
import shutil
from datetime import datetime

"""
Folder Structure Organizer

This script organizes the files in a specified directory by moving them into subdirectories based on their file extensions.
It also includes error handling and logging for better maintainability and extensibility.
"""

class FolderStructureOrganizer:
    def __init__(self, source_dir, target_dir):
        self.source_dir = source_dir
        self.target_dir = target_dir

    def create_extension_subdirs(self):
        """Create subdirectories for each file extension in the target directory."""
        for file in os.listdir(self.source_dir):
            extension = os.path.splitext(file)[1]
            if extension:
                subdir_path = os.path.join(self.target_dir, extension[1:])
                os.makedirs(subdir_path, exist_ok=True)

    def organize_files(self):
        """Move files into corresponding subdirectories based on their extensions."""
        try:
            self.create_extension_subdirs()
            for file in os.listdir(self.source_dir):
                extension = os.path.splitext(file)[1]
                if extension:
                    source_file_path = os.path.join(self.source_dir, file)
                    subdir_path = os.path.join(self.target_dir, extension[1:])
                    target_file_path = os.path.join(subdir_path, file)
                    shutil.move(source_file_path, target_file_path)
        except Exception as e:
            print(f"An error occurred: {e}")

    def run(self):
        "