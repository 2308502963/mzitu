# _*_ coding: utf-8 _*_
# @Time : 2019/12/12 15:15
# @Author : moran office
# File : 360pic.py
# Software : PyChram

# import requests
# import time
# from bs4 import BeautifulSoup
#
# url = 'https://image.so.com/z?ch=beauty'
#
# header = {
#     'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
#
#
# def update_header(referer):
#     header['Referer'] = '{}'.format(referer)
#
#
# html = requests.get(url, headers=header)
# res = BeautifulSoup(html.text, 'html.parser')
#
# list_a = res.find("div", class_='head-nav-bd').find_all("a")
#
# # 提取url
# for a in list_a:
#     # print(a.get_text(),a['href'].split('beauty')[-1])
#     # 跳转的网页用的是相对路径，而我又不是从主页爬的，所以分割一下url
#     img_url = url + a['href'].split('beauty')[-1]
#     # print(img_url)
#     html1 = requests.get(img_url, headers=header)
#     update_header(img_url)
#     res1 = BeautifulSoup(html1.text, 'html.parser')
    # new_urls = res1.find('div', class_='content').find_all('a', class_='img_link')
    # print(new_urls)
    # 网站的图片是异步加载的，还不会爬


# -*- coding: utf-8 -*-
from json import loads

import scrapy

from urllib.parse import urlencode

class ImageSpider(scrapy.Spider):
    name = 'image'
    allowed_domains = ['image.so.com']

    # 重写Spider中的start_requests方法：指定开始url
    def start_requests(self):
        base_url = 'http://image.so.com/zj?'
        param = {'ch': 'beauty', 'listtype': 'new', 'temp': '1'}
        # 可以根据需要爬取不同数量的图片，此处只爬取60张图片
        for page in range(2):
            param['sn'] = page * 30
            full_url = base_url + urlencode(param)
            yield scrapy.Request(url=full_url, callback=self.parse)

    def parse(self, response):
        # 获取到的内容是json数据
        # 用json.loads(）解析数据
        # 此处的response没有content
        model_dict = loads(response.text)
        for elem in model_dict['list']:
            item = BeautyItem()
            item['title'] = elem['group_title']
            item['tag'] = elem['tag']
            item['height'] = elem['cover_width']
            item['width'] = elem['cover_height']
            item['url'] = elem['qhimg_url']
            yield item


import scrapy


class BeautyItem(scrapy.Item):
    title = scrapy.Field()
    tag = scrapy.Field()
    height = scrapy.Field()
    width = scrapy.Field()
    url = scrapy.Field()

# -*- coding: utf-8 -*-

import logging
import pymongo
import scrapy

from scrapy.exceptions import DropItem
from scrapy.pipelines.images import ImagesPipeline

logger = logging.getLogger('SaveImagePipeline')


# 继承ImagesPipenine类，这是图片管道
class SaveImagePipeline(ImagesPipeline):
    """
    下载图片
    """
    def get_media_requests(self, item, info):
        # 此方法获取的是requests 所以用yield 不要return
        yield scrapy.Request(url=item['url'])

    def item_completed(self, results, item, info):
        """
        文件下载完成之后，返回一个列表 results
        列表中是一个元组，第一个值是布尔值，请求成功会失败，第二个值的下载到的资源
        """
        if not results[0][0]:
            # 如果下载失败，就抛出异常，并丢弃这个item
            # 被丢弃的item将不会被之后的pipeline组件所处理
            raise DropItem('下载失败')
        # 打印日志
        logger.debug('下载图片成功')
        return item

    def file_path(self, request, response=None, info=None):
        """
        返回文件名
        """
        return request.url.split('/')[-1]


class SaveToMongoPipeline(object):
    """
    保存图片信息到数据库
    """
    def __init__(self, mongodb_server, mongodb_port, mongodb_db, mongodb_collection):
        self.mongodb_server = mongodb_server
        self.mongodb_port = mongodb_port
        self.mongodb_db = mongodb_db
        self.mongodb_collection = mongodb_collection

    def open_spider(self, spider):
        # 当spider被开启时，这个方法被调用
        self.connection = pymongo.MongoClient(self.mongodb_server, self.mongodb_port)
        db = self.connection[self.mongodb_db]
        self.collection = db[self.mongodb_collection]

    def close_spider(self, spider):
        # 当spider被关闭时，这个方法被调用。
        self.connection.close()

    # 依赖注入
    @classmethod
    def from_crawler(cls, crawler):
        # cls() 会调用初始化方法
        return cls(crawler.settings.get('MONGODB_SERVER'),
                   crawler.settings.get('MONGODB_PORT'),
                   crawler.settings.get('MONGODB_DB'),
                   crawler.settings.get('MONGODB_COLLECTION'))

    def process_item(self, item, spider):
        post = {'title': item['title'], 'tag': item['tag'],
                'width': item['width'], 'height': item['height'], 'url': item['url']}
        self.collection.insert_one(post)
        return item
BOT_NAME = 'image360'

SPIDER_MODULES = ['image360.spiders']
NEWSPIDER_MODULE = 'image360.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/67.0.3396.79 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 1

# 随机延迟，设定随机延迟，使爬虫更像浏览器的行为
RANDOMIZE_DOWNLOAD_DELAY = True
# 延迟时间
DOWNLOAD_DELAY = 3

# 数据库信息
MONGODB_SERVER = '服务器地址'
MONGODB_PORT = 27017
MONGODB_DB = 'image360'
MONGODB_COLLECTION = 'image'

# 日志
LOG_LEVEL = 'DEBUG'

# 数字越小越先执行
ITEM_PIPELINES = {
    'SaveImagePipeline': 300,
    'SaveToMongoPipeline': 330,
}

# 配置图片保存地址，会自动创建文件夹
IMAGES_STORE = './resources'


