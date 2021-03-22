import tensorflow as tf

with tf.GradientTape() as tape:
    x = tf.Variable(tf.constant(2.0))
    y = tf.pow(x, 3)  # y等于x的3次方
grad = tape.gradient(y, x)  # y对x求导
print(grad)
