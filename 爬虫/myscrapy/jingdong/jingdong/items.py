# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JingdongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    channel_num=scrapy.Field()
    # 频道1
    channel1=scrapy.Field()
    # 频道2
    channel2=scrapy.Field()
    # 图书名
    name=scrapy.Field()
    # 价格
    price=scrapy.Field()
    #  评论数
    comment_num=scrapy.Field()
    # 作者
    author=scrapy.Field()
    # 出版社
    pub=scrapy.Field()
    # 销售方
    seller=scrapy.Field()



