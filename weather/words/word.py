# _*_ coding: utf-8 _*_
# @Time : 2020/10/6 16:25
# @Author : moran office
# File : word.py
# Software : PyChram

import requests
import json

url = "https://wen.mouse123.cn/Api/Sentence/Djt"

# http请求头，防止反爬虫
refer = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

#
response = requests.get(url, headers = refer)
# print(response.text)

result = json.loads(response.text)
# print(result)

def getWord():
    return result