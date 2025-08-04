# 代码生成时间: 2025-08-04 13:14:03
import numpy as np
import re
import json

"""
Log Parser Tool

This tool is designed to parse log files and extract relevant information.
It is built using Python and NumPy, ensuring efficient and scalable log processing.
"""

class LogParser:
    """
    A class to parse log files and extract relevant information.
    """
    def __init__(self, file_path):
        """
        Initializes the LogParser class.
        
        Args:
            file_path (str): The path to the log file to be parsed.
        """
        self.file_path = file_path
        self.log_data = []

    def parse_log(self):
        """
        Parses the log file and extracts relevant information.
        
        Returns:
            list: A list of dictionaries containing the extracted log data.
        """
        try:
            with open(self.file_path, 'r') as file:
                for line in file:
                    # Assuming the log format is 'timestamp - log level - message'
                    timestamp, log_level, message = line.strip().split(' - ')
                    self.log_data.append({
                        'timestamp': timestamp,
                        'log_level': log_level,
                        'message': message
                    })
        except FileNotFoundError:
            print(f"Error: The file {self.file_path} does not exist.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")

        return self.log_data

    def filter_logs(self, log_level):
        """
        Filters the parsed log data based on the log level.
        
        Args:
            log_level (str): The log level to filter by.
        
        Returns:
            list: A list of dictionaries containing the filtered log data.
        """
        return [log for log in self.log_data if log['log_level'] == log_level]

    def save_to_json(self, output_file):
        """
        Saves the parsed log data to a JSON file.
        
        Args:
            output_file (str): The path to the output JSON file.
        """
        try:
            with open(output_file, 'w') as file:
                json.dump(self.log_data, file, indent=4)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

# Example usage
if __name__ == '__main__':
    log_parser = LogParser('example.log')
    log_data = log_parser.parse_log()
    print(log_data)

    filtered_logs = log_parser.filter_logs('ERROR')
    print(filtered_logs)

    log_parser.save_to_json('parsed_logs.json')