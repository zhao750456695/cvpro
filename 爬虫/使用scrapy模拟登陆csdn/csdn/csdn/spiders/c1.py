# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request,FormRequest
import urllib.request
import ssl
import os
from selenium import webdriver
ssl._create_default_https_context = ssl._create_unverified_context


class C1Spider(scrapy.Spider):
    name = 'c1'
    allowed_domains = ['csdn.net']
    # start_urls = ['http://csdn.net/']
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'}

    # 编写start_requests()方法，第一次会默认调取该方法中的请求


    def start_requests(self):
        # 首先爬一次登录页，然后进入回调函数parse（）

        return [Request("https://passport.csdn.net/", meta={"cookiejar": 1}, callback=self.parse)]

    def parse(self, response):
        lt = response.xpath('//input[@name="lt"]/@value').extract()[0]
        execution = response.xpath('//input[@name="execution"]/@value').extract()[0]
        captcha = response.xpath('//input[@id="validateCode"]/@placeholder').extract()
        # 判断是否有验证码
        """
        用selenium通过浏览器进行截屏，手工输入验证码。
        """
        if len(captcha) > 0:
            print('此时有验证码')
            # 打开火狐浏览器
            browser = webdriver.Firefox()
            url = "https://passport.csdn.net/account/login?from=http://edu.csdn.net/mycollege"
            browser.set_window_size(1200, 900)
            browser.get(url)
            # 保存截屏到本地
            browser.save_screenshot("./codingpy.png")
            browser.close()
            captcha_value = input('请在当前目录查看并输入验证码：')
            print("当前验证码为：" + captcha_value)
            data = {
                'lt': lt,
                'execution': execution,
                '_eventId': 'submit',
                'validateCode': captcha_value,
                'username': 'zhao750456695@163.com',
                'password': '322621'
            }
        else:
            # 设置要传递的post信息，此时没有验证码字段
            data = {
                'lt': lt,
                'execution': execution,
                '_eventId': 'submit',
                'username': 'zhao750456695@163.com',
                'password': '322621'
                       }
            print('登陆中...')
            # 通过FormRequest.from_response()
            return [FormRequest.from_response(response,
                                              # 设置cookie信息
                                              meta={'cookiejar': response.meta['cookiejar']},
                                              # 设置headers信息模拟成浏览器
                                              headers=self.header,
                                              # 设置post表单中的数据
                                              formdata=data,
                                              # 设置回调函数，此时回调函数为next()
                                              callback=self.next
                                              )]

    def next(self, response):

        yield Request('http://my.csdn.net', callback=self.next2, meta={'cookiejar': True})

    def next2(self,response):
        # 设置文件路径
        file_path = './mycsdn.html'
        data = response.body.decode('utf-8')
        # 获取标题
        title = response.xpath('/html/head/title/text()').extract()[0]
        # 根据标题判断是否登陆成功
        if title == '我的CSDN':
            print('>>>>>>>>>>>>>终于等到你，登陆成功>>>>>>>>>>>>>>>')
            with open(file_path, 'w', encoding='utf-8', errors='ignore') as f:
                f.write(data)
        else:
            print(">>>>>>>>>>>呵呵，登陆没成功呢>>>>>>>>>>>>>>>>>>>>")
        print(response.xpath('/html/head/title/text()').extract())