#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/15 上午9:16
# @Author  : jesse
# @File    : python.csv模块.py

#下面演示了csv模块的用法,将普通文本中的内容读取,然后写入到csv文件中

import csv

with open ('pv','r') as pv,open('1.csv','w') as f:

    head = ["head1", 'head2']
    writer = csv.writer(f)
    writer.writerow(head)
    while True:
        line = pv.readline()
        if not line: break
        l1 = line.split()
        writer.writerow(l1)
f.close()
pv.close()