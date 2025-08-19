# 代码生成时间: 2025-08-20 04:14:21
import numpy as np
import requests
from urllib.parse import urlparse

"""
URL链接有效性验证工具

该工具使用Python和NumPy框架来验证URL链接的有效性。
它检查URL是否符合基本的格式要求，并尝试通过HTTP请求来验证其可访问性。

Attributes:
    None

Methods:
    is_valid_url(url): 验证URL是否有效。
    validate_urls(url_list): 验证多个URL链接的有效性。
"""

def is_valid_url(url):
    """验证URL是否有效。"""
    try:
        # 使用urlparse解析URL
        parsed_url = urlparse(url)

        # 检查协议和网络位置部分
        if not all([parsed_url.scheme, parsed_url.netloc]):
            return False

        # 使用requests库尝试访问URL
        response = requests.head(url, allow_redirects=True, timeout=5)
        # 检查HTTP响应状态码
        return response.status_code == 200
    except (requests.RequestException, ValueError) as e:
        # 捕获请求异常和URL解析异常
        print(f"Error validating URL {url}: {e}")
        return False

def validate_urls(url_list):
    """验证多个URL链接的有效性。

    Args:
        url_list (list): 需要验证的URL列表。

    Returns:
        dict: 包含URL和其有效性结果的字典。
    """
    valid_urls = {}
    for url in url_list:
        is_valid = is_valid_url(url)
        valid_urls[url] = is_valid
    return valid_urls

# 示例用法
if __name__ == '__main__':
    test_urls = [
        "http://www.google.com",
        "https://www.example.com",
        "http://invalid-url",
        "http://www.google.com/invalid-page"
    ]
    
    result = validate_urls(test_urls)
    for url, is_valid in result.items():
        print(f"URL: {url}, Valid: {is_valid}")