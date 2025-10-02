# 代码生成时间: 2025-10-03 01:39:26
import numpy as np
import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.metrics.pairwise import cosine_similarity


class ProductRecommendationEngine:
    """商品推荐引擎，使用余弦相似度计算用户间相似性并推荐商品"""

    def __init__(self, user_item_matrix):
        """
        :param user_item_matrix: 用户-商品矩阵，行代表用户，列代表商品，值代表评分
        """
        self.user_item_matrix = user_item_matrix
        self.user_similarity_matrix = None
        self.item_similarity_matrix = None

    def calculate_similarity(self, user_based=True):
        """计算用户相似度或商品相似度
        :param user_based: 计算用户相似度还是商品相似度
        """
        matrix = self.user_item_matrix.T if user_based else self.user_item_matrix
        similarity = cosine_similarity(matrix)
        if user_based:
            self.user_similarity_matrix = similarity
        else:
            self.item_similarity_matrix = similarity

    def recommend(self, user_id, num_recommendations=5, user_based=True):
        "