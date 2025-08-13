# 代码生成时间: 2025-08-13 12:10:08
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider


# 定义一个函数来更新图表
def update(val):
    # 获取滑块的值
    a = slider.val
    # 根据滑块的值重新生成数据
    data = np.exp(a * np.linspace(-2, 2, 200))
    # 更新图表
    line.set_ydata(data)
    fig.canvas.draw_idle()

# 创建一个图形和子图
# TODO: 优化性能
fig, ax = plt.subplots()
# 创建一个滑块
# 改进用户体验
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
slider = Slider(ax_slider, 'a', -2., 2., valinit=-1.)
# NOTE: 重要实现细节
# 将滑块的值改变时的回调函数绑定到滑块
# 添加错误处理
slider.on_changed(update)

# 生成初始数据和图表
# 扩展功能模块
data = np.exp(-1 * np.linspace(-2, 2, 200))
line, = ax.plot(data)
ax.set_ylim(0, 10)

# 显示图表
plt.show()