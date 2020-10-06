# _*_ coding: utf-8 _*_
# @Time : 2020/2/1 12:43
# @Author : moran office
# File : qq.py
# Software : PyChram

import requests
import re
from selenium import webdriver

# song = input("想要下载的歌曲:")
url = f'https://music.163.com/#/search/m/?s=猎户星座&type=1'  # 只搜索歌曲

driver = webdriver.Chrome("D:\ChromeCore\chromedriver.exe")
driver.get(url)

driver.switch_to.frame("g_iframe")

res = driver.find_elements_by_id("m-search")
