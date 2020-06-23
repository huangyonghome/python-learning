#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/23 下午6:41
# @Author  : jesse
# @File    : python10.gevent(1).py

from gevent import monkey;monkey.patch_all()
import time
import gevent


def task():
    time.sleep(1)
    print(123456)

def sync():
    for i in range(10):
        task()

def async1():
    g_list=[]
    for i in range(10):
        g = gevent.spawn(task)
        g_list.append(g)

    gevent.joinall(g_list)

#sync()
async1()