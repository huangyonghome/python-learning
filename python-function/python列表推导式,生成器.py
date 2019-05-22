#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 下午6:00
# @Author  : jesse
# @File    : python列表推导式,生成器.py

l1 = []
for i in range(1,21):
    l1.append(i)

print(l1)

#下面这个就是列表推导式的格式:
#[列表变量 for 列表变量 in 可迭代对象]

l2 = [i for i in range(0,21)]
print(l2)

#利用列表推导式.构建一个列表['python1期','python2期','python3期','python4期']

l3 = []
for i in range(1,5):
    a='python' + str(i) +'期'
    l3.append(a)

print(l3)