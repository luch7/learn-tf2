import tensorflow as tf

a = tf.zeros([2, 3])  # 二维-->矩阵
b = tf.ones(4)  # 一维-->数组
c = tf.fill([2, 3, 4], 9)  # 三维-->数字排成一个立体
print("a:", a)
print('aT:', tf.transpose(a))
print("b:", b)
print("c:", c)
