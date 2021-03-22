import tensorflow as tf

classes = 3
labels = tf.constant([0, 1, 2, 3])
output = tf.one_hot(labels, depth=classes)  # 第二个参数表示分类的个数，one_hot函数会根据此参数的值生成独热编码
# 独热编码：根据分类个数、独热码长度，生成 分类--独热码 一一对应的关系
# 一个独热码只含有一个1，其余为0
print("result of labels1:", output)
print("\n")
