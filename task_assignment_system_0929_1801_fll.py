# 代码生成时间: 2025-09-29 18:01:06
import numpy as np

"""
Task Assignment System
====================

This system is designed to assign tasks to workers based on their capabilities.
It uses numpy for efficient array operations.
"""

class TaskAssignmentSystem:
    """
    A class to manage task assignments to workers.

    Attributes:
        workers (dict): A dictionary with worker IDs as keys and their capabilities as values.
        tasks (list): A list of tasks to be assigned.
    """

    def __init__(self):
        """Initialize the task assignment system with an empty list of workers and tasks."""
        self.workers = {}
        self.tasks = []

    def add_worker(self, worker_id, capabilities):
        """Add a worker with their capabilities to the system.

        Args:
            worker_id (str): Unique identifier for the worker.
            capabilities (list): List of capabilities the worker has.
        """
        if not isinstance(capabilities, list):
            raise ValueError("Capabilities must be a list.")
        self.workers[worker_id] = capabilities

    def add_task(self, task, requirements):
        """Add a task with its requirements to the system.

        Args:
            task (str): Description of the task.
            requirements (list): List of capabilities required to complete the task.
        """
        if not isinstance(requirements, list):
            raise ValueError("Requirements must be a list.")
        self.tasks.append((task, requirements))

    def assign_tasks(self):
        """Assign tasks to workers based on their capabilities."""
        assignments = {}
        for task, requirements in self.tasks:
            for worker_id, capabilities in self.workers.items():
                if set(requirements).issubset(set(capabilities)):
                    if worker_id not in assignments:
                        assignments[worker_id] = []
                    assignments[worker_id].append(task)
                    break
        return assignments

    def display_assignments(self, assignments):
        """Display the assignments of tasks to workers.

        Args:
            assignments (dict): Dictionary of worker IDs and their assigned tasks.
        """
        for worker_id, tasks in assignments.items():
            print(f"Worker {worker_id} is assigned: {', '.join(tasks)}")

# Example usage:
if __name__ == '__main__':
    system = TaskAssignmentSystem()
    system.add_worker("worker1", ["coding", "design"])
    system.add_worker("worker2", ["coding", "testing"])
    system.add_task("Develop feature", ["coding"])
    system.add_task("Design interface", ["design"])
    system.add_task("Test feature", ["testing", "coding"])

    assignments = system.assign_tasks()
    system.display_assignments(assignments)