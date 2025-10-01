# 代码生成时间: 2025-10-01 22:36:49
import numpy as np

"""
Content Management System Demo using Python and NumPy framework.
This simple system allows for adding, retrieving, and deleting content items.
"""

class ContentItem:
    """Represents a single content item in the system."""

    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content

    def __str__(self):
        return f"ContentItem(id={self.id}, title='{self.title}')"


class ContentManagementSystem:
    """Manages a collection of content items."""

    def __init__(self):
        self.items = {}
        self.next_id = 1

    def add_item(self, title, content):
        """Adds a new content item to the system."""
        item_id = self.next_id
        self.next_id += 1
        self.items[item_id] = ContentItem(item_id, title, content)
        return item_id

    def get_item(self, item_id):
        """Retrieves a content item by its ID."""
        if item_id in self.items:
            return self.items[item_id]
        else:
            raise ValueError(f"No item with ID {item_id} found.")

    def delete_item(self, item_id):
        """Deletes a content item by its ID."""
        if item_id in self.items:
            del self.items[item_id]
        else:
            raise ValueError(f"No item with ID {item_id} found.")

    def list_items(self):
        """Lists all content items in the system."""
        for item in self.items.values():
            print(item)

# Example usage
if __name__ == '__main__':
    cms = ContentManagementSystem()
    try:
        item1_id = cms.add_item("Python Basics", "Learn the basics of Python programming.")
        item2_id = cms.add_item("NumPy Tutorial", "A comprehensive guide to NumPy.")
        cms.list_items()
        print(cms.get_item(item1_id))
        cms.delete_item(item2_id)
        cms.list_items()
    except ValueError as e:
        print(e)