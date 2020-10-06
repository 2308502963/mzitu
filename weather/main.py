# _*_ coding: utf-8 _*_
# @Time : 2020/10/6 15:40
# @Author : moran office
# File : main.py
# Software : PyChram

from weather import weather1
from weather.words import word
from flask import Flask
app = Flask(__name__)

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


if __name__ == "__main__":
    app.run()