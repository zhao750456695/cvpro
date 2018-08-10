# -*- coding:utf-8 -*-
import urllib.request
import urllib.parse
import re
import random
from lxml import etree
import ssl
import http.cookiejar
import jsonpath
import json
import redis
import bloom
import pymysql.cursors

# ===== 连接数据库
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="zhihu", charset='utf8', use_unicode=True)
cursor = conn.cursor()

bf = bloom.BloomFilter(0.001, 100000000)

ssl._create_default_https_context = ssl._create_unverified_context

# ===== 设置头信息
ua = [
            'User-Agent:Mozilla/4.0(compatible;MSIE7.0;WindowsNT5.1;TheWorld)'
            'User-Agent:Mozilla/5.0(compatible;MSIE9.0;WindowsNT6.1;Trident/5.0',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36',
            'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'
        ]
thisua = random.choice(ua)
headers = {"User-Agent": thisua}
headers1 = {'Cache-Control': 'max-age=0',
                                    'User-Agent': random.choice(ua),
                                    'Host': 'static.zhihu.com',
                                   'Connection': 'keep-alive',
                                    'Referer': 'https://www.zhihu.com/question/66168407'}
headers2 = {'Origin': 'https://www.zhihu.com',
                                   'Cookie': 'q_c1=f60ed6b773aa4a6ab738f45a4e151796|1512384632000|1512384632000; _zap=565df794-cd99-43fb-b355-fd0dce4e0228; r_cap_id="NWYyMzA3OTc1OTMxNGEyNDhjNDUzZGEzNDAxNDhjOWQ=|1512708961|a8df7eb834727e86165e51e2e97f9e655911f522"; cap_id="YjdkYTQ2YmVhNzNiNDBmZTk1ZTM2ODVhMDc5NmFjMzg=|1512708961|ec153c1d97202b34e0dcad25f04e46368933d9fd"; d_c0="ADCCCAd6ygyPTreiNiQaFu-2RyO0ga9XCD8=|1512526409"; __utma=51854390.1914147487.1512746686.1512799339.1512749032.3; __utmz=51854390.1512799339.2.2.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic; z_c0=Mi4xdmF2RkJnQUFBQUFBTUlJSUIzcktEQmNBQUFCaEFsVk5VbW9YV3dEM1h6d19DUHhmYTNkUVFNUzhTaV9MTk54QTFB|1512709202|82614d2ce989421f722bf15a353ad368ec26e2c7; __utmc=51854390; _xsrf=fe968e9b-713e-4eae-943b-6bdb581278cf; __utmv=51854390.100--|2=registration_date=20171205=1^3=entry_date=20171204=1',
                                   'User-Agent': random.choice(ua),
                                   'Host': 'static.zhihu.com',
                                   'Connection': 'keep-alive',
                                   'Referer': 'https://www.zhihu.com/question/66168407'}
def bopenr(headers):
    opener = urllib.request.build_opener()
    headall = []
    for key, value in headers.items():
        item = (key, value)
        headall.append(item)
    opener.addheaders = headall
    urllib.request.install_opener(opener)


bopenr(headers)

# ========================================第一部分 爬话题广场页面，找到每一大类下所有话题的ID
"""
详细说明：
     通过抓包分析，我们知道话题广场各大类下面的内容是通过post得到，要post是method: next和params: topic_id:大类ID, offset:控制每页显示数量的一个数字, hash_id: "990423d52d7f527ff662f67e6620a96e"，需要得到是大类的ID和offset，offset根据观察是每次增加20.因此只需要得到大类ID。
     同过得每个大类抓包，我们得到所有大类的ID：topicid = [253, 833, 99, 69, 113, 304, 13908, 570, 1761, 988, 388, 285, 686, 444, 1537, 3324, 2955, 4196, 395, 75, 68, 215, 1027, 445, 112, 237, 1740, 1538, 2143, 4217, 2253, 8437, 19800]。
     所有大类公用同一个post地址：https://www.zhihu.com/node/TopicsPlazzaListV2。
     ID与大类的对应：
{253:'游戏', 833:’运动’ , 99:'互联网’, 69:’艺术’, 113:’阅读’,304 :’美食’, 13908:’动漫’, 570:’汽车’, 生活方式:’1761’,教育 :’988’, 388:’摄影’,285 :’历史’,686 :’文化’,444 :’旅行’, 1537:’职业发展’,3324 :’经济学’,2955 :’足球’, 4196:’篮球’, 395:’投资’,75 :’音乐’, 68:’电影’,215 :’法律’, 1027:’自然科学’, 445:’设计’,112 :’创业’, 237:’健康’,1740 :’商业’, 1538:’体育’, 2143:’科技’,4217 :’化学’, 2253:’物理学’,8437 :’生物学’,19800: '金融'}

"""
url = "https://www.zhihu.com/node/TopicsPlazzaListV2"

topicid = [253, 833, 99, 69, 113, 304, 13908, 570, 1761, 988, 388, 285, 686, 444, 1537, 3324, 2955, 4196, 395, 75, 68, 215, 1027, 445, 112, 237, 1740, 1538, 2143, 4217, 2253, 8437, 19800]
# 话题广场ID对应
class_dict = {253: '游戏', 833:'运动', 99: '互联网', 69: '艺术', 113: '阅读', 304: '美食', 13908: '动漫', 570:' 汽车', 1761: '生活方式', 988: '教育', 388: '摄影', 285: '历史', 686: '文化', 444: '旅行', 1537: '职业发展', 3324: '经济学', 2955: '足球', 4196: '篮球', 395: '投资', 75 : '音乐', 68:'电影', 215 :'法律', 1027:'自然科学', 445:'设计', 112: '创业', 237: '健康', 1740: '商业', 1538:'体育', 2143: '科技', 4217: '化学', 2253:'物理学', 8437:'生物学', 19800:'金融'}
for tid in topicid:
    offset = 0
    values = {"method": "next", "params": '{"topic_id":'+ str(tid)+', "offset": ' + str(
        offset) + ', "hash_id": "990423d52d7f527ff662f67e6620a96e"}'}
    # 通过无限循环抓到一个大类下所有话题，直到最终没有话题时break
    while True:
        values = {"method": "next", "params": '{"topic_id":' + str(tid) + ', "offset": ' + str(
            offset) + ', "hash_id": "990423d52d7f527ff662f67e6620a96e"}'}
        try:
            data = urllib.parse.urlencode(values).encode(encoding='UTF8')
            req = urllib.request.Request(url, data)
            res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
        except Exception as err:
            print(err)
        print(res)
        pat = '"msg": \\[(.*?)\\]' # re里的[]要转义
        msg_data = re.compile(pat).findall(res)
        #print(msg_data)
        offset = offset + 20
        #print(len(msg_data))
        data = str(json.loads(res))
        patt = '<strong>(.*?)</strong>'
        pat = 'topic\\\/(.*?)\">'
            # #pat = 'topic(.*?)">'
        topic_id = re.compile(pat).findall(res)
        topic = re.compile(patt).findall(data)
        #print(topic)
        m = len(topic)

        nt = []
        for id in topic_id:
            thisid = re.sub("\\\\", "", id)
            nt.append(thisid)
        topic_id = nt
        #print(topic_id)
        if msg_data[0] == '':
            break
        print(m)
        for i in range(0, m):
            #print(i)
            #sql = "insert into topic(name,tid,class) values('" + topic[i] + "','" + topic_id[i] + "','" + class_dict[tid] + "')"
            sql = 'insert into topic_in(name, tid, class) values( "%s", "%s", "%s")'
            data = (topic[i], topic_id[i], class_dict[tid])
            try:
                print("》》》》》》正在抓取话题、话题id、所属类别，并写入数据库》》》》》》")
                cursor.execute(sql % data)
                conn.commit()
            except Exception as err:
                print(err)

# =============================================================================================
# ================================= 爬取话题的详细页面
        """
        详细分析：
            进入每一个话题的详细页面，进入话题的详细页面先要构造详细页面的url，url都是形如https://www.zhihu.com/topic/话题id/hot的样子，通过上面的函数可以获得话题id。显示更多的话题要进行抓包分析，经过分析又是post请求，其中有个参数offset用来请求下一页，这个offset参数的值正好是上一页data-score的最后一项。
            获得页面后，我们在页面上就可以找到所有问题的网址了。
        """
        for id in topic_id:

                bopenr(headers)
                try:
                    url = "https://www.zhihu.com/topic/" + str(id)+"/hot"
                    req = urllib.request.Request(url)
                    res = urllib.request.urlopen(req).read().decode("utf-8", "ignore")
                except Exception as err:
                    print(err)
                #print(res)
                pat = '<a class="question_link" href="/question/(.*?)"'
                question_id_list1 = re.compile(pat).findall(res)  # 问题ID
                #print('question_id_list1')
                #print(question_id_list1)
                pat = 'data-score="(.*?)"'
                data = re.compile(pat).findall(res)
                m = len(data)

                #print(data)
                offset = data[m - 1]
                while True:
                    bopenr(headers1)
                    topic_post_values = {"start": 0, "offset": offset}
                    try:
                        topic_post_data = urllib.parse.urlencode(topic_post_values).encode(encoding="utf-8")
                        topic_post_req = urllib.request.Request(url, topic_post_data)
                        topic_post_res = urllib.request.urlopen(topic_post_req).read().decode("utf-8", "ignore")
                    except Exception as err:
                        print(err)
                    # 细心，该处的topic_post_req写成了req
                    #print('topic_post_res')
                    #print(topic_post_res)
# ==========================抓取 question ID
                    pat = '<a class=\\\\"question_link\\\\" href=\\\\"\\\/question\\\/(.*?)\\\\" '
                    question_id_list = re.compile(pat).findall(topic_post_res) # 问题ID

# ====================从话题的详细页面进入具体的问题
                    """
                    详细描述：
                        通过上面的详细页面，可以获得问题的链接从而进入每一个具体问题。
                        具体问题的链接是形如https://www.zhihu.com/question/问题ID的样子
                        因而我们要获得问题ID。
                   """
                    for question_id in question_id_list:
                        bopenr(headers1)

                        #==== 抓取问题标题和内容
                        if bf.is_element_exist(question_id):
                            pass
                        else:
                            bf.insert_element(question_id)

                            question_initial_url = "https://www.zhihu.com/question/"+question_id
                            #print(question_initial_url)
                            try:
                                question_initial_url_req = urllib.request.Request(question_initial_url)
                                question_initial_url_res = urllib.request.urlopen(question_initial_url_req).read().decode("utf-8", "ignore")
                                #print(question_initial_url_res)
                                title_pat = '<title data-react-helmet="true">(.*?)- 知乎</title>'
                                question_title = re.compile(title_pat).findall(question_initial_url_res)[0]
                                #print(question_title)
                                selector = etree.HTML(question_initial_url_res)
                            except Exception as err:
                                print(err)
                            if selector.xpath('//span[@class="RichText"]/text()'):
                                question_content = selector.xpath('//span[@class="RichText"]/text()')[0]

                            else:
                                question_content = "没有描述"
                            sql = 'insert into ask(title, link, detail, aid) values("%s","%s","%s","%s")'
                            datasq = (question_title, question_initial_url, question_content, int(question_id))
                            try:
                                print("》》》》》》正在抓取问题标题、问题连接、问题描述、aid，并写入数据库》》》》》》")
                                cursor.execute(sql %datasq)
                                conn.commit()
                            except Exception as err:
                                print(err)
                            #print(question_id)
        # ===============抓回答

                            bopenr(headers2)
        # ================================
                            question_offset = 0
                            while True:
                                try:
                                    question_url = "https://www.zhihu.com/api/v4/questions/"+str(question_id)+"/answers?sort_by=default&include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cupvoted_followees%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cbadge%5B%3F%28type%3Dbest_answerer%29%5D.topics&limit=20&offset="+str(question_offset)
                                    question_req = urllib.request.Request(question_url)
                                    question_res = urllib.request.urlopen(question_req).read().decode("utf-8", "ignore")
                                except Exception as err:
                                    print(err)
                                pat2 = '"totals": (.*?),' # 最后漏了逗号，只能抓到空格
                                totals_res = re.compile(pat2).findall(question_res)
                                question_offset = question_offset + 20
                                pat3 = '"is_end": (.*?),'
                                is_end = re.compile(pat3).findall(question_res)
                                if is_end[0] == 'true':
                                    break # 下一次再break
                                #print(is_end[0])

                                #print(int(totals_res[0]))
                                #print(question_res)
                                json_question = json.loads(question_res)
                                answer_author = jsonpath.jsonpath(json_question, "$..name")
                                #print(answer_author)
                                answer_content = jsonpath.jsonpath(json_question, "$..content")
                                #print(answer_content)
                                try:
                                    for i in range(0, len(answer_author)):
                                        #print(answer_author[i])
                                       # print(answer_content[i])
                                        #print(str(answer_author[i]), str(answer_content[i]),int(question_id))
                                        print("》》》》》》正在抓取回答者、回答内容、回答id，并写入数据库》》》》》》")
                                        sql = 'insert into answer(author, content, askid) values("%s", "%s", "%s")'
                                        datasqq = (answer_author[i], pymysql.escape_string(answer_content[i]), int(question_id))
                                        cursor.execute(sql %datasqq)
                                        conn.commit()
                                except Exception as err:
                                    print(err)

# ==========================抓取 data-score
                                pat1 = 'data-score=\\\\"(.*?)\\\\"'
                                ress = re.compile(pat1).findall(topic_post_res)
                                #print('ress')
                                #print(ress)
                                n = len(ress)
                                if ress:
                                    offset = ress[n-1]
                                else:
                                    break
conn.close()
