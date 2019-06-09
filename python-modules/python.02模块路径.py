# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 10:16
# @Author  : jesse
# @File    : python.02模块路径.py

'''

模块引用顺序:
1.从内存中寻找
2.从内置模块寻找(os,time.sys...)
3.从sys.path寻找
'''

import sys
#sys.path就是系统的环境变量,类似于Linux的PATH变量
# print(sys.path)

#找不到module1模块,这是因为module1模块不在以上3个顺序中,而是在module目录下,python无法知道module1模块在哪里

# import module1

#解决办法

#1.将module目录添加进sys.path环境变量

sys.path.append(r"D:\python-learning\python-modules\module")

import module1

#2.利用from关键字指定从何处加载

from module import module1
module1.Foo()

