# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/4 17:27'
import urllib.request
from lxml import etree
data=urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8', 'ignore')
# 将html转为树类型的数据
treedata=etree.HTML(data)
title=treedata.xpath('//title/text()')
print(title)