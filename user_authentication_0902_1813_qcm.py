# 代码生成时间: 2025-09-02 18:13:43
import numpy as np

"""
User Authentication program using Python and NumPy.
This program simulates a simple user authentication system.
"""

class UserAuthentication:
    def __init__(self):
        # Initialize an empty dictionary to store user credentials
        self.users = {}

    def add_user(self, username, password):
        """Add a new user to the system.

        Args:
            username (str): The username of the new user.
            password (str): The password of the new user.
        """
        if username in self.users:
            raise ValueError(f"User {username} already exists.")
        self.users[username] = password

    def authenticate_user(self, username, password):
        """Authenticate a user by their username and password.

        Args:
            username (str): The username to authenticate.
            password (str): The password to authenticate.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        user_password = self.users.get(username)
        if user_password and user_password == password:
            return True
        else:
            return False

    def list_users(self):
        """List all users in the system."""
        return list(self.users.keys())

# Example usage
def main():
    auth_system = UserAuthentication()
    try:
        auth_system.add_user("user1", "password123")
        auth_system.add_user("user2", "password456")

        print("User list:", auth_system.list_users())

        # Attempt to authenticate a user
        print("Authenticating user1...", auth_system.authenticate_user("user1", "password123"))
        print("Authenticating user1 with wrong password...", auth_system.authenticate_user("user1", "wrongpassword"))

    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()