# 代码生成时间: 2025-08-01 12:13:58
import numpy as np
import os

"""
Password Encryption and Decryption Tool

A simple tool to encrypt and decrypt passwords using numpy.
"""

# Function to generate a random key
def generate_key(length=8):
    """Generate a random key of specified length."""
    return os.urandom(length)

# Function to encrypt the password
def encrypt_password(password, key):
    """Encrypt the given password using the provided key."""
    if not password:
        raise ValueError("Password cannot be empty.")
    if not key:
        raise ValueError("Key cannot be empty.")
    
    # Convert password to numpy array of bytes
    password_array = np.frombuffer(password.encode('utf-8'), dtype=np.uint8)
    
    # Convert key to numpy array of bytes
    key_array = np.frombuffer(key, dtype=np.uint8)
    
    # Encrypt using XOR operation
    encrypted_array = np.bitwise_xor(password_array, key_array)
    
    # Return the encrypted array as bytes
    return encrypted_array.tobytes()

# Function to decrypt the password
def decrypt_password(encrypted_password, key):
    """Decrypt the given encrypted password using the provided key."""
    if not encrypted_password:
        raise ValueError("Encrypted password cannot be empty.")
    if not key:
        raise ValueError("Key cannot be empty.")
    
    # Convert encrypted password to numpy array of bytes
    encrypted_array = np.frombuffer(encrypted_password, dtype=np.uint8)
    
    # Convert key to numpy array of bytes
    key_array = np.frombuffer(key, dtype=np.uint8)
    
    # Decrypt using XOR operation
    decrypted_array = np.bitwise_xor(encrypted_array, key_array)
    
    # Return the decrypted array as a string
    return decrypted_array.tobytes().decode('utf-8')

# Example usage
if __name__ == "__main__":
    # Generate a random key
    key = generate_key()
    
    # Original password
    password = "my_secret_password"
    
    # Encrypt the password
    encrypted = encrypt_password(password, key)
    print("Encrypted: ", encrypted)
    
    # Decrypt the password
    decrypted = decrypt_password(encrypted, key)
    print("Decrypted: ", decrypted)