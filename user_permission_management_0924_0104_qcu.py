# 代码生成时间: 2025-09-24 01:04:34
import numpy as np

"""
User Permission Management System
A simple program to manage user permissions using Python and NumPy.
"""

class Permission:
    """
    Represents a single permission.
    """
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Permission {self.name}>"]n


class User:
    """
    Represents a user with a set of permissions.
    """
    def __init__(self, username):
        self.username = username
        self.permissions = set()

    def add_permission(self, permission):
        """
        Adds a permission to the user.
        """
        if not isinstance(permission, Permission):
            raise ValueError("Permission must be an instance of Permission")
        self.permissions.add(permission)

    def remove_permission(self, permission):
        """
        Removes a permission from the user.
        """
        if permission not in self.permissions:
            raise ValueError("Permission not found")
        self.permissions.remove(permission)

    def has_permission(self, permission):
        """
        Checks if the user has a specific permission.
        """
        return permission in self.permissions

    def __repr__(self):
        return f"<User {self.username} with permissions: {[perm.name for perm in self.permissions]}>"


def main():
    """
    Main function to demonstrate the user permission management system.
    """
    # Create permissions
    read_permission = Permission("read")
    write_permission = Permission("write")

    # Create users
    alice = User("Alice")
    bob = User("Bob")

    # Assign permissions
    alice.add_permission(read_permission)
    bob.add_permission(read_permission)
    bob.add_permission(write_permission)

    # Check permissions
    print(alice.has_permission(write_permission))  # False
    print(bob.has_permission(write_permission))  # True

    # Remove permission
    bob.remove_permission(read_permission)
    print(bob.has_permission(read_permission))  # False

if __name__ == "__main__":
    main()
