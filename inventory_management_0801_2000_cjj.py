# 代码生成时间: 2025-08-01 20:00:28
import numpy as np

"""
Inventory Management System
# 改进用户体验

A simple inventory management system using Python and NumPy for storing and
# 优化算法效率
managing inventory data.

Features:
- Add items to inventory
- Remove items from inventory
- Update item quantities
- Display inventory items
# 添加错误处理
- Handle errors and edge cases

Usage:
- Create an instance of InventoryManager
- Use the provided methods to manage inventory
# 优化算法效率
"""

class InventoryManager:
    """Manage inventory items and their quantities."""
    def __init__(self):
        # Initialize the inventory as a NumPy array with item names and quantities
        self.inventory = np.array([['Item1', 10], ['Item2', 20], ['Item3', 30]], dtype=object)

    def add_item(self, item_name, quantity):
        """Add an item to the inventory with the specified quantity."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
# 扩展功能模块
        # Check if the item already exists in the inventory
        if self._item_exists(item_name):
            self._update_quantity(item_name, quantity)
        else:
            self.inventory = np.append(self.inventory, [[item_name, quantity]], axis=0)

    def remove_item(self, item_name):
# FIXME: 处理边界情况
        """Remove an item from the inventory."""
# FIXME: 处理边界情况
        # Check if the item exists in the inventory
        if not self._item_exists(item_name):
            raise ValueError("Item not found in inventory")
        self.inventory = self.inventory[~(self.inventory[:, 0] == item_name)]
# 添加错误处理

    def update_quantity(self, item_name, quantity):
        """Update the quantity of an existing item in the inventory."""
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")
        if not self._item_exists(item_name):
            raise ValueError("Item not found in inventory")
        self._update_quantity(item_name, quantity)

    def display_inventory(self):
        """Display all items and their quantities in the inventory."""
# 添加错误处理
        print("Inventory Items:")
        for row in self.inventory:
            print(f"Item: {row[0]}, Quantity: {row[1]}")

    def _item_exists(self, item_name):
        """Check if an item exists in the inventory."""
        return np.any(self.inventory[:, 0] == item_name)
# FIXME: 处理边界情况

    def _update_quantity(self, item_name, quantity):
        """Update the quantity of an existing item."""
        index = np.where(self.inventory[:, 0] == item_name)[0][0]
# 扩展功能模块
        self.inventory[index, 1] = quantity
# FIXME: 处理边界情况

# Example usage
if __name__ == '__main__':
# 改进用户体验
    inventory_manager = InventoryManager()
    inventory_manager.add_item('Item4', 40)
    inventory_manager.update_quantity('Item2', 25)
    inventory_manager.remove_item('Item3')
    inventory_manager.display_inventory()
# 添加错误处理
