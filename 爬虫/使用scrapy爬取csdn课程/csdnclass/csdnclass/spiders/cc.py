# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy.http import Request, FormRequest
from csdnclass.items import CsdnclassItem
import time
class CcSpider(scrapy.Spider):
    name = 'cc'
    allowed_domains = ['csdn.net']
    start_urls = ['http://csdn.net/']
    allurl=[]
    print('>>>>>>请耐心等待，着急也没用>>>>>>')
    # csdn课程一共有227页，根据课程页规律构建链接
    for i in range(1, 228):
        thisurl = 'http://edu.csdn.net/courses/p' + str(i)
        allurl.append(thisurl)
    def parse(self, response):
        while True:
            for m in range(0, len(self.allurl)):
                yield Request(self.allurl[m], callback=self.next)
            time.sleep(3)


    def next(self,response):
        # 获取课程详情页的链接，并进行访问
        link = response.xpath('//dd/a[@target="_blank"]/@href').extract()
        for i in range(0, len(link)):
             yield Request(link[i], callback=self.next2, dont_filter=True)


    def next2(self,response):
        item = CsdnclassItem()
        data = response.body.decode('utf-8')
        # 用正则爬取课程名字
        pat = '<div class="info_right.*?target="_blank">(.*?)</a>'
        item['class_name'] = re.compile(pat,re.S).findall(data)
        #item['class_name'] = response.xpath('//div[@id="course_detail_block1"]/div/h1/a/text()').extract()  # 解压
        item['student_num'] = response.xpath('//span[@ class="num"]/text()').extract()
        # normalize-space方法去除价格空格
        item['class_price'] = response.xpath('normalize-space(//sapn[@class="money"]/text())').extract()
        item['class_time'] = response.xpath('//span[@class="pinfo"]/text()').extract()
        yield item
