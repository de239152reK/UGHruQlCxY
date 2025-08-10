# 代码生成时间: 2025-08-11 05:52:22
import numpy as np
import os
import json
from docx import Document

"""
A simple document format converter that reads a .docx file and converts it to JSON format.
"""

class DocumentConverter:
    def __init__(self, input_path, output_path):
        """
        Initialize the DocumentConverter with input and output file paths.
        :param input_path: Path to the input .docx file.
        :param output_path: Path to the output .json file.
        """
        self.input_path = input_path
        self.output_path = output_path

    def read_docx(self):
        """
        Reads the content of the input .docx file and returns it as a list of paragraphs.
        :return: A list of paragraphs.
        :raises FileNotFoundError: If the input file does not exist.
        """
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"The file {self.input_path} does not exist.")

        document = Document(self.input_path)
        paragraphs = [p.text for p in document.paragraphs]
        return paragraphs

    def convert_to_json(self, paragraphs):
        """
        Converts the list of paragraphs to a JSON format.
        :param paragraphs: List of paragraphs to be converted.
        :return: A JSON string.
        """
        json_data = json.dumps(paragraphs, ensure_ascii=False, indent=4)
        return json_data

    def write_to_file(self, json_data):
        """
        Writes the JSON data to the output file.
        :param json_data: JSON string to be written.
        :raises IOError: If there is an issue writing to the file.
        """
        try:
            with open(self.output_path, 'w', encoding='utf-8') as f:
                f.write(json_data)
        except IOError as e:
            raise IOError(f"Failed to write to the file {self.output_path}: {e}")

    def convert_document(self):
        """
        Main method to convert the .docx file to a JSON file.
        """
        try:
            paragraphs = self.read_docx()
            json_data = self.convert_to_json(paragraphs)
            self.write_to_file(json_data)
            print(f"Document successfully converted to {self.output_path}")
        except Exception as e:
            print(f"An error occurred: {e}")

# Example usage:
# converter = DocumentConverter('input.docx', 'output.json')
# converter.convert_document()
