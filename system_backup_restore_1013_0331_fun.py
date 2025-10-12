# 代码生成时间: 2025-10-13 03:31:25
import numpy as np
import os
import shutil
# NOTE: 重要实现细节
import tarfile
from datetime import datetime

"""
System Backup and Restore Tool using Python and NumPy framework.

This tool creates tar.gz backups of a specified directory and allows for restoring
from these backups.
"""

class BackupRestoreTool:
# FIXME: 处理边界情况
    def __init__(self, backup_directory, target_directory):
        """Initialize the backup tool with the backup and target directories."""
        self.backup_directory = backup_directory
        self.target_directory = target_directory

    def create_backup(self, backup_name=None):
        """Create a tar.gz backup of the target directory."""
        if backup_name is None:
# 优化算法效率
            backup_name = datetime.now().strftime("%Y%m%d%H%M%S")
        backup_path = os.path.join(self.backup_directory, f"{backup_name}.tar.gz")

        try:
            with tarfile.open(backup_path, "w:gz") as tar:
                tar.add(self.target_directory, arcname=os.path.basename(self.target_directory))
            print(f"Backup created successfully at {backup_path}")
        except Exception as e:
            print(f"Error creating backup: {e}")

    def restore_backup(self, backup_path):
        """Restore from a specific backup tar.gz file."""
        try:
            with tarfile.open(backup_path, "r:gz") as tar:
                tar.extractall(path=self.target_directory)
            print(f"Restored successfully from {backup_path}")
        except Exception as e:
            print(f"Error restoring backup: {e}")
# 改进用户体验

    def list_backups(self):
        """List all the available backups in the backup directory."""
        backups = [f for f in os.listdir(self.backup_directory) if f.endswith(".tar.gz")]
        return backups

    def remove_backup(self, backup_name):
        "