import tensorflow as tf

# 创建一个张量tensor
a = tf.constant([[[1, 2, 0], [3, 4, 0], [5, 6, 0], [7, 8, 0]], [[1, 2, 0], [3, 4, 0], [5, 6, 0], [7, 8, 0]]], dtype=tf.int64)
print("a:", a)
print("a.dtype:", a.dtype)
print("a.shape:", a.shape)
# a.shape: (2, 4, 3)
# 表示三维
# 第一维有2个元素：2个矩阵
# 第二维有4个元素：每个矩阵有4行
# 第三维有3个元素：每行有3个数字

# 本机默认 tf.int32  可去掉dtype试一下 查看默认值
