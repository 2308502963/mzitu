# _*_ coding: utf-8 _*_
# @Time : 2020/10/6 15:48
# @Author : moran office
# File : weather.py
# Software : PyChram

# 用来爬取天气信息的py

import requests
import json

url = "https://v0.yiketianqi.com/api?version=v61&appid=38624114&appsecret=P1SBInud"

def getWeather1():


    json1 = requests.get(url).text
    # print(json.text)

    w_dict = json.loads(json1)
    # print(w_dict['date'])
    # print(w_dict['week'])
    # print(w_dict['city'])
    # print(w_dict['country'])
    # print(w_dict['wea'])
    # print(w_dict['tem'])
    # print(w_dict['air_tips'])

    jsonObj = {
        "date":w_dict['date'],
        "week":w_dict['week'],
        "country":w_dict['country'],
        "city":w_dict['city'],
        "wea":w_dict['wea'],
        "tem":w_dict['tem'],
        "air_tips":w_dict['air_tips']
    }
    return jsonObj
#
# if __name__ == '__main__':
#     getWeather1()

