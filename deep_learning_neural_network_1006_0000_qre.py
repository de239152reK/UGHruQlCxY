# 代码生成时间: 2025-10-06 00:00:39
import numpy as np
from numpy.random import default_rng
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

"""
创建一个深度学习神经网络程序。
这个程序使用NumPy来实现一个简单的多层感知机（MLP），
用于分类任务。
"""

# 生成数据集
def generate_dataset():
    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    return X, y

# 标准化数据
def standardize_data(X):
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

# 神经网络激活函数
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# 激活函数的导数（用于反向传播）
def sigmoid_derivative(x):
    return x * (1 - x)

# 前向传播
def forward_propagation(X, weights, biases):
    layer1 = sigmoid(np.dot(X, weights[0]) + biases[0])
    layer2 = sigmoid(np.dot(layer1, weights[1]) + biases[1])
    return layer2

# 计算成本函数
def compute_cost(y, y_hat):
    return -np.mean(y * np.log(y_hat) + (1 - y) * np.log(1 - y_hat))

# 反向传播
def backpropagation(X, y, y_hat, weights, biases):
    delta2 = (y_hat - y) * sigmoid_derivative(y_hat)
    delta1 = delta2.dot(weights[1].T) * sigmoid_derivative(y_hat)
    
    d_weights1 = delta1.T.dot(X)
    d_biases1 = delta1.sum(axis=0)
    d_weights2 = delta2.T.dot(layer1)
    d_biases2 = delta2.sum(axis=0)
    return d_weights1, d_biases1, d_weights2, d_biases2

# 更新权重和偏置
def update_weights(weights, biases, d_weights, d_biases, learning_rate):
    weights[0] -= learning_rate * d_weights[0]
    biases[0] -= learning_rate * d_biases[0]
    weights[1] -= learning_rate * d_weights[1]
    biases[1] -= learning_rate * d_biases[1]
    return weights, biases

# 训练神经网络
def train(X, y, epochs, learning_rate):
    # 随机权重和偏置
    weights = [np.random.randn(20, 8), np.random.randn(8, 1)]
    biases = [np.zeros((1, 8)), np.zeros((1, 1))]
    
    for epoch in range(epochs):
        layer1 = sigmoid(np.dot(X, weights[0]) + biases[0])
        layer2 = sigmoid(np.dot(layer1, weights[1]) + biases[1])
        y_hat = layer2
        cost = compute_cost(y, y_hat)
        
        d_weights1, d_biases1, d_weights2, d_biases2 = backpropagation(X, y, y_hat, weights, biases)
        
        weights, biases = update_weights(weights, biases, [d_weights1, d_weights2], [d_biases1, d_biases2], learning_rate)
        
        if epoch % 100 == 0:
            print(f"Epoch {epoch}, Cost: {cost}")
    return weights, biases

# 主函数
def main():
    try:
        X, y = generate_dataset()
        X = standardize_data(X)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        
        weights, biases = train(X_train, y_train, epochs=1000, learning_rate=0.1)
        
        # 测试模型
        predictions = forward_propagation(X_test, weights, biases)
        accuracy = (np.round(predictions) == y_test.reshape(-1, 1)).mean()
        print(f"Test Accuracy: {accuracy * 100}%")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()