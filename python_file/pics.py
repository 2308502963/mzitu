# -*- coding: utf-8 -*-
#爬取网络图片并保存到电脑上
import requests
import os
url="http://tieba.baidu.com/photo/p?kw=%E4%B8%9D%E8%B7%AF%E7%90%B4%E8%A1%8C&ie=utf-8&flux=1&tid=4153410689&pic_id=b09955a1cd11728b0b6c9cc1cefcc3cec2fd2c2d&pn=1&fp=2&see_lz=1"
root="E://pydownload//"
path=root+url.split('/')[-1]
if not os.path.exists(root):
    ps.mkdir(root)
if not os.path.exists(path):
    r=requests.get(url)
    with open(path,'wb') as f:
        f.write(r.content)
        f.close()
        print("文件保存成功")
else:
    print("文件已经存在")
