# 代码生成时间: 2025-09-03 20:53:25
import numpy as np


class OrderProcessing:
    """
    订单处理类，实现订单的创建、修改、删除和查询功能。
    """
    def __init__(self):
        """
        初始化订单存储列表。
        """
        self.orders = []

    def create_order(self, order_id, customer_name, product_details):
        """
        创建一个新订单。
        
        参数：
        order_id (str): 订单的唯一标识符。
        customer_name (str): 客户名称。
        product_details (dict): 产品详情，包括产品名称和数量。
        
        返回：
        bool: 创建成功返回True，否则返回False。
        """
        if not order_id or not customer_name or not product_details:
            print("Error: 订单信息不完整。")
            return False
        
        new_order = {
            'order_id': order_id,
            'customer_name': customer_name,
            'product_details': product_details
        }
        self.orders.append(new_order)
        return True

    def update_order(self, order_id, new_product_details):
        """
        更新订单的产品详情。
        
        参数：
        order_id (str): 订单的唯一标识符。
        new_product_details (dict): 新的产品详情。
        
        返回：
        bool: 更新成功返回True，否则返回False。
        """
        for order in self.orders:
            if order['order_id'] == order_id:
                if new_product_details:
                    order['product_details'] = new_product_details
                    return True
                else:
                    print("Error: 新的产品详情不能为空。")
                    return False
        print("Error: 订单不存在。")
        return False

    def delete_order(self, order_id):
        """
        删除一个订单。
        
        参数：
        order_id (str): 订单的唯一标识符。
        
        返回：
        bool: 删除成功返回True，否则返回False。
        """
        for i, order in enumerate(self.orders):
            if order['order_id'] == order_id:
                self.orders.pop(i)
                return True
        print("Error: 订单不存在。")
        return False

    def query_order(self, order_id=None):
        """
        查询订单。
        
        参数：
        order_id (str): 订单的唯一标识符，为空时查询所有订单。
        
        返回：
        list: 包含订单信息的列表。
        """
        if order_id:
            for order in self.orders:
                if order['order_id'] == order_id:
                    return [order]
            print("Error: 订单不存在。")
            return []
        else:
            return self.orders


# 示例代码
if __name__ == '__main__':
    order_processor = OrderProcessing()
    
    # 创建订单
    product_details = {'product_name': 'Apple', 'quantity': 10}
    order_processor.create_order('001', 'John Doe', product_details)
    
    # 更新订单
    order_processor.update_order('001', {'product_name': 'Banana', 'quantity': 15})
    
    # 查询订单
    query_result = order_processor.query_order('001')
    print(query_result)
    
    # 删除订单
    order_processor.delete_order('001')
    
    # 再次查询订单
    query_result = order_processor.query_order('001')
    print(query_result)