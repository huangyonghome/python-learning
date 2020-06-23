# -*- coding: utf-8 -*-
# @Time    : 2019-07-31 22:54
# @Author  : jesse
# @File    : python07.gevent.py

from gevent import monkey;monkey.patch_all()
import time
import gevent


# def task():
#     time.sleep(1)
#     print(123456)
#
#
# def sync():
#     for i in range(10):
#         task()
#
# def async1():
#     g_list=[]
#     for i in range(10):
#         g = gevent.spawn(task)
#         g_list.append(g)
#
#     gevent.joinall(g_list)
#
# #sync()
# async1()


# import time
# def consumer():
#     r = ''
#     time.sleep(1)
#     while True:
#         n = yield r
#         if not n:
#             return
#         time.sleep(1)
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         time.sleep(1)
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
# c = consumer()
# produce(c)