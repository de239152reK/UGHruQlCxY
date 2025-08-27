# 代码生成时间: 2025-08-27 10:02:39
import os
import numpy as np
from PIL import Image
from glob import glob
from typing import Tuple

"""
Image Size Adjuster

This program is designed to adjust the size of multiple images in a directory.
It uses the PIL library to open and modify images, and NumPy to perform
operations on image arrays.
"""

class ImageSizeAdjuster:
    def __init__(self, source_dir: str, target_dir: str, new_size: Tuple[int, int]):
        self.source_dir = source_dir
        self.target_dir = target_dir
        self.new_size = new_size
        self.images = self._load_images()

    def _load_images(self) -> list:
        """
        Load all images from the source directory.
        Returns a list of image paths.
        """
        try:
            image_paths = glob(os.path.join(self.source_dir, "*.*"))
            return image_paths
        except Exception as e:
            print(f"Failed to load images: {e}")
            return []

    def adjust_sizes(self) -> None:
        """
        Adjust the size of each image to the new size specified during initialization.
        Saves the adjusted images to the target directory.
        """
        for image_path in self.images:
            try:
                with Image.open(image_path) as img:
                    # Convert the image to RGB
                    img = img.convert('RGB')
                    # Resize the image using the new size
                    img_resized = img.resize(self.new_size)
                    # Save the resized image to the target directory
                    filename = os.path.basename(image_path)
                    target_path = os.path.join(self.target_dir, filename)
                    img_resized.save(target_path)
                print(f"Adjusted image saved to {target_path}")
            except Exception as e:
                print(f"Failed to adjust image {image_path}: {e}")

    def run(self) -> None:
        """
        Run the image size adjustment process.
        """
        print("Starting image size adjustment process...")
        self.adjust_sizes()
        print("Image size adjustment process complete.")

# Example usage
if __name__ == '__main__':
    source_directory = "path/to/source/images"
    target_directory = "path/to/target/images"
    new_image_size = (800, 600)  # Width x Height

    adjuster = ImageSizeAdjuster(source_directory, target_directory, new_image_size)
    adjuster.run()
