# 代码生成时间: 2025-08-14 14:42:53
import numpy as np

"""
Order Processing System

This module demonstrates a simple order processing system using Python and NumPy.
It showcases clear code structure, error handling, comments, and best practices for maintainability and scalability."""

class OrderProcessingError(Exception):
    """Custom exception class for order processing errors."""
    pass

class Order:
    """Class representing an order."""
    def __init__(self, order_id, customer_id, items):
        """Initialize an order with an ID, customer ID, and items."""
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items  # List of tuples (item_id, quantity)

    def validate(self):
        """Validate the order's contents."""
        if not self.items:
            raise OrderProcessingError("Order must contain at least one item.")
        for item, quantity in self.items:
            if quantity <= 0:
                raise OrderProcessingError(f"Invalid quantity for item {item}: {quantity}.")

    def calculate_total(self):
        """Calculate the total cost of the order."""
        total = 0
        for item, quantity in self.items:
            # Assume item prices are stored in a NumPy array for simplicity
            price = np.array([10, 20, 30])[item]  # Replace with actual item prices
            total += price * quantity
        return total

class OrderProcessor:
    """Class responsible for processing orders."""
    def __init__(self):
        """Initialize the order processor."""
        pass

    def process_order(self, order):
        """Process an order."""
        try:
            order.validate()
            total = order.calculate_total()
            print(f"Order {order.order_id} processed successfully. Total cost: ${total}")
        except OrderProcessingError as e:
            print(f"Error processing order {order.order_id}: {e}")

# Example usage
if __name__ == "__main__":
    order_items = [(0, 1), (1, 2), (2, 1)]  # (item_id, quantity)
    order = Order(1, 1, order_items)
    processor = OrderProcessor()
    processor.process_order(order)