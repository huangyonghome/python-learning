#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/5/27 下午6:09
# @Author  : jesse
# @File    : p1.py



def add_userinfo(name,age,province="北京"):
  	return name,province,age
s= add_userinfo(name="Lyon",province="湖北",age=18)

print(s)