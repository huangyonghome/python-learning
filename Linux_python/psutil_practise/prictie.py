#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 下午1:52
# @Author  : jesse
# @File    : prictie.py

import psutil

# print(psutil.virtual_memory())

def bytes2human(n):
    symbols = ("K",'M','G','T','P','E','Z','Y')
    prefix = {}
    for i, s in enumerate(symbols):
        prefix[s] = 1 << (i + 1) * 10

    for  s in reversed(symbols):
        if n >= prefix[s]:
            value = float(n) / prefix[s]
            return '%.1f%s' %(value,s)
    return "%sB" %n

# print(bytes2human(psutil.virtual_memory().total))
# print(bytes2human(10))