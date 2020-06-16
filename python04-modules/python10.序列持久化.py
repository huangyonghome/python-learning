#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/12 下午6:11
# @Author  : jesse
# @File    : python10.序列持久化.py

import json

# f = open('json_file','a+')
#
# dic = {'name':'jesse','age': 33,'job':'city'}
#
# json.dump(dic,f)
#
# f.close()
#
# f = open('json_file','r',encoding='utf-8')
#
# # dic = f.read()
# dic1 = json.load(f)
#
# f.close()
#
# # print(type(dic))
# # print(dic)
#
# print(type(dic1))
# print(dic1)

# dic = '{"name":"jesse","age": 33,"job":"city"}'
#
# f = open('json_file1','w')
#
# f.write(json.dumps(dic))
#
# f.close()
#
# with open('json_file1','r') as f:
#     line = f.read()
#
# line = json.loads(line)
#
# print(type(line),line)


# lst = [1,2,3,4,5]
#
# j_d = json.dumps(lst)
#
# print(type(j_d),j_d)
#
# j_s = json.loads(j_d)
#
# print(type(j_s),j_s)
#
# dic_s = '{"k1":"v1","k2":"v2"}'
#
# dic = json.loads(dic_s)
#
# print(type(dic),dic)

############################

# import pickle
#
# dic = {'k1':'v1','k2':'v2','k3':'v3'}
#
# p_d = pickle.dumps(dic)
#
# print(type(p_d),p_d)
#
# p_l = pickle.loads(p_d)
#
# print(type(p_l),p_l)