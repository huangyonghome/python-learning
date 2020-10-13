#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 上午10:26
# @Author  : jesse
# @File    : counter_practise.py

import json
from collections import Counter

c = Counter()

# with open('hsq.log') as f:
#     line = f.readline()
#     print(type(line))
#
#     line_dic = json.loads(line)
#     print(type(line_dic))
#     print(line_dic)
#     print(line_dic.get('request'))
#     print((line_dic.get('request')).split("?")[0])
    # for line in f:
#         line = json.loads(line)
#
#         # c[line.get] += 1
#
#

with open('hsq.log') as f:
    for line in f:
        line_dic = json.loads(line)
        request = line_dic.get('request').split('?')[0]
        c[request] += 1

for item in c.most_common(10):
    print(item)
# print(c.most_common(10))
