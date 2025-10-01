# 代码生成时间: 2025-10-02 01:34:30
import numpy as np


class DataStats:
    """
    统计数据分析器，用于对数据集中的数值数据进行统计分析。
    """

def __init__(self, data):
    """
    初始化函数。
    :param data: 包含数值数据的列表或NumPy数组。
    """
    if not isinstance(data, (list, np.ndarray)):
        raise ValueError("Data must be a list or a NumPy array.")
    self.data = np.array(data)
    self.data = self.data[np.isfinite(self.data)]  # 过滤掉非数值

   
    def mean(self):
        """
        计算数据集的均值。
        :return: 数据集的均值。
        """
        return np.mean(self.data)

    def median(self):
        """
        计算数据集的中位数。
        :return: 数据集的中位数。
        """
        return np.median(self.data)

    def max(self):
        """
        计算数据集的最大值。
        :return: 数据集的最大值。
        """
        return np.max(self.data)

    def min(self):
        """
        计算数据集的最小值。
        :return: 数据集的最小值。
        """
        return np.min(self.data)

    def std_deviation(self):
        """
        计算数据集的标准差。
        :return: 数据集的标准差。
        """
        return np.std(self.data)

    def variance(self):
        """
        计算数据集的方差。
        :return: 数据集的方差。
        """
        return np.var(self.data)

    def skewness(self):
        """
        计算数据集的偏度。
        :return: 数据集的偏度。
        """
        return self.data.skew()

    def kurtosis(self):
        """
        计算数据集的峰度。
        :return: 数据集的峰度。
        """
        return self.data.kurt()

# 示例用法
if __name__ == '__main__':
    data = np.random.normal(loc=0, scale=1, size=1000)  # 生成正态分布的随机数据
    stats = DataStats(data)
    print("Mean: ", stats.mean())
    print("Median: ", stats.median())
    print("Max: ", stats.max())
    print("Min: ", stats.min())
    print("Standard Deviation: ", stats.std_deviation())
    print("Variance: ", stats.variance())
    print("Skewness: ", stats.skewness())
    print("Kurtosis: ", stats.kurtosis())