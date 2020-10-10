# _*_ coding: utf-8 _*_
# @Time : 2020/10/6 15:40
# @Author : moran office
# File : main.py
# Software : PyChram

from weather import weather1
from weather.words import word
from flask import Flask
from flask_cors import *
import json

app = Flask(__name__)
CORS(app, supports_credentials=True) # 解决跨域请求问题

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/getWeather")
def getWeather():
    str = weather1.getWeather1()
    return str

@app.route("/getWord")
def getWord1():
    word1 = word.getWord()
    return word1

@cross_origin
@app.route("/getPic")
def getPic():
    dict = [
        {"url": "huaban.com",
         "path": "https://hbimg.huabanimg.com/a53ad2e2dc16932c0d491f6531045e80ad80d9697b968-DoYY7l_fw658/format/webp"},
        {"url": "huaban.com", "path": "https://dss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=3088786723,881777113&fm=26&gp=0.jpg"},
        {"url": "huaban.com", "path": "https://dss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=3612597965,1770541226&fm=26&gp=0.jpg"}
    ]
    return json.dumps(dict) # 转为json对象

if __name__ == "__main__":
    app.run()
