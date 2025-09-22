# 代码生成时间: 2025-09-23 00:02:53
import psutil
import time
import numpy as np

"""
System Performance Monitor Tool

This tool uses the psutil library to monitor various system performances such as
CPU usage, memory usage, disk usage, and network usage.
"""

class SystemPerformanceMonitor:

    def __init__(self):
        """Initialize the SystemPerformanceMonitor class."""
        self.cpu_usages = []
        self.memory_usages = []
        self.disk_usages = []
        self.network_usages = []

    def monitor_cpu_usage(self, interval, duration):
        """Monitor CPU usage over a specified duration with a given interval.

        Args:
        interval (int): Time interval in seconds between each measurement.
        duration (int): Total duration in seconds to monitor the CPU usage.
        """
        for _ in range(duration // interval):
            try:
                cpu_usage = psutil.cpu_percent(interval=interval)
                self.cpu_usages.append(cpu_usage)
            except Exception as e:
                print(f"Error monitoring CPU usage: {e}")
            time.sleep(interval)

    def monitor_memory_usage(self, interval, duration):
        """Monitor memory usage over a specified duration with a given interval.

        Args:
        interval (int): Time interval in seconds between each measurement.
        duration (int): Total duration in seconds to monitor the memory usage.
        """
        for _ in range(duration // interval):
            try:
                memory = psutil.virtual_memory()
                memory_usage = memory.percent
                self.memory_usages.append(memory_usage)
            except Exception as e:
                print(f"Error monitoring memory usage: {e}")
            time.sleep(interval)

    def monitor_disk_usage(self, interval, duration):
        """Monitor disk usage over a specified duration with a given interval.

        Args:
        interval (int): Time interval in seconds between each measurement.
        duration (int): Total duration in seconds to monitor the disk usage.
        """
        for _ in range(duration // interval):
            try:
                disk_usage = psutil.disk_usage('/')
                self.disk_usages.append(disk_usage.percent)
            except Exception as e:
                print(f"Error monitoring disk usage: {e}")
            time.sleep(interval)

    def monitor_network_usage(self, interval, duration):
        """Monitor network usage over a specified duration with a given interval.

        Args:
        interval (int): Time interval in seconds between each measurement.
        duration (int): Total duration in seconds to monitor the network usage.
        """
        for _ in range(duration // interval):
            try:
                network_io = psutil.net_io_counters()
                tx, rx = network_io.bytes_sent, network_io.bytes_recv
                self.network_usages.append((tx, rx))
            except Exception as e:
                print(f"Error monitoring network usage: {e}")
            time.sleep(interval)

    def get_cpu_usage_data(self):
        """Get the collected CPU usage data.

        Returns:
        list: A list of CPU usage percentages.
        """
        return self.cpu_usages

    def get_memory_usage_data(self):
        """Get the collected memory usage data.

        Returns:
        list: A list of memory usage percentages.
        """
        return self.memory_usages

    def get_disk_usage_data(self):
        """Get the collected disk usage data.

        Returns:
        list: A list of disk usage percentages.
        """
        return self.disk_usages

    def get_network_usage_data(self):
        """Get the collected network usage data.

        Returns:
        list: A list of tuples containing network transmission and reception bytes.
        """
        return self.network_usages

    def plot_usage_data(self, data, title, ylabel):
        """Plot the collected usage data.

        Args:
        data (list): A list of usage data to plot.
        title (str): The title of the plot.
        ylabel (str): The label for the y-axis.
        """
        try:
            import matplotlib.pyplot as plt
            plt.plot(data)
            plt.title(title)
            plt.ylabel(ylabel)
            plt.xlabel('Time (s)')
            plt.show()
        except Exception as e:
            print(f"Error plotting data: {e}")

# Example usage
def main():
    monitor = SystemPerformanceMonitor()

    # Monitor CPU usage for 10 seconds with a 1-second interval
    monitor.monitor_cpu_usage(1, 10)
    # Plot the collected CPU usage data
    monitor.plot_usage_data(monitor.get_cpu_usage_data(), 'CPU Usage Over Time', 'CPU Usage (%)')

    # Monitor memory usage for 10 seconds with a 1-second interval
    monitor.monitor_memory_usage(1, 10)
    # Plot the collected memory usage data
    monitor.plot_usage_data(monitor.get_memory_usage_data(), 'Memory Usage Over Time', 'Memory Usage (%)')

    # Monitor disk usage for 10 seconds with a 1-second interval
    monitor.monitor_disk_usage(1, 10)
    # Plot the collected disk usage data
    monitor.plot_usage_data(monitor.get_disk_usage_data(), 'Disk Usage Over Time', 'Disk Usage (%)')

    # Monitor network usage for 10 seconds with a 1-second interval
    monitor.monitor_network_usage(1, 10)
    # Plot the collected network usage data
    monitor.plot_usage_data(list(zip(*monitor.get_network_usage_data())), 'Network Usage Over Time', 'Network Usage (Bytes)')

if __name__ == '__main__':
    main()