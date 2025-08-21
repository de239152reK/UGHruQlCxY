# 代码生成时间: 2025-08-22 06:48:44
import os
import numpy as np
from PIL import Image

"""
Image Resizer is a Python program designed to batch resize images to a specified size.

This program utilizes the PIL library for image manipulation and the numpy library for numerical operations.
It is designed to be easy to understand, maintainable, and scalable.
"""

class ImageResizer:
    """A class to handle batch resizing of images."""

    def __init__(self, source_folder, target_folder, output_size):
        """Initialize the ImageResizer with source and target folders and output size."""
        self.source_folder = source_folder
        self.target_folder = target_folder
        self.output_size = output_size

    def resize_images(self):
        """Resize all images in the source folder to the specified output size."""
        if not os.path.exists(self.target_folder):
            os.makedirs(self.target_folder)

        for filename in os.listdir(self.source_folder):
            file_path = os.path.join(self.source_folder, filename)
            try:
                if os.path.isfile(file_path):
                    self.resize_image(file_path)
            except Exception as e:
                print(f"Error resizing {filename}: {e}")

    def resize_image(self, image_path):
        """Resize a single image and save it to the target folder."""
        with Image.open(image_path) as img:
            resized_img = img.resize(self.output_size, Image.ANTIALIAS)
            target_path = os.path.join(self.target_folder, os.path.basename(image_path))
            resized_img.save(target_path)
            print(f"Resized and saved {image_path} to {target_path}")

    def get_supported_extensions(self):
        """Return a set of supported image extensions."""
        return {'.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff'}

# Example usage:
if __name__ == '__main__':
    source_folder = 'path_to_source_folder'
    target_folder = 'path_to_target_folder'
    output_size = (800, 600)  # width, height

    resizer = ImageResizer(source_folder, target_folder, output_size)
    resizer.resize_images()
