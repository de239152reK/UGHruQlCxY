# 代码生成时间: 2025-09-08 21:30:46
import numpy as np

"""
Access Control System using Python and NumPy.
This module provides a simple access control system with user roles and permissions.
"""

class AccessControl:
    def __init__(self):
        """Initialize the access control system."""
        self.roles = {
            'admin': {'permissions': {'read': True, 'write': True, 'delete': True}},
            'user': {'permissions': {'read': True, 'write': False, 'delete': False}},
            'guest': {'permissions': {'read': False, 'write': False, 'delete': False}}
        }

    def add_user_role(self, user_id, role):
# FIXME: 处理边界情况
        """Add a user role to the system.
        Args:
# 改进用户体验
            user_id (str): The unique identifier for the user.
# FIXME: 处理边界情况
            role (str): The role to assign to the user.
        Raises:
            ValueError: If the role does not exist in the system."""
# FIXME: 处理边界情况
        if role not in self.roles:
# NOTE: 重要实现细节
            raise ValueError(f"Role '{role}' does not exist.")
        self.users = {user_id: role}

    def check_permission(self, user_id, permission):
# NOTE: 重要实现细节
        """Check if a user has a specific permission.
        Args:
            user_id (str): The unique identifier for the user.
# 改进用户体验
            permission (str): The permission to check.
        Returns:
# TODO: 优化性能
            bool: True if the user has the permission, False otherwise.
        Raises:
            ValueError: If the user does not exist in the system."""
        if user_id not in self.users:
            raise ValueError(f"User '{user_id}' does not exist.")
        user_role = self.users[user_id]
        return self.roles[user_role]['permissions'].get(permission, False)

    def remove_user_role(self, user_id):
        """Remove a user role from the system.
        Args:
            user_id (str): The unique identifier for the user."""
        if user_id in self.users:
            del self.users[user_id]
        else:
            print(f"User '{user_id}' does not exist.")

# Example usage
if __name__ == '__main__':
    ac = AccessControl()
    ac.add_user_role('user123', 'admin')
    try:
        print(ac.check_permission('user123', 'write'))  # Should return True
        print(ac.check_permission('user123', 'delete'))  # Should return True
# FIXME: 处理边界情况
    except ValueError as e:
        print(e)
    
    try:
        ac.remove_user_role('user123')
    except ValueError as e:
        print(e)