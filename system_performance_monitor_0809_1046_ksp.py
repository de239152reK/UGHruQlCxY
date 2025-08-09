# 代码生成时间: 2025-08-09 10:46:05
import psutil
import time

"""
System Performance Monitor

A tool to monitor system performance using Python and Numpy.
"""


class SystemPerformanceMonitor:
    """
    A class to monitor system performance metrics.
    """

    def __init__(self):
        self.cpu_percentages = []

    def get_cpu_usage(self, interval=1, count=10):
        """
        Get CPU usage percentage over a specified interval.
        
        Args:
        interval (int): Time interval in seconds to measure CPU usage. Defaults to 1.
        count (int): Number of times to measure CPU usage. Defaults to 10.
        
        Returns:
        list: A list of CPU usage percentages.
        """
        for _ in range(count):
            try:
                cpu_usage = psutil.cpu_percent(interval=interval)
                self.cpu_percentages.append(cpu_usage)
            except Exception as e:
                print(f"Error getting CPU usage: {e}")
                return None
        return self.cpu_percentages

    def get_memory_usage(self):
        """
        Get system memory usage.
        
        Returns:
        tuple: A tuple containing used memory and total memory.
        """
        try:
            memory = psutil.virtual_memory()
            return (memory.used, memory.total)
        except Exception as e:
            print(f"Error getting memory usage: {e}")
            return None

    def get_disk_usage(self):
        """
        Get system disk usage.
        
        Returns:
        tuple: A tuple containing used disk space and total disk space.
        """
        try:
            disk = psutil.disk_usage('/')
            return (disk.used, disk.total)
        except Exception as e:
            print(f"Error getting disk usage: {e}")
            return None

    def monitor_system(self, interval=1, count=10):
        """
        Monitor system performance over a specified interval.
        
        Args:
        interval (int): Time interval in seconds to monitor system performance. Defaults to 1.
        count (int): Number of times to monitor system performance. Defaults to 10.
        """
        cpu_usages = self.get_cpu_usage(interval, count)
        memory_usage = self.get_memory_usage()
        disk_usage = self.get_disk_usage()
        return cpu_usages, memory_usage, disk_usage


# Example usage
if __name__ == '__main__':
    monitor = SystemPerformanceMonitor()
    cpu_usages, memory_usage, disk_usage = monitor.monitor_system(interval=1, count=10)
    print("CPU Usages: ", cpu_usages)
    print("Memory Usage: ", memory_usage)
    print("Disk Usage: ", disk_usage)