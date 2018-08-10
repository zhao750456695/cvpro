# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/5 19:37'
from bs4 import BeautifulSoup as bs
import urllib.request
import random
ua = [
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
    'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
    'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
    'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
]
url = 'http://edu.iqianyue.com'

req2 = urllib.request.Request(url)
req2.add_header('User-Agent', random.choice(ua))
data = urllib.request.urlopen(req2).read().decode('utf-8', 'ignore')
print(data)
bs1=bs(data)
# # 获取标签 bs对象.标签名
bs1.title
print(bs1.title)

# # 获取标签里面的文字：bs对象.标签名.string
bs1.title.string
print(bs1.title.string)
# # 获取标签名：bs对象.标签名.name
bs1.title.name
print(bs1.title.name)
# # 获取属性列表：bs对象.标签名.attr
print(bs1.title.attrs)
# # 获取某个属性对应的值：bs对象.标签名[属性名]或者bs对象.标签名.get(属性名)
print(bs1.a["class"])
print(bs1.a.get("class"))
# # 提取所有某个节点的内容：bs对象.findall('标签名') bs对象.find_all(['标签名1'， ’标签名2'])
print(bs1.find_all('a'))
print(bs1.find_all(['a', 'ul']))
# # 提取所有子节点：bs对象.标签.contents bs对象.标签.children
print(bs1.ul.contents)
# k2=bs1.ul.children
# allulc=[i for i in k2]
