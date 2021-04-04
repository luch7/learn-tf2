import numpy as np

rdm = np.random.RandomState(seed=1)
a = rdm.rand()
b = rdm.rand(2, 3, 4)  # 三维数组
print("a:", a)
print("b:", b)
