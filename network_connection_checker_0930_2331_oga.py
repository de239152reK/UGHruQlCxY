# 代码生成时间: 2025-09-30 23:31:47
import numpy as np
import socket
import time
from urllib.parse import urlparse

"""
A network connection checker using Python and NumPy.
This script can check the connection status to a given URL or hostname.
"""

class NetworkConnectionChecker:
    def __init__(self, target, timeout=5):
        """
        Initialize the NetworkConnectionChecker class.
        :param target: A string representing the target URL or hostname.
        :param timeout: An integer representing the timeout in seconds.
        """
        self.target = target
        self.timeout = timeout

    def check_connection(self):
        """
        Check the connection status to the target.
        :return: A boolean indicating whether the connection is successful.
        """
        try:
            # Parse the URL to get the hostname
            host = urlparse(self.target).netloc if self.target.startswith('http') else self.target
            # Use socket to check the connection
            socket.create_connection((host, 80), self.timeout)
            print(f"Connection to {self.target} is successful.")
            return True
        except OSError as e:
            print(f"Failed to connect to {self.target}: {e}")
            return False
        except Exception as e:
            print(f"An error occurred: {e}")
            return False

    def check_connection_with_retries(self, retries=3):
        """
        Check the connection status with retries.
        :param retries: An integer representing the number of retries.
        :return: A boolean indicating whether the connection is successful after retries.
        """
        for attempt in range(retries + 1):
            if self.check_connection():
                return True
            else:
                time.sleep(1)  # Wait for 1 second between retries
        return False

# Example usage
if __name__ == '__main__':
    # Create an instance of NetworkConnectionChecker
    checker = NetworkConnectionChecker('www.google.com')
    # Check the connection status
    if checker.check_connection_with_retries():
        print('The connection is stable.')
    else:
        print('The connection is unstable.')