# 代码生成时间: 2025-09-21 02:55:55
import numpy as np
import os
import psutil
from subprocess import Popen, PIPE

"""
Process Manager

A simple process manager that lists processes and allows to terminate them.
"""

class ProcessManager:
    def __init__(self):
        """Initialize the ProcessManager with a list of all running processes."""
        self.processes = []
        self._load_processes()

    def _load_processes(self):
        """Load the list of all running processes."""
        for proc in psutil.process_iter(['pid', 'name', 'status']):
            try:
                self.processes.append(proc.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

    def list_processes(self):
        """List all running processes."""
        print("PID\	Name\	Status")
        for proc in self.processes:
            print(f"{proc['pid']}\	{proc['name']}\	{proc['status']}")

    def terminate_process(self, pid):
        """Terminate a process by its PID."""
        try:
            process = psutil.Process(pid)
            process.terminate()
            print(f"Process {pid} terminated successfully.")
        except psutil.NoSuchProcess:
            print(f"Process {pid} does not exist.")
        except psutil.AccessDenied:
            print(f"Permission denied to terminate process {pid}.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def monitor_processes(self):
        "