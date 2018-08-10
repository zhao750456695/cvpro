# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest
import urllib.request
import os

class D1Spider(scrapy.Spider):
    name = 'd1'
    allowed_domains = ['douban.com']
    #start_urls = ['http://douban.com/']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'}
    def start_requests(self):
        # 首先爬一次登录页，然后进入回调函数parse()
        return [Request('https://accounts.douban.com/login', meta={'cookiejar': 1}, callback=self.parse,headers=self.header)] # 先进行Request请求，请求之后会找所设置的回调函数，执行回调函数里的内容，下面parse里的response参数就是返回的信息
    def parse(self, response):
        # 判断是否有验证码
        captcha=response.xpath('//img[@id="captcha_image"]/@src').extract()
        # 设置要传递的post信息，此时没有验证码字段
        print(response.xpath('/html/head/title/text()').extract())
        if(len(captcha)>0):
            print('此时有验证码')
            localpath='./captcha.png'
            urllib.request.urlretrieve(captcha[0],filename=localpath)
            #captcha_value=input('请输入验证码')
            cmd='python E:\Python调用示例\YDMPython3.x.py'
            r=os.popen(cmd) # 执行cmd命令
            captcha_value=str(r.read()) # 读取命令执行结果
            print(captcha_value)
            print('验证码识别结果为:'+captcha_value)
            data = {
                'redir': 'https://www.douban.com/',
                'form_email': 'zhao750456695@163.com',
                'form_password': 'zhaojie123',
                'captcha-solution': captcha_value
            }
        else:
            data = {
                'redir': 'https://www.douban.com/',
                'form_email': 'zhao750456695@163.com',
                'form_password': 'zhaojie123'
            }
        print('登录中')
        # 通过FormRequest.from_response()进行登录
        return  [FormRequest.from_response(response,
                                           # 设置cookie信息
                                           meta={'cookiejar': response.meta['cookiejar']},
                                           headers=self.header,
                                           formdata=data,
                                           callback=self.next,
                                           )]

    def next(self, response):
        # 回调传过来的response，是登录成功后的页面
        # response.body获取所有信息 字符串形式

        print(response.xpath('/html/head/title/text()').extract())
    #     yield Request('http://edu.iqianyue.com/index_user_index', callback=self.next2, meta={'cookiejar': True})# 保持登录状态
    #
    # def next2(self, response):
    #     # 回调传来的页面，是个人中心的页面
    #     data=response.body
    #     fh=open('./b.html', 'wb')
    #     fh.write(data)
    #     fh.close()
    #     print(response.xpath('/html/head/title/text()').extract())
