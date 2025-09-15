# 代码生成时间: 2025-09-16 04:25:28
import psutil
import time
import numpy as np
"""
系统性能监控工具
使用PYTHON和NUMPY框架监控系统性能，包括CPU利用率、内存使用情况、磁盘使用情况等。
"""

def monitor_cpu_utilization(interval=1, duration=10):
    """监控CPU利用率
    Args:
        interval (int): 监控间隔（秒）
        duration (int): 监控持续时间（秒）
    Returns:
        list: CPU利用率时间序列
    """
    utilization_series = []
    start_time = time.time()
    while time.time() - start_time < duration:
        utilization = psutil.cpu_percent(interval=interval)
        utilization_series.append(utilization)
        time.sleep(interval)
    return np.array(utilization_series)

def monitor_memory_usage(interval=1, duration=10):
    """监控内存使用情况
    Args:
        interval (int): 监控间隔（秒）
        duration (int): 监控持续时间（秒）
    Returns:
        tuple: (内存使用量时间序列，内存总量时间序列)
    """
    memory_usage_series = []
    memory_total_series = []
    start_time = time.time()
    while time.time() - start_time < duration:
        memory = psutil.virtual_memory()
        memory_usage_series.append(memory.used / (1024 ** 3))  # GB
        memory_total_series.append(memory.total / (1024 ** 3))  # GB
        time.sleep(interval)
    return np.array(memory_usage_series), np.array(memory_total_series)

def monitor_disk_usage(interval=1, duration=10):
    """监控磁盘使用情况
    Args:
        interval (int): 监控间隔（秒）
        duration (int): 监控持续时间（秒）
    Returns:
        list: 磁盘使用量时间序列
    """
    disk_usage_series = []
    start_time = time.time()
    while time.time() - start_time < duration:
        disk_usage = psutil.disk_usage('/')
        disk_usage_series.append(disk_usage.used / (1024 ** 3))  # GB
        time.sleep(interval)
    return np.array(disk_usage_series)

if __name__ == '__main__':
    try:
        print("监控CPU利用率...")
        cpu_utilization = monitor_cpu_utilization(interval=1, duration=10)
        print("CPU利用率时间序列：", cpu_utilization)

        print("监控内存使用情况...")
        memory_usage, memory_total = monitor_memory_usage(interval=1, duration=10)
        print("内存使用量时间序列：", memory_usage)
        print("内存总量时间序列：", memory_total)

        print("监控磁盘使用情况...")
        disk_usage = monitor_disk_usage(interval=1, duration=10)
        print("磁盘使用量时间序列：", disk_usage)
    except Exception as e:
        print(f"监控过程中出现错误：{e}")