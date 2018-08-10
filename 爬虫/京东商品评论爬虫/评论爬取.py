# -*- coding:utf-8 -*-
import urllib.request
import re
from ip_ua import * # import ip_ua 会报错
import ssl
import os
# 全局取消证书验证，否则读取https会报错
ssl._create_default_https_context = ssl._create_unverified_context
data_path = "./jd"
if not os.path.exists(data_path):
    os.makedirs(data_path)

for i in range(1,50):
    url = 'https://search.jd.com/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&page=' + str(i) + '&scrolling=y'
    data = ip_ua(url)
    url_pat= 'data-spu="(.*?)"'
    rst = re.compile(url_pat).findall(data)
    for item in rst:
        fh = open(data_path +'/'+ item + '评论.txt', 'a')

        myurl = 'https://item.jd.com/'+item+'.html'

        data = urllib.request.urlopen(myurl).read()
        data1 = data.decode('gbk', 'ignore')
        c_pat = '<div class="comment-content">(.*?)</div></div>'
        nn_pat = '<title>(.*?)</title>'
        rst555 = re.compile(nn_pat).findall(data1)
        rst666 = re.compile(c_pat,re.S).findall(data1)
        fh.write(str(rst555))
        fh.write(str(rst666))

        for i in range(1,3):
            hiden_url = 'https://sclub.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv131292&productId='+item+'&score=0&sortType=5&page='+str(i)+'&pageSize=10&isShadowSku=0&rid=0&fold=1'
            h_pat = '"content":"(.*?)\W.*?"'
            data2 = urllib.request.urlopen(hiden_url).read()
            data3 = data2.decode('gbk', 'ignore')

            rst888 = re.compile(h_pat).findall(data3)
            fh.write(str(rst888))
            print(str(rst888))

    fh.close()