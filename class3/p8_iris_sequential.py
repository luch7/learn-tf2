import tensorflow as tf
from sklearn import datasets
import numpy as np

x_train = datasets.load_iris().data
y_train = datasets.load_iris().target

# 实现数据集乱序
np.random.seed(116)
np.random.shuffle(x_train)
np.random.seed(116)
np.random.shuffle(y_train)
tf.random.set_seed(116)

# 三个神经元
model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(3, activation='softmax', kernel_regularizer=tf.keras.regularizers.l2())
])

# 优化器、损失函数、准确率
model.compile(optimizer=tf.keras.optimizers.SGD(lr=0.1),
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),  # 经过概率分布输出
              metrics=['sparse_categorical_accuracy'])
# 训练集的输入特征、训练集的标签、batch值、大循环次数、从训练集划分20%到测试集、多少次epoch测试一次（测试频率）
model.fit(x_train, y_train, batch_size=32, epochs=500, validation_split=0.2, validation_freq=20)

# 打印网络结构和参数统计
# 这里的鸢尾花是四输入三输出，input 1x4 * 4x3 + 1x3 = output，一共15个参数
# Model: "sequential"
# _________________________________________________________________
# Layer (type)                 Output Shape              Param #
# =================================================================
# dense (Dense)                (None, 3)                 15
# =================================================================
# Total params: 15
# Trainable params: 15
# Non-trainable params: 0
# _________________________________________________________________
#
# Process finished with exit code 0

model.summary()
