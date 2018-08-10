# -*- coding: utf-8 -*-
import scrapy
from baidunews.items import BaidunewsItem
from scrapy.http import Request
import re
class N1Spider(scrapy.Spider):
    name = 'n1'
    allowed_domains = ['baidu.com']
    start_urls = ['http://news.baidu.com/widget?id=LocalNews&ajax=json']
    allid=['LocalNews', 'civilnews', 'InternationalNews', 'EnterNews', 'SportNews', 'FinanceNews', 'TechNews', 'MilitaryNews', 'InternetNews', 'DiscoveryNews', 'LadyNews', 'HealthNews', 'PicWall']
    allurl = []
    for k in range(0, len(allid)):
        thisurl =  'http://news.baidu.com/widget?id='+allid[k]+'&ajax=json'
        allurl.append(thisurl)

    def parse(self, response):
        for m in range(0, len(self.allurl)):
            print('第' + str(m) + '个栏目')
            yield Request(self.allurl[m], callback=self.next)

    def next(self, response):
        data=response.body.decode('utf-8', 'ignore')
        pat1='"m_relate_url":"(.*?)"'
        pat2='"url":"(.*?)"'
        url1 = re.compile(pat1, re.S).findall(data)
        url2 = re.compile(pat2, re.S).findall(data)
        if(len(url1)!=0):
            url=url1
        else:
            url=url2
        for i in range(0, len(url)):
            thisurl = re.sub('\\\/', '/', url[i])
            print(thisurl)

    def next2(self, response):
        item = BaidunewsItem()
        item['link']=response.url
        item['title']=response.xapth('/heml/head/title/text()')
        item['content']=response.body

