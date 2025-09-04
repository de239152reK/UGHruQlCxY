# 代码生成时间: 2025-09-04 08:52:54
import numpy as np
import os
import re
from collections import Counter
import string

"""
A text file analyzer that processes the content of a given text file
and provides various statistics and insights.
"""

class TextFileAnalyzer:
    def __init__(self, filepath):
        """
        Initialize the TextFileAnalyzer with a file path.
        :param filepath: Path to the text file to be analyzed.
        """
        self.filepath = filepath
        self.text_content = None

    def read_file(self):
        """
        Reads the content of the file into memory.
        :raises FileNotFoundError: If the file does not exist.
        """
        if not os.path.exists(self.filepath):
            raise FileNotFoundError("The file does not exist.")

        with open(self.filepath, 'r', encoding='utf-8') as file:
            self.text_content = file.read()

    def word_count(self):
        """
        Returns a Counter object with word frequencies.
        """
        if self.text_content is None:
            raise ValueError("File content has not been read. Call read_file() first.")

        # Remove punctuation and convert to lower case
        words = re.findall(r'\w+', self.text_content.lower())
        return Counter(words)

    def sentence_count(self):
        """
        Returns the number of sentences in the file.
        """
        if self.text_content is None:
            raise ValueError("File content has not been read. Call read_file() first.")

        # Split the text into sentences based on common sentence delimiters
        sentences = re.split(r'[.!?]+', self.text_content)
        return len([s for s in sentences if s.strip()])

    def character_count(self):
        """
        Returns a Counter object with character frequencies.
        """
        if self.text_content is None:
            raise ValueError("File content has not been read. Call read_file() first.")

        # Count all characters including spaces and punctuation
        return Counter(self.text_content)

    def analyze(self):
        """
        Performs a complete analysis of the text file and
        returns a dictionary with word, sentence, and character counts.
        """
        self.read_file()
        word_counts = self.word_count()
        sentence_count = self.sentence_count()
        char_counts = self.character_count()

        return {
            "word_counts": dict(word_counts),
            "sentence_count": sentence_count,
            "char_counts": dict(char_counts)
        }

# Example usage
if __name__ == '__main__':
    filepath = 'example.txt'  # Replace with the path to your text file
    analyzer = TextFileAnalyzer(filepath)
    try:
        analysis_results = analyzer.analyze()
        print("Word Counts: ", analysis_results['word_counts'])
        print("Sentence Count: ", analysis_results['sentence_count'])
        print("Character Counts: ", analysis_results['char_counts'])
    except Exception as e:
        print("An error occurred: ", str(e))