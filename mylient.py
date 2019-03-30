#coding:utf-8
 
from aip import AipImageClassify
 
""" 这里输入你创建应用获得的三个参数"""
APP_ID = '11638563'
API_KEY = 'XsQl0XGRGWeYIN7k52AMGVU4'
SECRET_KEY = 'z53nby7BINknecpiOSCkenPTFtYZUHsx'
 
client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)
 
""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()
 
""" 图片为存储在本地的图片，格式不限 """
image = get_file_content('180806-202532.png')
 
""" 调用通用物体识别 """
print (client.advancedGeneral(image));
 
