# 代码生成时间: 2025-08-21 01:13:17
import os
import shutil
from pathlib import Path
import numpy as np

"""
Folder Structure Optimizer

This program is designed to organize the folder structure in a specified directory.
It moves all files into subfolders based on their extensions.
"""

class FolderStructureOptimizer:
    def __init__(self, source_folder):
        self.source_folder = Path(source_folder)
        self.extensions = self._get_extensions()
        """Initialize the folder structure optimizer with the source directory."""

    def _get_extensions(self):
        """Get all unique file extensions in the source folder."""
        extensions = set()
        for path in self.source_folder.rglob('*'):
            if path.is_file():
                extensions.add(path.suffix)
        return extensions

    def optimize(self):
        "