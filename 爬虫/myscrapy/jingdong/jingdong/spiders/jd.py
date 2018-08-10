# -*- coding: utf-8 -*-
import scrapy
import urllib.request
import re
import random
from jingdong.items import JingdongItem
from lxml import etree
from scrapy.http import Request
import ssl


# 全局取消证书验证，否则读取https会报错
ssl._create_default_https_context = ssl._create_unverified_context
class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com']
    #start_urls = ['http://jd.com/']
    def start_requests(self):
        ua=[
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
                'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
                'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
                ]
        urls = ['https://channel.jd.com/p_wenxuezongheguan.html']
        catall=[]
        for url in urls:
            req2 = urllib.request.Request(url)
            req2.add_header('User-Agent', random.choice(ua))
            pddata=urllib.request.urlopen(req2).read().decode('gbk', 'ignore')
            pat2='href="..list.jd.com.list.html.cat=([0-9,]*?)[&"]'
            catdata=re.compile(pat2).findall(pddata)
            for j in catdata:
                catall.append(j)
        catall2=set(catall)
        print(catall2)
        # 获得页数
        allpage=[]
        x=0
        for m in catall2:
            thispdnum=m
            url='https://list.jd.com/list.html?cat='+thispdnum
            req3 = urllib.request.Request(url)
            req3.add_header('User-Agent', random.choice(ua))
            listdata = urllib.request.urlopen(req3).read().decode('gbk', 'ignore')
            pat3='<em>共<b>(.*?)</b>页'
            page=re.compile(pat3).findall(listdata)
            if len(page)>0:
                pass
            else:
                page=[1]
            allpage.append({thispdnum:page[0]})
            if x>2:
                break
            x+=1
        x=0
        for n in catall2:
            thispage=allpage[x][n]
            for p in range(1, int(thispage)+1):
                thispageurl= 'https://list.jd.com/list.html?cat='+str(n)+'&page='+str(p)
                print(thispageurl)
                yield Request(thispageurl, callback=self.parse)
            x+=1
    def parse(self, response):
        item=JingdongItem()
        listdata=response.body.decode('utf-8', 'ignore')
        # 频道1/2
        pd=response.xpath('//span[@class="curr"]/text()').extract()
        if len(pd)==0:
            pd=['缺省', '缺省']
        if len(pd)==1:
            pda=pd[0]
            pd=[pda, '缺省']
        pd1=pd[0]
        pd2=pd[1]
        # 图书名
        bookname=response.xpath('//div[@class="p-name"]/a/em/text()').extract()
        #print(bookname)
        # 价格
        allskupat='<a data-sku="(.*?)"'
        allsku=re.compile(allskupat).findall(listdata)
        #print(allsku)
        # 评论数

        # 作者的信息
        author=response.xpath('//span[@class="author_type_1"]/a/@title').extract()
        # 出版社的信息
        pub=response.xpath('//span[@class="p-bi-store"]/a/@title').extract()
        # 店家
        seller=response.xpath('//span[@class="curr-shop"]/text()').extract()
        # 处理当前页的数据
        for n in range(0, len(seller)):
            name=bookname[n+3]
            thissku=allsku[n]
            priceurl='https://p.3.cn/prices/mgets?callback=jQuery7839616&type=1&skuIds=J_'+str(thissku)
            pricedata=urllib.request.urlopen(priceurl).read().decode('utf-8', 'ignore')
            pricepat='"p":"(.*?)"'
            price=re.compile(pricepat).findall(pricedata)[0]

            commenturl = 'https://club.jd.com/comment/productCommentSummaries.action?my=pinglun&referenceIds=' + str(thissku)+'&callback=jQuery8841347'
            commentdata = urllib.request.urlopen(commenturl).read().decode('utf-8', 'ignore')
            commentpat = '"CommentCount":(.*?),'
            commentnum = re.compile(commentpat).findall(commentdata)[0]
            thisauthor=author[n]
            thispub=pub[n]
            thisseller=seller[n]
            print(pd1)
            print(pd2)
            print(name)
            print(price)
            print(commentnum)
            print(thisauthor)
            print(thispub)
            print(thisseller)
            item['channel1']=pd1
            item['channel2']=pd2
            item['name']=bookname
            item['comment_num']=commentnum
            item['author'] = thisauthor
            item['pub'] = thispub
            item['seller'] = thisseller
            yield item






