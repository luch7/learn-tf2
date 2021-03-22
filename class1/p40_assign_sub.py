import tensorflow as tf

x = tf.Variable(4)
x.assign_sub(1)  # 自减
print("x:", x)  # 4-1=3
