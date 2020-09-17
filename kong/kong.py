#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午2:16
# @Author  : jesse
# @File    : kong.py

import requests,json,ast

# url = 'http://10.0.0.101:8001/'

# data = {'name':'betaapi1','protocol':'http','host':'m.devapi.haoshiqi.net'}
#
# #提交
# server_url = url + 'services'
# r = requests.post(server_url,data=data)
# # # r = requests.get(server_url)
# print(r.status_code)
# print(r.text)
# response = json.loads(r.text)

# print(type(r.text))
# print(r.text)
# print(response)
# data = response.get('data')
# for item in data:d
#     # print(item)
#     if item.get('name') == 'betaapi':
#         print(item)
#         break

# print(data)
# # print(response.get("id"))
#
# for item in response.get('data'):
#     print(item)

# routes_url = url + 'routes'
# #
# data = {    "name": "test2",
#             "hosts2": "m.devapi.haoshiqi.net",
#             "strip_path": "true",
#             "protocols": ["http", "https"],
#             "paths": "/test",
#             "methods": ["GET", "POST"],
#             "service.id":"bf70b926-e427-408c-b777-9095a882814f"
#           }
#
# r = requests.post(routes_url,data=data)
# print(r.text)
# print(r.status_code)
#
# hsq_beta = '{ "name": "hsq-beta","host": "m.devapi.xxx.net","port": 80,"protocol": "http","path": "null"}'
#
# # print(ast.literal_eval(hsq_beta))
# # res = json.dumps(hsq_beta)
# dic = json.loads(res)
# print(dic)
# print(type(dic))

# import configparser,json,requests,sys
#
# config = configparser.ConfigParser()
# config.read('/Users/huangyong/Desktop/python-learning/kong/config.ini')
#
# service = config['service']
#
# service_dic = config['service'].getdict('hsq_beta')

data = {"name":"request-transformer","config.replace.uri":"/open/item/itemdetail","config.add.querystring":"id:\$(uri_captures.id)"}
#
url = 'http://10.0.0.101:8001/services/6234f088-14ed-4c6b-9784-c671d6895613/plugins'
r = requests.post(url,data=data)
print(r.status_code)
print(r.text)
#
# url = 'http://10.0.0.101:8001/routes/'
# res =requests.get(url)
# response = json.loads(res.text)
# data = response.get('data')
# print(data)
# for item in data:
#     print(item.get('id'))

