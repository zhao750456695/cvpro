import requests
import re
import random
# 关闭取消SSL验证的警告
requests.packages.urllib3.disable_warnings()

# 代理池
uapools = [
        'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
        'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
        'Mozilla/5.0(Macintosh;U;IntelMacOSX10_6_8;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50'
        'Mozilla/5.0(Windows;U;WindowsNT6.1;en-us)AppleWebKit/534.50(KHTML,likeGecko)Version/5.1Safari/534.50',
        'Opera/9.80(Macintosh;IntelMacOSX10.6.8;U;en)Presto/2.8.131Version/11.11',
        'Mozilla/5.0(WindowsNT6.1;rv:2.0.1)Gecko/20100101Firefox/4.0.1'
    ]
# 构造头
headers={
    'User-Agent': random.choice(uapools),
}
# 扶摇 腾讯视频深度解读抓取
# 经过抓包分析得到下面链接
# https://video.coral.qq.com/filmreviewr/c/upcomment/639agzdh10yu2q2?&reqnum=3
# https://video.coral.qq.com/filmreviewr/c/upcomment/639agzdh10yu2q2?&reqnum=3&commentid=6414840928427831839
# https://video.coral.qq.com/filmreviewr/c/upcomment/639agzdh10yu2q2?&reqnum=3&commentid=6414844123338895494
"""
上面三条url是点击 查看更多解读 抓到的三个url，每条url下会显示三条解读
分析url，发现639agzdh10yu2q2是视频的id，reqnum=3是请求的评论的数量
commentid=6414840928427831839是评论的id
下面是第一个url页面开始的几行
{"errCode":0,"data":{"targetid":2003562847,"display":1,"total":143,"reqnum":3,"retnum":3,"maxid":"6431486847932559482","first":"6415114866625577150","last":"6414840928427831839","hasnext":true,
我们发现第一个url页面的last正是第二个url中的评论id
所以，我们可以通过不断抓取last来构造url

"""
# 第一页
vid = "639agzdh10yu2q2"
url = "https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?&reqnum=3"
f= open('./fuyao.txt','w',encoding='utf-8')
while True:
    try:
        # 关闭验证，否则会报错
        response=requests.get(url, headers=headers,  verify=False)
        data = response.text
        pat_last = '"last":"(.*?)"'
        cid = re.compile(pat_last).findall(data)
        # 当不再有评论id时，结束爬取
        if len(cid)==0:
            break
        title_pat = '"title":"(.*?)","abstract"'
        title = re.compile(title_pat,re.S).findall(data)

        content_pat = '"content":"(.*?)"type"'
        content = re.compile(content_pat, re.S).findall(data)
        i=0
        while i < len(title):

            f.write("=========================================================="+"\n")
            f.write('titel:'+title[i].encode('utf-8').decode('unicode_escape')+"\n")
            f.write('content:'+content[i].encode('utf-8').decode('unicode_escape')+"\n")
            f.write("=========================================================="+"\n")
            i =i +1

        url = "https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?&reqnum=3&commentid="+cid[0]
    except Exception as err:
        print(err)

f.close()

