# 代码生成时间: 2025-08-09 14:33:31
import numpy as np

"""
User Authentication module
This module provides a simple user authentication mechanism using
Numpy for storing and validating credentials.
"""

# Define a class for User Authentication
class UserAuthentication:
    def __init__(self):
        # Initialize an empty dictionary to store user credentials
        self.credentials = {}

    def add_user(self, username, password):
        """
        Add a new user with given username and password.
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        Raises:
            ValueError: If the username already exists.
        """
        if username in self.credentials:
            raise ValueError("Username already exists.")
        self.credentials[username] = password

    def authenticate_user(self, username, password):
        """
        Authenticate a user with given username and password.
        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        # Check if the username exists and the password matches
        return self.credentials.get(username) == password

    def get_user_list(self):
        """
        Get a list of all registered usernames.
        Returns:
            list: A list of usernames.
        """
        return list(self.credentials.keys())

# Example usage
if __name__ == '__main__':
    auth_system = UserAuthentication()
    try:
        auth_system.add_user("alice", "password123")
        auth_system.add_user("bob", "securepass")
        
        # Attempt to add a duplicate user
        auth_system.add_user("alice", "anotherpass")
    except ValueError as e:
        print(e)
    
    print("Authentication successful: ", auth_system.authenticate_user("alice", "password123"))
    print("Authentication successful: ", auth_system.authenticate_user("bob", "wrongpass"))
    print("User list: ", auth_system.get_user_list())