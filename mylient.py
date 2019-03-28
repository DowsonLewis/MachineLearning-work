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
 
image = get_file_content('180806-202532.png')
 
""" 调用通用物体识别 """
print (client.advancedGeneral(image));
 
