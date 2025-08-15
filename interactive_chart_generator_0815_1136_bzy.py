# 代码生成时间: 2025-08-15 11:36:55
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib import colors as mcolors

"""
Interactive Chart Generator"""

# Define a class to handle the interactive chart
class InteractiveChart:
    def __init__(self, x_data, y_data):
        """Initialize the chart with x and y data."""
        self.x_data = np.array(x_data)
        self.y_data = np.array(y_data)
        self.fig, self.ax = plt.subplots()
        self.line, = self.ax.plot(self.x_data, self.y_data)
        self.ax.set_xlabel('X-axis')
        self.ax.set_ylabel('Y-axis')
        self.ax.set_title('Interactive Chart')
        self.fig.subplots_adjust(bottom=0.25)
        self.init_slider()

    def init_slider(self):
        """Initialize a slider to control the line color."""
        axcolor = 'lightgoldenrodyellow'
        self.axcolor = plt.axes([0.2, 0.1, 0.65, 0.03], facecolor=axcolor)
        self.slider = Slider(self.axcolor, 'Color', 0.0, 1.0, valinit=0.5)
        self.slider.on_changed(self.update_line_color)

    def update_line_color(self, val):
        """Update the line color based on the slider's value."""
        color_norm = mcolors.Normalize(vmin=0, vmax=1, clip=False)
        new_color = plt.cm.viridis(color_norm(val))
        self.line.set_color(new_color)
        self.fig.canvas.draw_idle()

    def show(self):
        "