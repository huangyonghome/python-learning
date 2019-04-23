#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/23 下午7:00
# @Author  : jesse
# @File    : python字典.py

#1.创建一个空字典

dic = dict()
#或者
dic1 = {}

print(dic)
print(dic1)

#创建字典
dic = {"name":"jesse","age":33,"job":"it","sex":"male"}

#### 2.增加键值对

#给字典增加一个新的键值对.如果键不存在,则添加

dic['company'] = 'dwd'

print(dic)

#如果字典已经存在了这个键.则用新的值替代

dic['company'] = 'hsq'

print(dic)

#通过setdefault方法也可以增加一个值
dic.setdefault('school',"college")

print(dic)

#和刚才相反.如果键已经存在,则新值不会生效.
dic.setdefault('school','primary')

print(dic)



