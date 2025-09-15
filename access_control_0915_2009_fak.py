# 代码生成时间: 2025-09-15 20:09:59
import numpy as np

"""
访问权限控制程序

该程序使用NumPy框架提供了一个简单的访问权限控制系统，
允许管理员分配不同的权限给不同的用户。
"""

class AccessControl:
    def __init__(self):
        """初始化访问控制字典"""
        self.permissions = {}

    def add_user(self, username):
        """添加新用户

        :param username: 用户名
        """
        if username in self.permissions:
            raise ValueError("用户已存在")
        self.permissions[username] = set()

    def remove_user(self, username):
        """移除用户

        :param username: 用户名
        """
        if username not in self.permissions:
            raise ValueError("用户不存在")
        del self.permissions[username]

    def assign_permission(self, username, permission):
        """为用户分配权限

        :param username: 用户名
        :param permission: 权限
        """
        if username not in self.permissions:
            raise ValueError("用户不存在")
        self.permissions[username].add(permission)

    def revoke_permission(self, username, permission):
        """撤销用户的权限

        :param username: 用户名
        :param permission: 权限
        """
        if username not in self.permissions:
            raise ValueError("用户不存在\)
        if permission not in self.permissions[username]:
            raise ValueError("用户没有此权限\)
        self.permissions[username].remove(permission)

    def check_permission(self, username, permission):
        """检查用户是否有某权限

        :param username: 用户名
        :param permission: 权限
        :return: 布尔值
        """
        if username not in self.permissions:
            raise ValueError("用户不存在\)
        return permission in self.permissions[username]

    def list_permissions(self, username):
        """列出用户的权限

        :param username: 用户名
        :return: 用户的权限列表
        """
        if username not in self.permissions:
            raise ValueError("用户不存在\)
        return list(self.permissions[username])


# 示例用法
if __name__ == '__main__':
    ac = AccessControl()
    try:
        ac.add_user('admin')
        ac.assign_permission('admin', 'read')
        ac.assign_permission('admin', 'write')
        print(ac.check_permission('admin', 'read'))  # True
        print(ac.check_permission('admin', 'delete'))  # False
        ac.revoke_permission('admin', 'write')
        print(ac.check_permission('admin', 'write'))  # False
        print(ac.list_permissions('admin'))  # ['read']
    except ValueError as e:
        print(e)