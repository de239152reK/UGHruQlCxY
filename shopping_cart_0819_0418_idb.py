# 代码生成时间: 2025-08-19 04:18:47
import numpy as np

"""
Shopping Cart Implementation using Python and NumPy
"""

# Define a Product class to represent individual products
class Product:
    def __init__(self, name, price):
        self.name = name  # String, product name
        self.price = price  # Float, product price

    def __str__(self):
        return f"Product Name: {self.name}, Price: ${self.price}"


# Define a ShoppingCart class to manage the shopping cart
class ShoppingCart:
    def __init__(self):
        self.items = []  # List of Product objects

    # Add a product to the cart
    def add_product(self, product):
        if not isinstance(product, Product):
            raise ValueError("Only Product instances can be added to the cart.")
        self.items.append(product)
        print(f"Added {product.name} to the cart.")

    # Remove a product from the cart
    def remove_product(self, product_name):
        for product in self.items:
            if product.name == product_name:
                self.items.remove(product)
                print(f"Removed {product_name} from the cart.")
                return
        raise ValueError(f"Product {product_name} not found in the cart.")

    # Get the total price of the cart
    def get_total_price(self):
        total = sum(item.price for item in self.items)
        return total

    # Display the cart contents
    def display_cart(self):
        if not self.items:
            print("Your cart is empty.")
        else:
            print("Cart Contents:")
            for item in self.items:
                print(item)

# Example usage
if __name__ == "__main__":
    # Create some products
    product1 = Product("Apple", 0.5)
    product2 = Product("Banana", 0.3)
    product3 = Product("Orange", 0.4)

    # Create a shopping cart and add products
    cart = ShoppingCart()
    cart.add_product(product1)
    cart.add_product(product2)
    cart.add_product(product3)

    # Display the cart
    cart.display_cart()

    # Remove a product
    cart.remove_product("Banana")

    # Display the cart again
    cart.display_cart()

    # Get the total price
    total = cart.get_total_price()
    print(f"Total Price: ${total}")