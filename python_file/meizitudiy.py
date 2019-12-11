# -*- coding: UTF-8 -*-
# @Time : 2019/5/11 16:44 
# @Author : 墨染
# @Site :  
# @File : meizitudiy.py 
# @Software: PyCharm

import requests
import os
from bs4 import BeautifulSoup
import os
from io import BytesIO
import time
from PIL import Image

def update_header(referer):
    headers['Referer'] = '{}'.format(referer)

headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
url="http://www.mzitu.com/all"
r=requests.get(url, headers=headers)
path="./photo"
if not os.path.exists(path):
    os.makedirs(path)

#print(r.text)
soup = BeautifulSoup(r.text, "html.parser")

a_list = soup.find('div', class_="all").find_all('a')
a_list.pop(0)
#print(a_list)
for a in a_list:
    title = a.get_text()# 取出a标签的文本
    href = a['href']  # 取出a标签的href 属性
    html = requests.get(href, headers=headers)
    #print(html.text)
    html_Soup = BeautifulSoup(html.text, 'lxml')
    max_span = html_Soup.find('div', class_='pagenavi').find_all('span')[-2].get_text()  ##查找所有的<span>标签获取第十个的<span>标签中的文本也就是最后一个页面了
    for page in range(1, int(max_span) + 1):
       page_url = href + '/' + str(page)
       #print(page_url)  ##这个page_url就是每张图片的页面地址啦！但还不是实际地址！
       img_html = requests.get(page_url, headers=headers)
       img_Soup = BeautifulSoup(img_html.text, 'lxml')
       img_url = img_Soup.find('div', class_='main-image').find('img')['src']
       print(img_url)
       img = requests.get(img_url, headers=headers)
       name = img_url.split('/')[-1]  ##取URL 倒数第四至第九位 做图片的名字
       update_header(img_url)
       print(name)
       # image = Image.open(BytesIO(img.content))    #??
       # #print(image.format)
       # image.save(name, 'jpeg')  #??????2
       # time.sleep(1)
       with open("E:\\meizi"+'/'+name, mode="wb") as file:
           file.write(img.content)

