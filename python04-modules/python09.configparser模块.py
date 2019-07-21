#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 下午6:02
# @Author  : jesse
# @File    : python09.configparser模块.py

import configparser

#实例化一个对象

conf = configparser.ConfigParser()

#读取配置文件

conf.read("config.ini")


#显示所有的块级别配置.在这个例子中,打印[mysql]和[client]

sec = conf.sections()
print(sec)

#显示某个块级别下的键值,例如mysql配置下的host,port配置

mysql_conf = conf.options("mysql")

print(mysql_conf)


#显示某个块级别下的所有键值对,
mysql_items = conf.items("mysql")

print(mysql_items)

#获取某个块级别下的属性对应值.例如打印出client块配置下的user值

user = conf.get("client",'user')

print(user)