import numpy as np
import tensorflow as tf

test = tf.constant([[1, 2, 3], [2, 3, 4], [5, 4, 3], [8, 7, 2]])
print("test:\n", test)
print("每一列的最大值的索引：", tf.argmax(test, axis=0))  # 返回每一列最大值的索引，
# 比如：第0轴，就是列，第一列最大值为8，对应的下标为3；第二列最大值为7，对应的下标为3；第三列最大值为4，对应的下标为1
print("每一行的最大值的索引", tf.argmax(test, axis=1))  # 返回每一行最大值的索引
# 第1轴就是行
