# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 16:21
# @Author  : jesse
# @File    : python02.线程数据共享.py

'''
演示主线程和子线程之间数据是共享的,无需通过队列或者管道来共享数据.

'''

from threading import Thread

def func():
    global g
    g += 1
    print(g)


g = 100
t_list = []

for i in range(10):
    t = Thread(target=func)
    t.start()

for t in t_list:
    t.join()

print(g)
