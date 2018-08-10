# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnclassItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 设置课程名称，学生数量，课程价格，课时数
    class_name = scrapy.Field()
    student_num = scrapy.Field()
    class_price = scrapy.Field()
    class_time = scrapy.Field()
