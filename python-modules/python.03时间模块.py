# -*- coding: utf-8 -*-
# @Time    : 2019-06-11 0:08
# @Author  : jesse
# @File    : python.03时间模块.py

import time

#(tm_year=2019, tm_mon=6, tm_mday=11, tm_hour=0, tm_min=9, tm_sec=6, tm_wday=1, tm_yday=162, tm_isdst=0)
print(time.localtime())

# 获取当前时间字符串.格式可以自定义 #2019-06-11 00:17:29
print(time.strftime("%Y-%m-%d %H:%M:%S"))

# print(time.strptime("2019-06-11 00:17:29",'%a %b %d %H:%M:%S %Y'))

print(time.clock())

import calendar

print(calendar.month(2016,8))

import datetime

help(datetime)