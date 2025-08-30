# 代码生成时间: 2025-08-30 20:41:53
import os
import shutil
import numpy as np
from datetime import datetime


class FolderStructureOrganizer:
    """
    A class to organize the folder structure by moving files into
    categorized subfolders based on their file types.
    """

    def __init__(self, root_dir):
        """
        Initialize the FolderStructureOrganizer with a root directory.
        """
        self.root_dir = root_dir
        self.file_types = {
            'images': ['.jpg', '.jpeg', '.png', '.gif'],
            'documents': ['.pdf', '.doc', '.docx', '.txt'],
            'videos': ['.mp4', '.avi', '.mov'],
            'audios': ['.mp3', '.wav']
        }

    def organize(self):
        """
        Organize the files in the root directory by moving them into
        subfolders based on their file types.
        """
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                file_path = os.path.join(root, file)
                file_extension = os.path.splitext(file)[1].lower()
                if file_extension in self.file_types['images']:
                    self.move_file(file_path, 'images')
                elif file_extension in self.file_types['documents']:
                    self.move_file(file_path, 'documents')
                elif file_extension in self.file_types['videos']:
                    self.move_file(file_path, 'videos')
                elif file_extension in self.file_types['audios']:
                    self.move_file(file_path, 'audios')

    def move_file(self, file_path, category):
        """
        Move a file to a categorized subfolder.
        """
        try:
            dest_folder = os.path.join(self.root_dir, category)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(file_path, dest_folder)
            print(f"Moved {file_path} to {dest_folder}")
        except Exception as e:
            print(f"Error moving file {file_path}: {str(e)}")


if __name__ == '__main__':
    # Example usage
    organizer = FolderStructureOrganizer('/path/to/your/folder')
    organizer.organize()