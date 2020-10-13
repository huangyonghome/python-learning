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


# ip = "192.168.1.20a"
# # if [1] * 4 == [x.isdigit() and 0 <= int(x) <= 255 for x in ip.split(".")]:
# #     print("ok")
# # else:
# #     print("no")
# #
# #
# print(ip.startswith("19"))
# print(ip.split(".")[0])
#
# l1 = [1,2,3]
# l2 = "sadf"
#
# print(isinstance(l2,list))
# import json
# ip = ["10.111.5.177","10.111.5.178","10.111.5.179"]
#
# ip.append({"name","jesse"})
# ip.append({"name":"jerry"})
# print(ip)

#
# class A:
#     def __init__(self,name):
#         self.name = name
#         print(A.__name__)
#
#
# a = A('name')

#
# dic = {}
# l1 = []
# for i in range(2):
#     dic["name"] = 'jesse' + str(i)
#     dic["age"] = i
#     print("dic",":",dic)
#     l1.append(dic)
#     print(l1)
#
# # print
#
#
# print(isinstance(0,int))

# a=["千山鸟飞绝"]
# b=["千山鸟飞绝"]
# c=["千山鸟飞绝"]
# d=["千山鸟飞绝"]
#
# e=[a,b,c,d]
# print(e)
#
# f=[j for x in e for j in x[0]]

# e=a+b+c+d
# e.append(a,b,c,d)
# print(f)
# print(a.split(","))

# b = for x in str(a)
# b=[]

# print([x for x in a[0] b[0] c[0] d[0]])

# for x in a[0]:
#     b.append(x)

# print(b)


# import re
#
# a = """
#     domain: trade.doweidu.com
#     主机: hsq-api2
#     IP地址: ['10.111.5.248']
#     业务线: hsq
#     调用方式: GET
#     请求链接: /common/sysconfigbyname?name=order_tag_list
#     状 态 码: 200
#     后端服务器: 127.0.0.1:9000
#     数      量: 123067
# """
#
# b=re.findall(r"domain: (.*)\.doweidu\.com",a)[0]
#
# print(b)
#
#
#
#
# if project == "hsq":
#     at_list = ['15601606633']
# elif porject == "iqg":
#     at_list = ["13722981841"]
# elif project == "bbh":
#     at_list = ["17621707088"]
# elif project == "msf":
#     at_list = ["18015130020"]
# elif project == "mg":
#     if "nginx" in Type:
#         mg_project = re.findall("domain: (.*)\.doweidu\.com", body)[0]
#         if mg_project == "trade":
#             at_list = ["17721019171"]
#         elif mg_project == "message.center":
#             at_list = ["17091314591"]
#         elif mg_project == "goods.center":
#             at_list = ["18616309723"]
#         else:
#             at_list = ["18616990553"]
#     else:
#         at_list = ["18616990553"]
#
# if (not "at_list" in locals().keys()):at_list = ["17749739691"]
#
# print(at_list)
#
# # locals()
# # print( not 'b' in locals().keys())
#
#
#
# #
# #
# #
# #
# #
# # if Type == "fpm":
# #    if project == "hsq":
# #         at_list = ['15601606633']
# #    elif porject == "iqg":
# #         at_list = ["13722981841"]
# #    elif project == "bbh":
# #         at_list = ["17621707088"]
# #    elif project == "msf":
# #         at_list = ["18015130020"]
# #    elif project == "mg":
# #         at_list = ["18616990553"]

# a= [[1,2,3],[4,5,6]]
# b = [1,2,3,4,7,8,9,0]
# # print(a[::-1])
# print(b[::-1])
# print(b)
#®®
# import os
# print(os.path.abspath(os.path.dirname(__file__)))
# print(os.path.dirname(__file__))
# print(__file__)


# fruits = ['orange','apple','banana','pear']
#
# statement=fruits[0]
#
# for item in fruits[1:]:
#     statement = statement + ',' + item
#
#
# print(statement)

# print(",".join(fruits))

a = 'Hello,World'

print

b = ''.join(reversed(a))
print(b)
