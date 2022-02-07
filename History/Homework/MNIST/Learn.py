import Read_File #自己写的
import tensorflow as tf

from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

#加载数据，基于numpy
train_images = Read_File.demo_train_images.to_numpy().reshape((60000, 28, 28, 1))/255.0
train_labels = Read_File.demo_train_labels.to_numpy()
test_images = Read_File.demo_test_images.to_numpy().reshape((10000, 28, 28, 1))/255.0
test_labels = Read_File.demo_test_labels.to_numpy()

#可视化
plt.figure(figsize=(10, 10),)
for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i].reshape((28, 28)), cmap="gray")
    plt.xlabel(train_labels[i])
plt.show()

#增加卷积层和池化层（搞不懂），这里的input_shape是表示了28*28的单通道图片
model = models.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation='relu'))

#增加全连接层
model.add(layers.Flatten())
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(10, activation="softmax"))

model.summary()

check_path = './ckpt/cp-{epoch:04d}.ckpt'
# period 每隔 5 epoch保存一次
save_model_cb = tf.keras.callbacks.ModelCheckpoint(
    check_path, save_weights_only=True, verbose=1, period=5)
#跑五轮
model.compile(optimizer='adam',
                        loss='sparse_categorical_crossentropy',
                        metrics=['accuracy'])
model.fit(train_images, train_labels, epochs=5, callbacks=[save_model_cb])

test_loss, test_acc = model.evaluate(test_images, test_labels)
print("准确率: %.4f，共测试了%d张图片 " % (test_acc, len(test_labels)))
