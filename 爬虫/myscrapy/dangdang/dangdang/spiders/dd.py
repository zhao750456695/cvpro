# -*- coding: utf-8 -*-
import scrapy
from dangdang.items import DangdangItem
from scrapy.http import Request
class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=python&act=input&show=big#J_tab']

    def parse(self, response):
        item=DangdangItem()
        item['title']=response.xpath('//a[@name="itemlist-picture"]/@title').extract()
        item['link']=response.xpath('//a[@name="itemlist-title"]/@href').extract()
        item['comment']=response.xpath('//a[@name="itemlist-review"]/text()').extract()
        # print(item['title'])
        # print(item['link'])
        # print(item['comment'])
        print('返回item')
        m=0
        print(item['title'][0])
        print(m)
        yield item
        for i in range(2, 4):
            url = 'http://search.dangdang.com/?key=python&act=input&show=big&page_index='+str(i)
            print('第'+str(i)+'页')
            m=m+1
            print(m)
            print('yield前')
            yield Request(url, callback=self.parse)
            print('yield后')
        print('for 结束了')