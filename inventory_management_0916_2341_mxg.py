# 代码生成时间: 2025-09-16 23:41:06
import numpy as np

"""
Inventory Management System

This system allows for adding, removing, and querying items in an inventory.
It uses numpy for efficient numerical operations and data storage.
"""

class Inventory:
    def __init__(self):
        """Initialize the inventory with an empty numpy array."""
        self.items = np.array([], dtype=np.dtype({'names': ('id', 'name', 'quantity'), 'formats': ('i4', 'U20', 'i4')}))

    def add_item(self, item_id, item_name, quantity):
        """Add a new item to the inventory."""
        if self.get_item(item_id).size > 0:
            raise ValueError(f"Item with ID {item_id} already exists.")
        new_item = np.array([((item_id, item_name, quantity))], dtype=self.items.dtype)
        self.items = np.append(self.items, new_item)

    def remove_item(self, item_id):
        """Remove an item from the inventory by its ID."""
        self.items = np.delete(self.items, self.items['id'] == item_id)

    def update_quantity(self, item_id, quantity):
        """Update the quantity of an existing item."""
        index = np.where(self.items['id'] == item_id)[0]
        if index.size == 0:
            raise ValueError(f"Item with ID {item_id} not found.")
        self.items[index][0]['quantity'] = quantity

    def get_item(self, item_id):
        """Retrieve an item by its ID."""
        return self.items[self.items['id'] == item_id]

    def list_all_items(self):
        """List all items in the inventory."""
        return self.items

    def __str__(self):
        """String representation of the inventory."""
        return str(self.items)

# Example usage
if __name__ == '__main__':
    inventory = Inventory()
    try:
        inventory.add_item(1, "Widget", 10)
        inventory.add_item(2, "Gadget", 20)
        print(inventory.get_item(1))
        inventory.update_quantity(1, 15)
        print(inventory.get_item(1))
        inventory.remove_item(2)
        print(inventory.list_all_items())
    except ValueError as e:
        print(e)