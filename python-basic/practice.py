#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 上午9:46
# @Author  : jesse
# @File    : practice.py

dic = {"name":"jesse","age":33,"job":"it","sex":"male"}
#
# dic.update({"name":"lyon"})
#
# dic.update({"company":"internet"})
#
# print(dic)
#
# dic.get("name")



for i,k in (enumerate(dic)):
    print(i,"\t",k)
