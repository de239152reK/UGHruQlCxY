# 代码生成时间: 2025-09-12 17:03:09
import numpy as np
import threading
import time
from datetime import datetime, timedelta

"""
定时任务调度器

这个模块实现了一个简单的定时任务调度器，允许用户定义需要执行的任务和执行的时间。
任务可以是任意的Python函数，调度器将在指定的时间自动调用这些函数。
"""

class Scheduler:
    def __init__(self):
        """初始化调度器"""
        self.tasks = []  # 存储任务的列表

    def add_task(self, task, run_at):
        "