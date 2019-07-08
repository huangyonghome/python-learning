# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 10:15
# @Author  : jesse
# @File    : my_module2.py

print("执行了module1目录下的module1模块")
class Foo1:
    def __init__(self):
        print("执行module1模块的Foo1函数")



import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from ..module2 import my_module2.Foo2

Foo2()