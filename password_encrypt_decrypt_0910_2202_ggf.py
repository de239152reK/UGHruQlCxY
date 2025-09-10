# 代码生成时间: 2025-09-10 22:02:14
import numpy as np
import os
from cryptography.fernet import Fernet

"""
Password Encryption and Decryption Tool
This module provides functionality to encrypt and decrypt passwords using the Fernet symmetric encryption algorithm from the cryptography library.
"""


# Define a class to handle password encryption and decryption
class PasswordTool:
    def __init__(self, key=None):
        """
        Initialize the PasswordTool with an optional key.
        If no key is provided, a new key will be generated.
        """
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.cipher = Fernet(self.key)

    def encrypt(self, password):
        """
        Encrypt the given password.
        Args:
            password (str): The password to be encrypted.
        Returns:
            str: The encrypted password.
        Raises:
            ValueError: If the password is None or empty.
        """
        if not password:
            raise ValueError("Password cannot be empty")
        return self.cipher.encrypt(password.encode()).decode()

    def decrypt(self, encrypted_password):
        """
        Decrypt the given encrypted password.
        Args:
            encrypted_password (str): The password to be decrypted.
        Returns:
            str: The decrypted password.
        Raises:
            ValueError: If the encrypted password is None or empty.
        """
        if not encrypted_password:
            raise ValueError("Encrypted password cannot be empty")
        return self.cipher.decrypt(encrypted_password.encode()).decode()

    def get_key(self):
        """
        Get the encryption key.
        Returns:
            str: The encryption key.
        """
        return self.key.decode()

# Example usage
if __name__ == '__main__':
    password_tool = PasswordTool()
    original_password = "my_secret_password"

    try:
        encrypted_password = password_tool.encrypt(original_password)
        print("Encrypted Password:", encrypted_password)

        decrypted_password = password_tool.decrypt(encrypted_password)
        print("Decrypted Password:", decrypted_password)
    except ValueError as e:
        print("Error: ", e)