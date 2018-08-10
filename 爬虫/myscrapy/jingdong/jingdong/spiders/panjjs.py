# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/5 20:17'
import time
from selenium import webdriver

browser=webdriver.PhantomJS() # phantomjs的接口 生成一个对象
browser.get('http://www.baidu.com') # get访问
a=browser.get_screenshot_as_file('./test.jpg') # 截屏
# browser.find_element_by_xpath('//*[@id="kw"]').clear() # 通过xpath找到输入框 清除一下
# browser.find_element_by_xpath('//*[@id="kw"]').send_keys('爬虫') # send_keys 输入数据
# browser.find_element_by_xpath('//*[@id="su"]').click() # 找到搜索点击按钮
# time.sleep(5)
# a=browser.get_screenshot_as_file('./test.jpg')
data=browser.page_source # 找到网页源码
browser.quit()
print(len(data))
import re
title=re.compile('<title>(.*?)</title>').findall(data)
print(title)
print(data)