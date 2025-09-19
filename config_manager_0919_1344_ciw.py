# 代码生成时间: 2025-09-19 13:44:33
import json
import numpy as np
import os

"""
Config Manager is a utility class for managing configuration files.
It provides methods to load, save, and update configuration settings.
"""
class ConfigManager:
    def __init__(self, config_file):
        """
        Initialize the ConfigManager with a configuration file path.
        :param config_file: Path to the configuration file.
        """
        self.config_file = config_file
        self.config_data = {}

    def load_config(self):
        """
        Load the configuration from the file.
        If the file does not exist, create it with default settings.
        """
        if not os.path.exists(self.config_file):
            self.save_config()
            print(f"Config file {self.config_file} created with default settings.")
        else:
            try:
                with open(self.config_file, 'r') as file:
                    self.config_data = json.load(file)
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format in config file.")
            except Exception as e:
                raise IOError(f"Failed to load config file: {e}")

    def save_config(self):
        """
        Save the current configuration to the file.
        """
        try:
            with open(self.config_file, 'w') as file:
                json.dump(self.config_data, file, indent=4)
        except Exception as e:
            raise IOError(f"Failed to save config file: {e}")

    def update_config(self, key, value):
        """
        Update a configuration setting.
        :param key: Configuration key.
        :param value: New value for the key.
        """
        self.config_data[key] = value
        self.save_config()

    def get_config(self, key):
        """
        Retrieve a configuration value by key.
        :param key: Configuration key.
        :return: Value associated with the key.
        """
        return self.config_data.get(key)

# Example usage
if __name__ == '__main__':
    config_path = 'config.json'
    manager = ConfigManager(config_path)
    manager.load_config()
    print(manager.get_config('example_key'))  # Get a config value
    manager.update_config('example_key', 'example_value')  # Update a config value
