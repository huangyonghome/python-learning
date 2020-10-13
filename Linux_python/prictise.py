#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 上午11:14
# @Author  : jesse
# @File    : prictise.py

# d = {}
#
# d['a'] = 1
# d.setdefault('a',0)
# print(d)

import os


# print(os.path.abspath(__file__))

# def index_words(text):
#     result = []
#     if text:
#         result.append(0)
#     for index,letter in enumerate(text,1):
#         if letter == ' ':
#             result.append(index)
#
#     return result
#
#
# text = """The Zen of Python, by Tim Peters"""
# print(index_words(text))
#
#
# def generator_words(text):
#     if text:
#         yield  0
#
#     for index,letter in enumerate(text,1):
#         if letter == ' ':
#             yield index
#
# print([x for x in generator_words(text)])
# print(list(generator_words(text)))


# data = [item for item in range(1,102,10)]
#
# print(data)


import re

class Foo():
    def __init__(self):
        name = re.sub(r'([A-Z])', r'.\1', self.__class__.__name__)
        print(name)
        print(name[1:])
        print(self.__class__.__name__)


f = Foo()

