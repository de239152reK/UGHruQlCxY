# 代码生成时间: 2025-09-09 19:29:49
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, interactive, widgets
from IPython.display import display

"""
Interactive Chart Generator

This program generates interactive charts using Python, NumPy, and Matplotlib.
It allows users to select different types of plots, such as line, scatter, and histogram.
"""

def generate_line_chart(x, y):
    """Generate a line chart with the given x and y values."""
    plt.figure(figsize=(8, 5))
    plt.plot(x, y, label='Line')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Line Chart')
    plt.legend()
    plt.grid(True)
    plt.show()


def generate_scatter_chart(x, y):
    """Generate a scatter chart with the given x and y values."""
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y, label='Scatter')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Scatter Chart')
    plt.legend()
    plt.grid(True)
    plt.show()


def generate_histogram(data):
    """Generate a histogram with the given data."""
    plt.figure(figsize=(8, 5))
    plt.hist(data, bins=20, label='Histogram')
    plt.xlabel('Value')
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    """Main function to create the interactive chart generator."