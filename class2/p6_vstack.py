import numpy as np

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
c = np.vstack((a, b))  # 将行向量组成矩阵
print("c:\n", c)

