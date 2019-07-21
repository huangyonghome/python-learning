# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 16:10
# @Author  : jesse
# @File    : python01.线程.py

'''
线程的thread函数和进程的process函数用法相同.
线程的主线程和子线程的PID相同

'''
from threading import Thread

import os


def func(a,b):
    n = a+b
    print(n,"子线程的PID",os.getpid())


print("主线程PID:",os.getpid())
for i in range(10):
    t=Thread(target=func,args=(i,5))

    t.start()