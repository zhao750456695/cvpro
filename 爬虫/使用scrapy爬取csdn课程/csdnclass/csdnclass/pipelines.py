# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class CsdnclassPipeline(object):
    def process_item(self, item, spider):
        # 通过循环，将每一个课程写入单独的文件中
        for i in range(0, len(item['class_name'])):
            cn = item['class_name'][i]
            sn =item['student_num'][i]
            cp = item['class_price'][i]
            ct = item['class_time'][i]
            print('正在爬取课程:' + cn + ',并写入文件^_^')
            with open('./' +cn+'.txt','w+',encoding='utf-8',errors='ignore') as f:
                f.write('课程名：'+cn+ '\r\n')
                f.write('学生数：'+sn+'\r\n')
                f.write('课程价格：'+cp+'\r\n')
                f.write('课时数：'+ct+'\r\n')

        return item
