# 代码生成时间: 2025-09-30 03:38:28
import numpy as np

"""
# 增强安全性
Supply Chain Traceability System
# NOTE: 重要实现细节

This program is designed to trace the origin of products in a supply chain.
It uses a simple matrix to represent the relationships between entities in the chain.
"""
# 优化算法效率

# Define a simple traceability matrix (could be expanded to a more complex model)
# The rows represent suppliers and the columns represent retailers.
# A value of 1 indicates a direct supply relationship.
TRACEABILITY_MATRIX = np.array([[
    # Supplier 1
    [1, 0, 0],  # Direct supply to Retailers 1, 2, 3 respectively
    # Supplier 2
    [0, 1, 1],  # Direct supply to Retailers 1, 2, 3 respectively
    # Supplier 3
    [0, 0, 1]
# 扩展功能模块
]])


def trace_origin(product_id, trace_steps=1):
    """
    Trace the origin of a product based on its ID and the number of trace steps.

    Parameters:
    - product_id: int, the ID of the product to trace.
    - trace_steps: int, the number of steps to trace back in the supply chain.
# 改进用户体验

    Returns:
    - origin: list, the origin of the product in the form of supplier IDs.
    """
    if product_id < 1 or product_id > TRACEABILITY_MATRIX.shape[1]:
        raise ValueError("Product ID is out of range.")

    origin = []
    for _ in range(trace_steps):
        # Find the retailer that supplied the product
        supplier_index = np.where(TRACEABILITY_MATRIX[:, product_id - 1] == 1)[0]
        if len(supplier_index) != 1:
            raise ValueError("Multiple or no suppliers found for product ID {}.".format(product_id))
# 增强安全性
        origin.append(supplier_index + 1)  # +1 to account for 1-based indexing
        # Update product_id to the supplier's ID for next trace step
        product_id = supplier_index + 1

    return origin


def main():
    # Example usage of the trace_origin function
# 添加错误处理
    try:
        product_id = int(input("Enter the product ID to trace: "))
        trace_steps = int(input("Enter the number of trace steps: "))
        origin = trace_origin(product_id, trace_steps)
        print("The origin of the product is: {}".format(origin))
    except ValueError as e:
        print(e)
# 增强安全性

if __name__ == "__main__":
    main()