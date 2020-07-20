# -*- coding: utf-8 -*-
# @Time    : 2019-06-11 0:08
# @Author  : jesse
# @File    : python.03时间模块.py

import time
import os
import datetime

# now_time = time.strftime("%Y-%m-%d %H:%M:%S")
#
# print(now_time)
#
# now_timestamp = time.time()
#
# print(now_timestamp)
#
# print(time.localtime())

# current_time = time.strftime('%Y%m%d')
# filename = 'access'+'-'+current_time+'.log'
# file_dir = '/data/logs/mendian_pv/'
# oss_dir = '/pv_log/'
#
#
# oss = os.path.join(file_dir,filename)
# oss_dir = os.path.join(oss_dir,filename)
#
# print(oss_dir)

print(datetime.timedelta(days=1))
#
# day = datetime.datetime.strptime(self.date,'%Y-%m-%d')
#
# print(datetime.date.today())
# today = datetime.date.today()
# print(str(today - datetime.timedelta(days=1)))

# print((date.today() + timedelta(days = -1)).strftime("%Y%m%d"))
#
today = datetime.datetime.today()

yesterday = today - datetime.timedelta(days=1)

print(yesterday.strftime("%Y%m%d"))


# st = time.strptime(ft,'%Y/%m/%d %H:%M:%S')
#
# print(st)
#
# print(time.localtime())

# print(time.time())
#
# print(time.time())

#(tm_year=2019, tm_mon=6, tm_mday=11, tm_hour=0, tm_min=9, tm_sec=6, tm_wday=1, tm_yday=162, tm_isdst=0)
# print(time.localtime())

# 获取当前时间字符串.格式可以自定义 #2019-06-11 00:17:29
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

# print(time.strptime("2019-06-11 00:17:29",'%a %b %d %H:%M:%S %Y'))

# print(time.clock())
#
# import calendar
#
# print(calendar.month(2016,8))
#
# import datetime
#
# help(datetime)

'''
python有3种时间形式:
'''

#1.时间戳.返回当前时间的时间戳(1970纪元后经过的浮点秒数)
# print(time.time())

#2.格式化时间.
# print(time.strftime("%Y-%m-%d %H:%M:%S"))

#3.结构化时间元祖
# print(time.localtime())

'''
时间格式之间的转换
'''

# #1.格式化时间 -----> 结构化时间
# ft = time.strftime('%Y-%m-%d %H:%M:%S')
# st = time.strptime(ft,'%Y-%m-%d %H:%M:%S')
# print(ft, st,sep='\n')
# #

# #2,结构化时间------->时间戳
# t= time.mktime(st)
# print(t)
#
#
# #时间戳---------->结构化时间
# t = time.time()
# st = time.localtime(t)
# print(st)
# #
# # #结构化时间---------->格式化时间
# ft = time.strftime('%Y-%m-%d %H:%M:%S',st)
# print(ft)

# print(time.asctime())
# print(time.ctime())
# print(time.localtime())
#
#
# true_time=time.mktime(time.strptime('2017-09-11 08:30:00','%Y-%m-%d %H:%M:%S'))
# time_now=time.mktime(time.strptime('2017-09-12 11:00:00','%Y-%m-%d %H:%M:%S'))
# dif_time=time_now-true_time
# print(dif_time)
# struct_time=time.gmtime(dif_time)
# print(struct_time)
# print('过去了%d年%d月%d天%d小时%d分钟%d秒'%(struct_time.tm_year-1970,struct_time.tm_mon-1,
#                                        struct_time.tm_mday-1,struct_time.tm_hour,
#                                        struct_time.tm_min,struct_time.tm_sec))

# import datetime
#
# print(datetime.datetime.now())
#
# print(datetime.datetime.now() + datetime.timedelta(weeks=-3))


# t = time.time()
#
# st = time.localtime(t)
#
# rt = time.strftime('%Y-%m-%d %H:%M:%S',st)
#
# print(rt)