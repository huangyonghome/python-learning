#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 上午11:05
# @Author  : jesse
# @File    : read_csv.py

import csv
from collections import namedtuple

with open('example.csv') as f:

    #读取csv文件
    f_csv = csv.reader(f)

    #获取csv文件的标题
    headings = next(f_csv)

    #定义一个命名元祖.元祖的字段是csv文件的标题,考虑到有些字段是python关键字字段(比如class,def).或者可能会出现重复字段,
    # 所以使用rename参数,表示如果有python不允许的字段,自动重命名
    Row = namedtuple('Row', headings,rename=True)
    for r in f_csv: # 循环文件,由于标题已经读取了,所以这里循环的是表格内容
        row = Row(*r) #生成一个命名元祖,将表格内容的值赋予到csv标题
        # print(row.english)  #可以像函数和类的静态方法一样,根据标题列名字段获取值.
        print(row[2])  # 还可以使用下标访问元祖中的内容
