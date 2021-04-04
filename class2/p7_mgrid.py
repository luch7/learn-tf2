import numpy as np
import tensorflow as tf

# 生成等间隔数值点
x, y = np.mgrid[1:5:3j, 2:6:1]  # 起始值：结束值：步长（为实数时，表示步长，为虚数时表示点的个数），前闭后开区间，第一个参数返回第一维，第二个参数返回第二维，以此类推
z = np.mgrid[1:5:3j, 2:6:1]
# 将x, y拉直，并合并配对为二维张量，生成二维坐标点
grid = np.c_[x.ravel(), y.ravel()]
print("x:\n", x)
print("y:\n", y)
print("z:\n", z)
print("x.ravel():\n", x.ravel())
print("y.ravel():\n", y.ravel())
print('grid:\n', grid)


