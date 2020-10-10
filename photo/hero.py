# _*_ coding: utf-8 _*_
# @Time : 2020/10/10 14:41
# @Author : moran office
# File : hero.py
# Software : PyChram

import requests
import json
import os
from bs4 import BeautifulSoup

path = "E:\\hero\\"
 # 一共138 页

# base_url = "https://lol.qq.com/data/info-defail.shtml?id=".format(page)
# https://game.gtimg.cn/images/lol/act/img/js/hero/1.js

def save_hero(page = 1):
    base_url = "https://game.gtimg.cn/images/lol/act/img/js/hero/{}.js".format(page)
    # print(base_url)
    response = requests.get(base_url)
    # response.encoding = response.apparent_encoding
    # soup = BeautifulSoup(response.text, "html.parser")
    # ul = soup.find("ul", id= "skinBG")
    # print(ul.text)
    if not response.ok:
        print("url不存在")
        return
    else:
        data = json.loads(response.text)
        # print(data)

        hero = data["hero"]
        img_data_list = data["skins"]

        file_name = hero["name"] + "_" + hero["title"]  # 文件夹名称
        if (os.path.exists(path + file_name)):
            print('目录已存在')
            flag = 1
        else:
            os.makedirs(path + file_name)
            flag = 0
        os.chdir(path + file_name)  # cd 进文件夹
        if (flag == 1 and len(os.listdir(path + file_name)) >= len(img_data_list)):
            print('已经保存完毕，跳过')
            #continue
            return
        print("开始保存："+file_name)
        for img_data in img_data_list:  # 遍历list
            img_name = img_data["mainImg"].split("/")[-1]
            img_url = img_data["mainImg"]
            print(img_url)
            try:
                img = requests.get(img_url)
                f = open(img_name, 'wb')
                f.write(img.content)
                f.close()
            except:
                print("发生错误,将跳过")
                pass
        print("单个英雄保存完成")


for m in range(149):
    print("第%d页",m + 1)
    save_hero(m +1 )
print("所有英雄保存成功")


