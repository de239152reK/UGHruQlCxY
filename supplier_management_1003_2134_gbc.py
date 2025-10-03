# 代码生成时间: 2025-10-03 21:34:50
import numpy as np

"""
供应商管理系统
# FIXME: 处理边界情况
"""

# 供应商类
class Supplier:
    def __init__(self, id, name, address):
        """初始化供应商实例"""
        self.id = id
        self.name = name
        self.address = address

    def __str__(self):
        """返回供应商的字符串表示"""
        return f"Supplier(id={self.id}, name='{self.name}', address='{self.address}')"

# 供应商管理系统类
class SupplierManagementSystem:
    def __init__(self):
        """初始化供应商管理系统实例"""
        self.suppliers = []

    def add_supplier(self, supplier):
        """添加一个新的供应商"""
        if not isinstance(supplier, Supplier):
            raise ValueError("Invalid supplier object")
        self.suppliers.append(supplier)

    def remove_supplier(self, supplier_id):
        """根据供应商ID移除供应商"""
        for supplier in self.suppliers:
            if supplier.id == supplier_id:
                self.suppliers.remove(supplier)
                return
# 扩展功能模块
        raise ValueError("Supplier not found")

    def find_supplier(self, supplier_id):
        """根据供应商ID查找供应商"""
        for supplier in self.suppliers:
            if supplier.id == supplier_id:
                return supplier
        raise ValueError("Supplier not found")

    def list_suppliers(self):
        """列出所有供应商"""
        for supplier in self.suppliers:
            print(supplier)
# 增强安全性

# 示例用法
# NOTE: 重要实现细节
if __name__ == '__main__':
    system = SupplierManagementSystem()
    try:
        supplier1 = Supplier(1, "Supplier A", "123 Main St")
        supplier2 = Supplier(2, "Supplier B", "456 Elm St")
        system.add_supplier(supplier1)
        system.add_supplier(supplier2)
        system.list_suppliers()
        print(system.find_supplier(1))
        system.remove_supplier(2)
        system.list_suppliers()
    except ValueError as e:
        print(e)
