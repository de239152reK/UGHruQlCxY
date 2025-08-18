# 代码生成时间: 2025-08-19 07:59:23
import os
import shutil
import logging
import numpy as np
from datetime import datetime

# 设置日志配置
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FileBackupSync:
    """文件备份和同步工具
    """

    def __init__(self, source_dir, backup_dir):
        """初始化函数
        
        :param source_dir: 源目录路径
        :param backup_dir: 备份目录路径
        """
        self.source_dir = source_dir
        self.backup_dir = backup_dir
        
        # 创建备份目录，如果不存在
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
            logging.info(f"创建备份目录：{self.backup_dir}")

    def backup_files(self):
        """备份文件
        """
        logging.info("开始备份文件...")

        for root, dirs, files in os.walk(self.source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                backup_file_path = self._get_backup_file_path(file_path)
                self._copy_file(file_path, backup_file_path)
        
        logging.info("文件备份完成。")

    def sync_files(self):
        """同步文件
        """
        logging.info("开始同步文件...")

        for root, dirs, files in os.walk(self.source_dir):
            for file_name in files:
                file_path = os.path.join(root, file_name)
                backup_file_path = self._get_backup_file_path(file_path)
                self._sync_file(file_path, backup_file_path)
        
        logging.info("文件同步完成。")

    def _get_backup_file_path(self, file_path):
        """获取备份文件路径
        """
        relative_path = os.path.relpath(file_path, self.source_dir)
        backup_file_path = os.path.join(self.backup_dir, relative_path)
        return backup_file_path

    def _copy_file(self, source_file_path, backup_file_path):
        """复制文件
        """
        try:
            shutil.copy2(source_file_path, backup_file_path)
            logging.info(f"文件 {source_file_path} 已备份到 {backup_file_path}")
        except Exception as e:
            logging.error(f"备份文件 {source_file_path} 失败：{str(e)}")

    def _sync_file(self, source_file_path, backup_file_path):
        """同步文件
        """
        try:
            if os.path.exists(backup_file_path):
                # 如果备份文件存在，则比较文件内容
                if not np.array_equal(np.fromfile(source_file_path, dtype=np.uint8), np.fromfile(backup_file_path, dtype=np.uint8)):
                    shutil.copy2(source_file_path, backup_file_path)
                    logging.info(f"文件 {source_file_path} 已同步到 {backup_file_path}")
                else:
                    logging.info(f"文件 {source_file_path} 已最新，无需同步")
            else:
                # 如果备份文件不存在，则复制文件
                shutil.copy2(source_file_path, backup_file_path)
                logging.info(f"文件 {source_file_path} 已同步到 {backup_file_path}")
        except Exception as e:
            logging.error(f"同步文件 {source_file_path} 失败：{str(e)}")

if __name__ == '__main__':
    # 设置源目录和备份目录
    source_dir = "/path/to/source/directory"
    backup_dir = "/path/to/backup/directory"

    # 创建文件备份和同步工具实例
    backup_sync_tool = FileBackupSync(source_dir, backup_dir)

    # 备份文件
    backup_sync_tool.backup_files()

    # 同步文件
    backup_sync_tool.sync_files()