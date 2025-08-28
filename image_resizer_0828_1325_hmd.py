# 代码生成时间: 2025-08-28 13:25:15
import os
import numpy as np
from PIL import Image

"""
Image Resizer - A tool to batch resize images.

This script takes images from a specified directory, resizes them to a given dimension,
and saves them to a new directory.

Attributes:
# 增强安全性
    source_dir (str): The directory containing the original images.
# 扩展功能模块
    target_dir (str): The directory where the resized images will be saved.
    target_size (tuple): The desired size for the resized images.

Methods:
    resize_images(): Resizes images in the source directory and saves them to the target directory.
# 优化算法效率
"""
# 改进用户体验

class ImageResizer:
# TODO: 优化性能
    def __init__(self, source_dir, target_dir, target_size):
        self.source_dir = source_dir
# 优化算法效率
        self.target_dir = target_dir
        self.target_size = target_size

    def resize_image(self, image_path):
        """
        Resize a single image.

        Args:
            image_path (str): The path to the image file.

        Returns:
# TODO: 优化性能
            PIL.Image: The resized image.
# 增强安全性
        """
# NOTE: 重要实现细节
        try:
            with Image.open(image_path) as img:
                # Resize the image
                resized_img = img.resize(self.target_size, Image.ANTIALIAS)
# NOTE: 重要实现细节
                return resized_img
# 添加错误处理
        except IOError as e:
            print(f"Error opening or resizing image {image_path}: {e}")
            return None

    def save_resized_image(self, resized_img, target_path):
        """
        Save the resized image to the target directory.
# 添加错误处理

        Args:
            resized_img (PIL.Image): The resized image to save.
# 改进用户体验
            target_path (str): The path where the resized image will be saved.
        """
        try:
            resized_img.save(target_path)
        except IOError as e:
            print(f"Error saving resized image to {target_path}: {e}")

    def resize_images(self):
        """
        Resize all images in the source directory and save them to the target directory.
        """
        if not os.path.exists(self.target_dir):
            os.makedirs(self.target_dir)
# 添加错误处理

        for filename in os.listdir(self.source_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
                file_path = os.path.join(self.source_dir, filename)
                target_path = os.path.join(self.target_dir, filename)

                # Resize the image
                resized_img = self.resize_image(file_path)
                if resized_img:
                    # Save the resized image
                    self.save_resized_image(resized_img, target_path)

# Example usage
if __name__ == '__main__':
    source_dir = 'path/to/source/directory'
    target_dir = 'path/to/target/directory'
    target_size = (800, 600)  # Desired size for the resized images

    resizer = ImageResizer(source_dir, target_dir, target_size)
    resizer.resize_images()