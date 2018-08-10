# -*- coding:utf-8 -*-
"""
项目描述：爬取京东商城零食频道（https://search.jd.com/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&wq=%E9%9B%B6%E9%A3%9F&
pvid=ss7fo4wi.ri9kq2）商品的商品名、商品价格、商品出售方、商品评论数等信息爬下来，存储到一个文件中，爬30-50页就行。
文件存放要求：
商品常规项信息全部存储到一个文件中，每行为一个商品的信息，形如：
{“商品名”：XXXXX，“商品价格‘：XXXX，……}
{“商品名”：XXXXX，“商品价格‘：XXXX，……}
……
"""
import urllib.request
import re
from ip_ua import *# 若写成import ip_ua下面ip_ua()会报错，最好自定义包不要和函数重名
import ssl
# 全局取消证书验证，否则读取https会报错
ssl._create_default_https_context = ssl._create_unverified_context
# =====
with open('./jd.txt', 'w') as txt:
    for i in range(1,100):
        url = 'https://search.jd.com/Search?keyword=%E9%9B%B6%E9%A3%9F&enc=utf-8&page=' + str(i) + '&scrolling=y'
        data = ip_ua(url)
        # 商品名称列表
        with open('./i.txt', 'w', encoding='utf-8') as f:
            f.write(data)
        pat1 = '<div class="p-name p-name-type-2">.*?<em>(.*?)</em>'
        rst = re.compile(pat1, re.S).findall(data)
        rst1 = []  # 不能放在for循环内
        for item in rst:
            pat2 = '<span.*?>'
            pat3 = '<font.*?>'
            pat4 = '<img.*?>'
            rep = '</span>'
            rep2 = '</font>'
            pat2 = re.compile(pat2)
            pat3 = re.compile(pat3)
            pat4 = re.compile(pat4)
            item = re.sub(pat2, '', item)
            item = re.sub(pat3, '', item)
            item = re.sub(pat4, '', item)
            item = item.replace(rep, '')
            item = item.replace(rep2, '')
            # print(item)
            rst1.append(item)  # 不能写成rst1=rst1.append(item)
        print('正在爬取第'+str(i)+'页商品名称')
        # 商品价格列表
        price_pat = '<em>￥</em><i>(.*?)</i>'
        rst2 = re.compile(price_pat).findall(data)
        print('正在爬取第'+str(i)+'页价格')
        # 商品评价列表
        c_pat = '">(.*?)</a>条评价</strong>'
        rst3 = re.compile(c_pat).findall(data)
        print('正在爬取第'+str(i)+'页评价')
        # 店铺列表
        shop_pat = '<div class="p-shop".*?<span class="J_im_icon"><a target="_blank" class=".*?" onclick=".*?" href=".*?" title=".*?">(.*?)</a></span>'
        rst4 = re.compile(shop_pat, re.S).findall(data)
        print('正在爬取第'+str(i)+'页卖家')

        # 将商品名称、价格、评论、店铺组合起来
        for i in range(0, len(rst4)):
            f = '商品名称' + ':' + rst1[i] + ' ' + '商品价格' + ':' + rst2[i] + ' ' + '商品评价' + ':' + rst3[
                    i] + ' ' + '卖家' + ':' + rst4[i] + '\r\n'
            txt.write(f)

# ===================================================评论爬取==========================================================
"""
商品的评论项单独存储到一个文件夹中，每一个商品的所有评论存储到一个文件中，每个评论占一行。
comment/
          XXXXXX01.txt
         XXXXXX02.txt
"""
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