import urllib.request
import re
import pymysql
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="webclass")

def getdata(pdnum,classtype,detail):
    #获取当前频道所有作品
    allnovels=[]
    for i in range(0,25):
        try:
            thispage=urllib.request.urlopen("http://www.itangyuan.com/category/"+pdnum+"_"+str(i)+".html").read().decode("utf-8","ignore")
            pat1='<span class="bname".*?<a href="/book/(.*?).html">'
            novelid=re.compile(pat1,re.S).findall(thispage)
            for j in novelid:
                allnovels.append(j)
        except Exception as err:
            print(err)
    #获取每部作品中的文章
    allarticles=[]
    for i in allnovels:
        try:
            thisurl="http://www.itangyuan.com/book/"+str(i)+".html"
            thispage=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
            pat1='id="chapter_.*?_url" href="/book/chapter/(.*?).html"'
            aid=re.compile(pat1,re.S).findall(thispage)
            for j in aid:
                allarticles.append(j)
        except Exception as err:
            print(err)
    #获取每篇文章的内容
    for i in allarticles:
        try:
            thisurl="http://www.itangyuan.com/book/chapter/"+i+".html"
            thispage=urllib.request.urlopen(thisurl).read().decode("utf-8","ignore")
            pat1='<div class="section-main-con" data-name="section-con">(.*?) <p class="end">'
            content=re.compile(pat1,re.S).findall(thispage)
            pat2='<a class="book-name" href="/book/.*?.html">(.*?)</a>'
            title=re.compile(pat2,re.S).findall(thispage)
            if(len(content)==0):
                continue
            else:
                content=content[0]
            if(len(title)==0):
                continue
            else:
                title=title[0]
            sql="insert into traindata1(content,title,classtype,detail) values('"+str(content)+"','"+str(title)+"','"+str(classtype)+"','"+str(detail)+"')"
            conn.query(sql)
            conn.commit()
        except Exception as err:
            print(err)

#频道号
pdnum=["girl_4408_0_heat_0","girl_193_0_heat_0","boy_182_0_heat_0","girl_22_0_heat_0"]
detail=["现言","古风","悬疑","灵异"]
classtype=["0","1","2","3"]
allweb=zip(pdnum,detail,classtype)
for i in allweb:
    getdata(i[0],i[2],i[1])
