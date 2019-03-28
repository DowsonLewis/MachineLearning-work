#encoding:utf8
from aip import AipSpeech

""" 你的 APPID AK SK """
APP_ID = '11638573'
API_KEY = 'i7GrxEZTu2wUy275NGku06m7'
SECRET_KEY = 'kaQGRN9Fq8baVM3W4bOZXqHazAcyZNo0'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)
result = client.synthesis(text = '茕茕孑立 沆瀣一气 踽踽独行 醍醐灌顶 绵绵瓜瓞 奉为圭臬 龙行龘龘 犄角旮旯 娉婷袅娜 涕泗滂沱 呶呶不休 不稂不莠 咄嗟 蹀躞 耄耋 饕餮 囹圄 蘡薁 觊觎 龃龉 狖轭鼯轩 怙恶不悛 其靁虺虺 腌臢孑孓 陟罚臧否 针砭时弊 鳞次栉比 一张一翕', options={'vol':5})

if not isinstance(result,dict):
    with open('audio.mp3','wb') as f:
        f.write(result)
else:print(result)
