# _*_ coding: utf-8 _*_
# @Time : 2020/1/16 19:11
# @Author : moran office
# File : 2.py
# Software : PyChram

import requests
import itchat
from itchat.content import *
import datetime
import time

# 每日一句
def get_sentence(api):
    res = requests.get(api)
    return res.json()

#
def get_response(msg):
    data = {
        'key': key,
        'info': msg,
        'userid': '123',
    }
    try:
        r = requests.post(api_url, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def auto_reply(msg):
    print("接收到消息:"+msg['Content'])
    itchat.send_msg(get_response(msg['Content']),toUserName=msg['FromUserName'])
    print("自动回府："+get_response(msg['Content']))

if __name__=='__main__':
    itchat.login()
    api_url = "http://openapi.tuling123.com/openapi/api/v2"
    key = "ab4d08a2b4d240cea9516455a1e9842d"

    # 金山词霸每日一句
    jinshanapi = "http://open.iciba.com/dsapi/"
    sentence = get_sentence(jinshanapi)
    # print(sentence)
    content = sentence['content']   # 英文的句子
    note = sentence['note'] # 中文的句子
    # print("{}:{}".format(content, note))

    user = itchat.search_friends()
    userName = user[0]['userName']

    while True:
        time = datetime.datetime.now()
        hour = time.hour
        minute = time.minute
        # print("{}:{}".format(hour, minute))
        # break
        if hour == 5 and minute == 20:
            itchat.send_msg('%s' % content, toUserName=userName)
        else:
            time.sleep(10)
            continue
    itchat.run

