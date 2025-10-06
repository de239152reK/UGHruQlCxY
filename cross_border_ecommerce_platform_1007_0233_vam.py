# 代码生成时间: 2025-10-07 02:33:30
import numpy as np

"""
Cross Border ECommerce Platform

This module implements a simple cross-border e-commerce platform using Python and Numpy framework.
It allows for product listing, customer registration, and order management.

Attributes:
    - products (dict): A dictionary to store product information.
    - customers (dict): A dictionary to store customer information.
    - orders (list): A list to store order information.

Methods:
    - add_product: Adds a new product to the product list.
    - register_customer: Registers a new customer.
    - place_order: Places an order for a customer.
    - get_product: Retrieves product information.
    - get_customer: Retrieves customer information.
    - get_order: Retrieves order information.

Example:
    >>> platform = CrossBorderECommercePlatform()
    >>> platform.add_product('Product1', 'Description', 100)
    >>> platform.register_customer('Customer1', 'customer1@example.com')
    >>> platform.place_order('Customer1', 'Product1', 1)
    >>> print(platform.get_product('Product1'))
    >>> print(platform.get_customer('Customer1'))
    >>> print(platform.get_order(0))
"""

class CrossBorderECommercePlatform:
    def __init__(self):
        """Initializes the cross-border e-commerce platform."""
        self.products = {}  # Product dictionary
        self.customers = {}  # Customer dictionary
        self.orders = []  # Order list

    def add_product(self, product_name, description, price):
        """Adds a new product to the product list."""
        if product_name in self.products:
            raise ValueError(f"Product '{product_name}' already exists.")
        self.products[product_name] = {'description': description, 'price': price}

    def register_customer(self, customer_name, email):
        """Registers a new customer."""
        if customer_name in self.customers:
            raise ValueError(f"Customer '{customer_name}' already exists.")
        self.customers[customer_name] = {'email': email}

    def place_order(self, customer_name, product_name, quantity):
        """Places an order for a customer."""
        if customer_name not in self.customers:
            raise ValueError(f"Customer '{customer_name}' does not exist.")
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist.")
        order = {
            'customer_name': customer_name,
            'product_name': product_name,
            'quantity': quantity,
            'price': self.products[product_name]['price'] * quantity
        }
        self.orders.append(order)

    def get_product(self, product_name):
        """Retrieves product information."""
        if product_name not in self.products:
            raise ValueError(f"Product '{product_name}' does not exist.")
        return self.products[product_name]

    def get_customer(self, customer_name):
        """Retrieves customer information."""
        if customer_name not in self.customers:
            raise ValueError(f"Customer '{customer_name}' does not exist.")
        return self.customers[customer_name]

    def get_order(self, order_index):
        """Retrieves order information."""
        if order_index < 0 or order_index >= len(self.orders):
            raise ValueError(f"Order index {order_index} is out of range.")
        return self.orders[order_index]

# Example usage
if __name__ == '__main__':
    platform = CrossBorderECommercePlatform()
    platform.add_product('Product1', 'Description', 100)
    platform.register_customer('Customer1', 'customer1@example.com')
    platform.place_order('Customer1', 'Product1', 1)
    print(platform.get_product('Product1'))
    print(platform.get_customer('Customer1'))
    print(platform.get_order(0))
