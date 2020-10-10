# _*_ coding: utf-8 _*_
# @Time : 2020/10/9 15:43
# @Author : moran office
# File : wangzhe.py
# Software : PyChram

# https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?
# activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&'page=1'&iOrder=0&iSortNumClose=1
# &jsoncallback='jQuery17101511393952981157_1602231917132'&iAMSActivityId=51991&_everyRead=true&iTypeId=2
# &iFlowId=267733&iActId=2735&iModuleId=2735&_='1602232102683'

# https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?
# activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&'page=0'&iOrder=0&iSortNumClose=1
# &jsoncallback=&iAMSActivityId=51991&_everyRead=true&iTypeId=2
# &iFlowId=267733&iActId=2735&iModuleId=2735

import requests
import json
import os
import html
refer = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 '
                  'Safari/537.36',
}

path = "E:\\wangzhe\\"

page = 0  # 一共23页

for j in range(24):
    base_url = "https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?sDataType=JSON&page={}&iActId=2735".format(page + j)
    response = requests.get(base_url, headers= refer)
    response.encoding = 'utf-8'
    # print(response.text)
    # response.encoding = response.apparent_encoding


    # 数据对象
    json_obj = json.loads(response.text)
    print(json_obj)
    # break
    if json_obj["iBltFlag"] != "0":  # 请求失败
        continue
    data_list = json_obj["List"]
    for data in data_list:
        file_name = data["sProdName"]  # 拿到文件名
        print("文件名"+file_name)
        if (os.path.exists(path + file_name)):
            print('目录已存在')
            flag = 1
        else:
            os.makedirs(path + file_name)
            flag = 0
        os.chdir(path + file_name)  # cd 进文件夹
        if (flag == 1 and len(os.listdir(path + file_name)) >= int(8)):
            print('已经保存完毕，跳过')
            continue
        # 获取图片地址
        for i in range(8):
            prefix = "sProdImgNo_{}".format(i+1)
            url = data[prefix]
            url = url.replace("%3A", ":")
            url = url.replace("%2F", "/")
            url = url.replace("%2E", ".")
            url = url.replace("%5F", "_")
            url = url.replace("/200", "/0")
            print(url)
            img_name = url.split('/')[-2]
            try:
                pic = requests.get(url)
                f = open(img_name, 'wb')
                f.write(pic.content)
                f.close()
            except:
                print("发生错误,将跳过")
                pass
            # 保存结果
        print("单个英雄保存结束")

    print("单页保存结束")


# http://shp.qpic.cn/ishow/2735122815/1545981285_-888937974_30782_sProdImgNo_6.jpg/0  1920*1080
# http://shp.qpic.cn/ishow/2735122815/1545981285_-888937974_30782_sProdImgNo_6.jpg/200

# http://shp.qpic.cn/ishow/2735122815/1545981192_-888937974_23607_sProdImgNo_6.jpg/0
# http://shp.qpic.cn/ishow/2735122815/1545981192_-888937974_23607_sProdImgNo_6.jpg/200





