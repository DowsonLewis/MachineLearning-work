#!usr/bin/env python
#coding:utf-8

from tensorflow.example.tutorials.mnist import input_data

# 从MNIST_data/中读取MNIST数据。这条语句在数据不存在时，会自动执行下载
mnist = input_data.read_read_data_set("MNIST_data/",one_hot=True)

# 查看训练数据的大小
print('训练数据：',mnist.train.images.shape)#(55000,784)
print('训练标签：',minst.train.labels.shape)#(55000,10)

# 查看验证数据的大小
print('验证数据：',mnist.validation.images.shape)#(5000,784)
print('验证标签：',mnist.validation.labels.shape)#(5000,10)

# 查看测试数据的大小
print('测试数据：',mnist.test.images.shape)#(10000,784)
print('测试标签：',mnist.test.labels.shape)#(10000,10)

# 打印出第0张图片的向量表示
print('第0张图片的向量表示：',mnist.train.images[0,:])
