# 代码生成时间: 2025-08-10 02:29:53
import numpy as np
# FIXME: 处理边界情况
from PIL import Image
import os
import glob
def resize_images(source_folder, target_folder, target_size):
    # 确保目标文件夹存在，如果不存在则创建
# 增强安全性
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
# 扩展功能模块

    # 遍历源文件夹下的所有图片文件
    for image_path in glob.glob(os.path.join(source_folder, "*")):
        try:
            # 打开图片
            with Image.open(image_path) as img:
                # 调整图片尺寸
                img_resized = img.resize(target_size, Image.ANTIALIAS)
# TODO: 优化性能

                # 获取文件名
# NOTE: 重要实现细节
                filename = os.path.basename(image_path)
                # 保存调整后的图片到目标文件夹
                img_resized.save(os.path.join(target_folder, filename))
        except IOError as e:
            print(f"Error resizing {image_path}: {e}")

def main():
# 扩展功能模块
    # 源文件夹和目标文件夹的路径
# 改进用户体验
    source_folder = "path_to_source_folder"
    target_folder = "path_to_target_folder"
    # 目标尺寸
    target_size = (300, 300)
# TODO: 优化性能

    # 调用resize_images函数
    resize_images(source_folder, target_folder, target_size)

if __name__ == "__main__":
    main()

"""
图片尺寸批量调整器
这个程序可以批量调整文件夹内所有图片的尺寸。

参数:
source_folder (str): 源文件夹路径，包含需要调整尺寸的图片。
target_folder (str): 目标文件夹路径，调整尺寸后的图片将保存在这里。
target_size (tuple): 目标尺寸，格式为(width, height)。
"""