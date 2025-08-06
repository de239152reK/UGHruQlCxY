# 代码生成时间: 2025-08-06 20:05:35
import numpy as np


# 统计数据分析器类
class DataAnalyzer:
    def __init__(self, data):
        """初始化数据分析师
        :param data: numpy数组，包含要分析的数据
        """
        self.data = np.array(data)
        self._validate_data()

    def _validate_data(self):
        """验证数据是否为有效的numpy数组
        """
        if not isinstance(self.data, np.ndarray):
            raise ValueError("数据必须是numpy数组")

    def mean(self):
        """计算数据的平均值
        :return: 平均值
        """
        return np.mean(self.data)

    def median(self):
        """计算数据的中位数
        :return: 中位数
        """
        return np.median(self.data)

    def std_dev(self):
        """计算数据的标准差
        :return: 标准差
        """
        return np.std(self.data)

    def min_max(self):
        """计算数据的最小值和最大值
        :return: 元组，包含最小值和最大值
        """
        return np.min(self.data), np.max(self.data)

    def histogram(self, bins=10):
        """生成数据的直方图
        :param bins: 直方图的箱数，默认为10
        :return: 直方图的箱边界和频率
        """
        return np.histogram(self.data, bins=bins)


# 示例用法
if __name__ == '__main__':
    # 示例数据
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # 创建数据分析师实例
    analyzer = DataAnalyzer(data)

    # 计算平均值
    print("平均值:", analyzer.mean())

    # 计算中位数
    print("中位数:", analyzer.median())

    # 计算标准差
    print("标准差:", analyzer.std_dev())

    # 计算最小值和最大值
    min_val, max_val = analyzer.min_max()
    print("最小值:", min_val)
    print("最大值:", max_val)

    # 生成直方图
    hist, bin_edges = analyzer.histogram(bins=5)
    print("直方图箱边界:", bin_edges)
    print("直方图频率:", hist)