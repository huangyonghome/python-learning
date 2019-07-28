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

func5 = filter(lambda x : x % 2 == 0,[1,2,3,4,5,6])
print(list(func5))