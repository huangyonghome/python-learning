# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 10:15
# @Author  : jesse
# @File    : my_module2.py

print("执行了module2目录下的module2模块")
class Foo2:
    def __init__(self):
        print("执行module2模块的Foo2函数")

import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from .. module1 import my_module1

my_module1.Foo1()
