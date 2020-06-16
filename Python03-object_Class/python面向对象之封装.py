#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/13 下午5:10
# @Author  : jesse
# @File    : python面向对象之封装.py

#私有属性,私有方法

class A():
    def __init__(self,name):
        self.__name = name

    def __func(self):
        print("you got me")

a = A("jesse")

# print(a.__name)
print(a._A__name)
# print(a.__func())
print(a._A__func())