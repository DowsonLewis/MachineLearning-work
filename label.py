#coding:utf-8

from tensorflow.example.tutorials.mnist import input_data
import numpy as np

mnist = input_data.read_data_sets("MNIST_data/",one_hot=True)

# 看前20张训练图片的label
for i in range(20):
    # 得到独热表示
    one_hot_label = mnist.train.labels[i,:]
    # 通过np.argmax,可以直接获得原始的label
    # 因为只有1位为1，其他都是0
    label = np.argmax(one_hot_label)
    print('minsit_train_%d.jpg label:%d' %(i,label))
