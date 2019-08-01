# -*- coding: utf-8 -*-
# @Time    : 2019-07-31 22:54
# @Author  : jesse
# @File    : python07.gevent.py

from gevent import monkey;monkey.patch_all()
import time
import gevent


def task():
    time.sleep(1)
    print(123456)


def sync():
    for i in range(10):
        task()



def async():
    g_list=[]
    for i in range(10):
        g = gevent.spawn(task)
        g_list.append(g)

    gevent.joinall(g_list)

# sync()
async()