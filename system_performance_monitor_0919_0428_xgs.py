# 代码生成时间: 2025-09-19 04:28:01
import psutil
import time
import numpy as np

"""
系统性能监控工具。
使用psutil库来监控CPU，内存和磁盘使用情况。
使用numpy库对数据进行处理和分析。
"""

class SystemPerformanceMonitor:
    def __init__(self, interval=1):
        """
        初始化系统性能监控工具。
        :param interval: 监控间隔时间（秒），默认为1秒
        """
        self.interval = interval

    def monitor_cpu_usage(self):
        """
        监控CPU使用率。
        返回过去1秒内的CPU使用率（百分比）。
        """
        try:
            cpu_usage = psutil.cpu_percent(interval=self.interval)
            return cpu_usage
        except Exception as e:
            print(f"监控CPU使用率时出错：{e}")
            return None

    def monitor_memory_usage(self):
        """
        监控内存使用情况。
        返回内存使用量（MB）。
        """
        try:
            memory = psutil.virtual_memory()
            used_memory = memory.total - memory.available
            return used_memory // (1024 * 1024)  # 转换为MB
        except Exception as e:
            print(f"监控内存使用情况时出错：{e}")
            return None

    def monitor_disk_usage(self):
        """
        监控磁盘使用情况。
        返回磁盘使用量（GB）。
        """
        try:
            disk_usage = psutil.disk_usage('/')
            used_disk = disk_usage.total - disk_usage.free
            return used_disk // (1024 ** 3)  # 转换为GB
        except Exception as e:
            print(f"监控磁盘使用情况时出错：{e}")
            return None

    def run(self):
        """
        运行系统性能监控工具。
        每隔1秒监控一次CPU，内存和磁盘使用情况。
        """
        while True:
            cpu_usage = self.monitor_cpu_usage()
            memory_usage = self.monitor_memory_usage()
            disk_usage = self.monitor_disk_usage()

            if cpu_usage is not None and memory_usage is not None and disk_usage is not None:
                print(f"CPU使用率：{cpu_usage}%")
                print(f"内存使用量：{memory_usage}MB")
                print(f"磁盘使用量：{disk_usage}GB")

            time.sleep(self.interval)

if __name__ == '__main__':
    monitor = SystemPerformanceMonitor(interval=1)
    monitor.run()