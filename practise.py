#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午1:55
# @Author  : jesse
# @File    : practise.py

# import uuid
#
# a = str(uuid.uuid4())
#
# print(type(a),a)

# sum = 0
#
# for i in range(1,101):
#     sum += i
#
# print(sum)
#
#
#
#
# for i in range(1,101):
#     if i % 2 != 0:
#         print(i)
#
# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)

# list3 = [{"name":"alex","hobby":"抽烟"},
#          {"name":"alex","hobby":"喝酒"},
#          {"name":"alex","hobby":"烫头"},
#          {"name":"alex","hobby":"按摩"},
#          {"name":"egon","hobby":"喊麦"},
#          {"name":"egon","hobby":"街舞"},
#          ]
#
# list4 = []
# hobby_list = []
# for item in list3:
#     for item4 in list4:
#         if item['name'] == item4['name']:
#             item4['hobby_list'].append(item['hobby'])
#             break
#     else:
#         list4.append({"name":item['name'],"hobby_list":[item['hobby']]})






# def is_ipv4(ip):
#     """
#     检查ip是否合法
#     :param: ip ip地址
#     :return: True 合法 False 不合法
#     """
#     for x in ip.split("."):
#         print(x)
#
#     ip_list = [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")]
#     print(ip_list)
#
#     return True if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")] else False
#
# print(is_ipv4("192.168.1.20a"))


ip = "192.168.1.20a"
# if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")]:
#     print("ok")
# else:
#     print("no")
#
#
print(ip.startswith("19"))
print(ip.split(".")[0])

l1 = [1,2,3]
l2 = "sadf"

print(isinstance(l2,list))
import json
ip = ["10.111.5.177","10.111.5.178","10.111.5.179"]

ip.append({"name","jesse"})
ip.append({"name":"jerry"})
print(ip)