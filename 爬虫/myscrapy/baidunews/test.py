# -*- coding=utf-8 -*-
__author__ = 'zhaojie'
__date__ = '2018/4/4 8:41'
import re
with open('./new 5.txt', 'r') as f:
    data = f.readlines()
    idlist = []
    for line in data:
        if len(line)>1:
            print('line', len(line))
            pat = 'id=(.*?)&'
            res = re.compile(pat).findall(line)[0]

            idlist.append(res)
    print(idlist)

