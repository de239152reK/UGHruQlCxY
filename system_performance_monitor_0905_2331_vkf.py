# 代码生成时间: 2025-09-05 23:31:06
import psutil
import time

"""
A simple system performance monitor tool using Python and psutil library.
This tool monitors CPU, memory, and disk usage over a specified period of time.
"""

def monitor_system_performance(interval, duration):
    """
    Monitor system performance metrics at a specified interval for a certain duration.

    Args:
        interval (float): The time interval in seconds between each measurement.
        duration (int): The total duration in seconds for which to monitor the system.
    """
    start_time = time.time()
    while time.time() - start_time < duration:
        cpu_usage = psutil.cpu_percent(interval)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        print(f"CPU Usage: {cpu_usage}%")
        print(f"Memory Usage: {memory_usage}%")
        print(f"Disk Usage: {disk_usage}%")

        # Wait for the specified interval before the next measurement
        time.sleep(interval)

def main():
    """
    The main function to run the system performance monitor tool.
    """
    try:
        # Define the interval and duration for monitoring
        interval = 5.0  # seconds
        duration = 120  # seconds (2 minutes)

        # Run the system performance monitor
        monitor_system_performance(interval, duration)
    except Exception as e:
        # Handle any unexpected errors
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()