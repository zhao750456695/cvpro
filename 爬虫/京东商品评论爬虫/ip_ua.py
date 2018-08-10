# UA代理池和IP代理池结合使用
import urllib.request
import re
import random

def ip_ua(myurl, header=None,ip=False):
    uaplools = [
                'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
                'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
                'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
                'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
                'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
                ]
    thisua = random.choice(uaplools)
    print(thisua)
    headers = ('User-Agent', thisua)
    def ip(uapools):  
	# 使用大象代理平台的ip
        thisip = urllib.request.urlopen('http://tvp.daxiangdaili.com/ip/?tid=558442568021626&num=1').read().decode('utf-8')
        thisip = '127.0.0.1:8888'
        print('当前用的ip是：'+thisip)
        proxy = urllib.request.ProxyHandler({'http':thisip})
        opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler)
        headers =[headers]
	if header != None:
	    for k, v in header.items:
                headers.append((k, v))	    
	opener.addheaders = headers
        urllib.request.install_opener(opener)

    for i in range(2,23):
        try:
            url = myurl
            if ip=True:
                ip(uaplools)
            data = urllib.request.urlopen(url).read()
            data1 = data.decode('utf-8', 'ignore')
            print(len(data1))
            break
        except Exception as err:
            print(err)
    return data1

