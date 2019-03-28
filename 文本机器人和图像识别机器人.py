#coding=utf8
import requests
import itchat
import base64
import shutil,os
from itchat.content import *
from aip import AipImageClassify



KEY = '15fcf42e17d248f7b2156528c66870f7'

APP_ID = '11638563'
API_KEY = 'XsQl0XGRGWeYIN7k52AMGVU4'
SECRET_KEY = 'z53nby7BINknecpiOSCkenPTFtYZUHsx'

client = AipImageClassify(APP_ID, API_KEY, SECRET_KEY)

@itchat.msg_register([TEXT],isGroupChat=True)
def groupMsgReply(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    if msg['isAt']:
        content=msg['Content']
        data = {
            'key'    : KEY,
            'info'   : content,
            'userid' : 'wechat-robot',
        }
        try:
            r = requests.post(apiUrl,data=data).json()
            username = msg['ActualNickName']
            return r.get('text')
        except:
            return
    
@itchat.msg_register(itchat.content.TEXT)
def getResponse(msg):
    # 构造要发送给服务器的数据
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
        }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return
@itchat.msg_register(itchat.content.TEXT)
def tulingReply(msg):
    # 为了保证在图灵Key出现问题的时候仍旧可以回复，这里设置一个默认回复
    defaultReply = 'Lemon已接收 ' + msg['Text']
    # 如果图灵Key出现问题，那么reply将会是None
    reply = getResponse(msg['Text'])
    return reply or defaultReply

@itchat.msg_register([PICTURE])
def imgClassfy(msg):
    global client
    #下载图片
    msg.download(msg.fileName)
    '''itchat.send('@%s@%s' % (
        'img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']),
        msg['FromUserName'])'''
    #移动图片到img文件夹下
    shutil.move(".\\"+msg.fileName,".\\img")
    fp = open(".\\img\\"+msg.fileName,'rb')
    image = fp.read()
    fp.close()
    result = client.advancedGeneral(image)
    p = result['result']
    b1,b2,b3,b4,b5 = p[0].get('keyword'),p[1].get('keyword'),p[2].get('keyword'),p[3].get('keyword'),p[4].get('keyword')
    p1,p2,p3,p4,p5 = p[0].get('score'),p[1].get('score'),p[2].get('score'),p[3].get('score'),p[4].get('score')
    a0 = '我猜这张图片的主要内容是：'
    a1 = str(p1)+"的概率是："+str(b1)
    a2 = str(p2)+"的概率是："+str(b2)+'；'
    a3 = str(p3)+"的概率是："+str(b3)+'；'
    a4 = str(p4)+"的概率是："+str(b4)+'；'
    a5 = str(p5)+"的概率是："+str(b5)+'。'
    attr = a0+a1  #+a2+a3+a4+a5
    return itchat.send(msg=attr,toUserName=msg['FromUserName'])
    
# 使用热启动
itchat.auto_login(hotReload=True)
itchat.run()
