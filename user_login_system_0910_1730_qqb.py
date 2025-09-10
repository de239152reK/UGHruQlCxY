# 代码生成时间: 2025-09-10 17:30:42
import numpy as np
def login(user_input, stored_data):
    """
    用户登录验证系统
    参数：
    - user_input: 包含用户名和密码的元组
    - stored_data: 存储用户名和密码的字典
    返回：
    - 登录成功或失败的消息
    """
    try:
        username, password = user_input
        if username in stored_data and stored_data[username] == password:
            return f"登录成功，欢迎 {username}！"
        else:
            return "用户名或密码错误！"
    except Exception as e:
        return f"登录失败：{str(e)}"

def main():
    """
    示例主函数，用于测试登录验证系统
    """
    # 存储用户名和密码的字典
    users = {"admin": "12345", "user": "67890"}
    
    # 用户输入
    input_username = input("请输入用户名：")
    input_password = input("请输入密码：")
    
    # 登录验证
    result = login((input_username, input_password), users)
    print(result)

def __name__ == "__main__":
    main()
