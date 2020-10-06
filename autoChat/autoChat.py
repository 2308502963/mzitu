# _*_ coding: utf-8 _*_
# @Time : 2020/1/16 16:56
# @Author : moran office
# File : autoChat.py
# Software : PyChram

import urllib.request
import urllib.parse
import json
import itchat
import requests

api_url = "http://openapi.tuling123.com/openapi/api/v2"
key = "ab4d08a2b4d240cea9516455a1e9842d"

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
def reply(msg):
    defaultreply = "你说的是:"+msg["text"]+"吧!"
    reply = get_response(msg['text'])
    return reply or defaultreply

itchat.login()
itchat.run()