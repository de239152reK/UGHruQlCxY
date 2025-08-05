# 代码生成时间: 2025-08-06 04:48:36
import numpy as np

"""
This module provides a simple user authentication system using Python and NumPy.
It includes the necessary functions to verify user credentials."""

class AuthenticationError(Exception):
    """Custom exception for authentication errors."""
    pass

class UserAuth:
    """Class to handle user authentication."""
    def __init__(self, users):
        """Initialize the user authentication with a list of users.
        Each user is represented as a dictionary containing their credentials.
        """
        self.users = users

    def authenticate(self, username, password):
        """Authenticate a user with provided username and password.
        If authentication is successful, return the user's data;
        otherwise, raise an AuthenticationError.
        """
        for user in self.users:
            if user['username'] == username and user['password'] == password:
                return user
        raise AuthenticationError(f"Authentication failed for user: {username}")

    def check_credentials(self, username, password):
        """Check if the provided credentials match any user in the database."""
        try:
            authenticated_user = self.authenticate(username, password)
            return True, authenticated_user
        except AuthenticationError as e:
            return False, str(e)

# Example usage
if __name__ == '__main__':
    # Sample user database
    users_db = [
        {'username': 'user1', 'password': 'password1'},
        {'username': 'admin', 'password': 'adminpass'}
    ]

    # Initialize authentication system
    auth_system = UserAuth(users_db)

    # Attempt to authenticate a user
    username_input = 'user1'
    password_input = 'password1'

    # Check credentials
    success, result = auth_system.check_credentials(username_input, password_input)
    if success:
        print(f"User authenticated successfully: {result['username']}")
    else:
        print(f"Authentication failed: {result}")