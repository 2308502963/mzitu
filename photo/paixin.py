# _*_ coding: utf-8 _*_
# @Time : 2020/10/9 14:53
# @Author : moran office
# File : paixin.py
# Software : PyChram

import requests
import json
import os
from bs4 import BeautifulSoup

# base_url = "https://v.paixin.com/mediapack/16/"  # 后面构造页码  虚假的请求

# https://api2.paixin.com/albums/16/medias?page=0&size=45&sort=createdAt,desc
# https://api2.paixin.com/albums/16/medias?page=1&size=45&sort=createdAt,desc
# https://api2.paixin.com/albums/16/medias?page=2&size=45&sort=createdAt,desc
# https://api2.paixin.com/albums/16/medias?page=21&size=45&sort=createdAt,desc   真实的请求


# 图片保存的路径
path = "E:\\pic\\"

# http请求头，防止反爬虫
refer = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36',
}

# 一共 22 页
page = 0  # 页码

for i in range (0, 22):
    base_url = "https://api2.paixin.com/albums/16/medias?page={}&size=45&sort=createdAt,desc".format(page)
    response = requests.get(base_url, headers=refer)
    # print(response.text)
    content = json.loads(response.text)
    # print(type(content))
    # 循环遍历
    #
    size = content["size"]
    dir = content["page"] + 1
    print(str(dir)+"   dir")
    if (os.path.exists(path + str(dir))):
        print('目录已存在')
        flag = 1
    else:
        os.makedirs(path + str(dir))
        flag = 0
    os.chdir(path + str(dir))
    if (flag == 1 and len(os.listdir(path + str(dir))) >= int(size)):
        print('已经保存完毕，跳过')
        page +=1
        continue
    lists = content['elements']
    # # 保存图片
    for con in lists:
        img_url = con["image"]
        print(img_url)
        # 解析一个文件名出来
        file_name = img_url.split(r'/')[-2] + "-" + img_url.split(r'/')[-1]
        try:
            pic = requests.get("http:" + img_url, headers=refer)
        except:
            print("发生错误,将跳过")
            pass
        # 保存结果
        f = open(file_name, 'wb')
        f.write(pic.content)
        f.close()
print("保存结束")
























