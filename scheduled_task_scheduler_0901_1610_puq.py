# 代码生成时间: 2025-09-01 16:10:51
import numpy as np
import schedule
import time
from threading import Thread

"""
定时任务调度器

该程序实现了一个基本的定时任务调度器，它允许用户注册任务，并在指定的时间执行这些任务。
任务可以按秒、分钟、小时等时间间隔调度。
"""

class TaskScheduler:
    def __init__(self):
        """初始化调度器"""
        self.tasks = []
        self.scheduler = schedule.Scheduler()
        self.running = False

    def add_task(self, task, interval, unit='seconds'):
        """添加任务到调度器

        参数:
        task: 要执行的任务函数
        interval: 任务执行的间隔时间
        unit: 时间单位（秒、分钟、小时）
        """
        if unit == 'seconds':
            schedule.every(interval).seconds.do(task)
        elif unit == 'minutes':
            schedule.every(interval).minutes.do(task)
        elif unit == 'hours':
            schedule.every(interval).hours.do(task)
        else:
            raise ValueError("Unsupported time unit. Use 'seconds', 'minutes', or 'hours'.")
        
        self.tasks.append((task, interval, unit))

    def start(self):
        """启动调度器"""
        if not self.running:
            self.running = True
            thread = Thread(target=self._run)
            thread.start()
        else:
            print("Scheduler is already running.")

    def stop(self):
        """停止调度器"""
        self.running = False

    def _run(self):
        """私有方法：运行调度器"""
        while self.running:
            self.scheduler.run_pending()
            time.sleep(1)

# 示例：如何使用TaskScheduler
def example_task():
    print("Task executed at: {}".format(time.ctime()))

if __name__ == '__main__':
    scheduler = TaskScheduler()
    try:
        scheduler.add_task(example_task, 10, 'seconds')  # 每10秒执行example_task
        scheduler.start()
        
        # 为了示例，让程序运行一段时间后停止
        time.sleep(60)  # 运行60秒
        scheduler.stop()
    except KeyboardInterrupt:
        scheduler.stop()
        print("Scheduler stopped by user.")
    except Exception as e:
        scheduler.stop()
        print("Error occurred: {}".format(str(e)))
