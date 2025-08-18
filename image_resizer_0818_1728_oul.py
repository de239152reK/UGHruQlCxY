# 代码生成时间: 2025-08-18 17:28:53
import os
import numpy as np
from PIL import Image

"""
图片尺寸批量调整器
这个程序可以批量调整指定文件夹内所有图片的尺寸。
"""

class ImageResizer:
    def __init__(self, input_dir, output_dir, target_size):
        """
        构造函数
        :param input_dir: 输入文件夹路径，包含待调整尺寸的图片
        :param output_dir: 输出文件夹路径，存储调整尺寸后的图片
        :param target_size: 目标尺寸，格式为(width, height)
        """
        self.input_dir = input_dir
        self.output_dir = output_dir
        self.target_size = target_size
        self.file_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

    def resize_images(self):
        """
        调整文件夹内所有图片的尺寸
        """
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        for filename in os.listdir(self.input_dir):
            if any(filename.lower().endswith(ext) for ext in self.file_extensions):
                try:
                    image_path = os.path.join(self.input_dir, filename)
                    image = Image.open(image_path)
                    resized_image = self.resize_image(image)
                    output_path = os.path.join(self.output_dir, filename)
                    resized_image.save(output_path)
                    print(f"{filename} resized successfully.")
                except Exception as e:
                    print(f"Error resizing {filename}: {e}")
            else:
                print(f"{filename} is not a supported image file format.")

    def resize_image(self, image):
        """
        调整单张图片的尺寸
        :param image: PIL Image对象
        :return: 调整尺寸后的PIL Image对象
        """
        return image.resize(self.target_size, Image.ANTIALIAS)

# 使用示例
if __name__ == '__main__':
    # 输入文件夹路径
    input_dir = 'input_images'
    # 输出文件夹路径
    output_dir = 'resized_images'
    # 目标尺寸
    target_size = (800, 600)
    
    resizer = ImageResizer(input_dir, output_dir, target_size)
    resizer.resize_images()