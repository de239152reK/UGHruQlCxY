# 代码生成时间: 2025-09-22 03:09:49
import psutil
import numpy as np

"""
System Performance Monitor - A tool to monitor system performance metrics

This module uses the psutil library to fetch system performance data and
NumPy for data manipulation and analysis.
"""


class SystemPerformanceMonitor:
    def __init__(self):
        """Initialize the monitor with current system metrics."""
        self.cpu_usage = self.get_cpu_usage()
        self.memory_usage = self.get_memory_usage()
        self.disk_usage = self.get_disk_usage()
        self.network_usage = self.get_network_usage()

    def get_cpu_usage(self):
        """Get the current CPU usage percentage."""
        try:
# 优化算法效率
            return psutil.cpu_percent(interval=1)
        except Exception as e:
            print(f"Error fetching CPU usage: {e}")
# NOTE: 重要实现细节
            return None

    def get_memory_usage(self):
# 优化算法效率
        """Get the current memory usage details."""
        try:
# 扩展功能模块
            mem = psutil.virtual_memory()
            return {
                "total": mem.total,
                "available": mem.available,
                "used": mem.used,
                "percentage": mem.percent
            }
# NOTE: 重要实现细节
        except Exception as e:
            print(f"Error fetching memory usage: {e}")
            return None

    def get_disk_usage(self):
        """Get the current disk usage details."""
        try:
            disk = psutil.disk_usage('/')
            return {
                "total": disk.total,
                "used": disk.used,
                "free": disk.free,
                "percentage": disk.percent
            }
        except Exception as e:
# 改进用户体验
            print(f"Error fetching disk usage: {e}")
            return None

    def get_network_usage(self):
        """Get the current network usage details."""
        try:
# 改进用户体验
            net_io = psutil.net_io_counters()
            return {
                "bytes_sent": net_io.bytes_sent,
                "bytes_recv": net_io.bytes_recv,
                "packets_sent": net_io.packets_sent,
                "packets_recv": net_io.packets_recv
            }
        except Exception as e:
            print(f"Error fetching network usage: {e}")
            return None

    def monitor(self, interval=1):
        """Continuously monitor system performance at specified interval."""
# FIXME: 处理边界情况
        while True:
            cpu_usage = self.get_cpu_usage()
            memory_usage = self.get_memory_usage()
            disk_usage = self.get_disk_usage()
            network_usage = self.get_network_usage()

            print(f"CPU Usage: {cpu_usage}%")
            print(f"Memory Usage: {memory_usage['percentage']}%")
            print(f"Disk Usage: {disk_usage['percentage']}%")
            print(f"Network Usage: Sent {network_usage['bytes_sent']} bytes, Recv {network_usage['bytes_recv']} bytes")

            time.sleep(interval)

if __name__ == "__main__":
    monitor = SystemPerformanceMonitor()
    monitor.monitor(interval=5)  # Set the monitoring interval to 5 seconds