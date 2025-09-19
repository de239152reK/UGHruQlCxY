# 代码生成时间: 2025-09-19 18:10:07
import psutil
import time

"""
System Performance Monitor

This script provides a simple system performance monitoring tool using Python and psutil library.
It allows users to monitor CPU usage, memory usage, disk usage, and network IO.
"""

class SystemMonitor:
    def __init__(self):
# 改进用户体验
        """Initialize the SystemMonitor class."""
        pass

    def get_cpu_usage(self):
# FIXME: 处理边界情况
        """Get the current CPU usage percentage."""
        try:
            cpu_usage = psutil.cpu_percent(interval=1)
            return cpu_usage
        except Exception as e:
            print(f"Error getting CPU usage: {e}")
            return None

    def get_memory_usage(self):
        """Get the current memory usage percentage."""
        try:
            memory = psutil.virtual_memory()
            memory_usage = memory.percent
            return memory_usage
# 增强安全性
        except Exception as e:
            print(f"Error getting memory usage: {e}")
            return None

    def get_disk_usage(self, disk_path):
        """Get the disk usage percentage for the specified disk path."""
        try:
# TODO: 优化性能
            disk_usage = psutil.disk_usage(disk_path)
            disk_usage_percentage = disk_usage.percent
            return disk_usage_percentage
# FIXME: 处理边界情况
        except Exception as e:
# NOTE: 重要实现细节
            print(f"Error getting disk usage for {disk_path}: {e}")
            return None

    def get_network_io(self):
        """Get the current network IO statistics."""
        try:
            network_io = psutil.net_io_counters()
            # Return bytes_sent and bytes_recv as a dictionary
            return {"bytes_sent": network_io.bytes_sent, "bytes_recv": network_io.bytes_recv}
        except Exception as e:
            print(f"Error getting network IO: {e}")
            return None

    def monitor_system(self, interval=1):
        """Continuously monitor system performance at a specified interval."""
        while True:
# FIXME: 处理边界情况
            cpu_usage = self.get_cpu_usage()
            memory_usage = self.get_memory_usage()
            disk_usage = self.get_disk_usage('/')
            network_io = self.get_network_io()

            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage}%")
# FIXME: 处理边界情况
            print(f"Disk Usage: {disk_usage}%")
            print(f"Network IO: {network_io}")

            time.sleep(interval)
# 添加错误处理

if __name__ == "__main__":
    monitor = SystemMonitor()
    monitor.monitor_system(interval=2)  # Set the monitoring interval to 2 seconds
