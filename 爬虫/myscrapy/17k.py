# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/6 19:28'
import redis
import urllib.request
import re
#rconn=redis.Redis('', '')


for i in range(0, 1000000000000):
    #isdo=rconn.hget('url', str(i))
    # if isdo!=None:
    #     continue
    #rconn.hset('url', str(i), '1')
    try:
        data=urllib.request.urlopen('http://www.17k.com/book/'+str(i)+'.html').read().decode('utf-8', 'ignore')

    except Exception as err:
        print(str(i)+str(err))
        continue
    pat='<a class="red".*?>(.*?)</a>'
    rst=re.compile(pat).findall(data)
    if len(rst)==0:
        continue
    print(rst)
    name=rst[0]
    #rconn.hset('rst', str(i), str(name))


