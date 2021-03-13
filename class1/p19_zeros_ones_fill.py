import tensorflow as tf

a = tf.zeros([2, 3])
b = tf.ones(4)
c = tf.fill([2, 3, 4], 9)
print("a:", a)
print("b:", b)
print("c:", c)
