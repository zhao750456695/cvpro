# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='dd', charset='utf8', use_unicode=True)
        cursor = conn.cursor()
        for i in range(0, len(item['title'])):
            title=item['title'][i]
            link=item['link'][i]
            comment=item['comment'][i]
            sql = 'insert into good(title,link,comment) values("'+title+'","'+link+'","'+comment+'")'
            # sql = 'insert into goods(title,link,comment) values("%s", "%s", "%s")'
            # data = (str(title), str(link), str(comment))
            # cursor.execute(sql %data)
            # conn.commit()
            # try:
            #     conn.query(sql)
            #     conn.commit()
            # except Exception as err:
            #     print(err)
        conn.close()
        return item
