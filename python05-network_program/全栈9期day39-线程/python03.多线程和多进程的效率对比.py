# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 17:07
# @Author  : jesse
# @File    : python03.多线程和多进程的效率对比.py

'''
演示了100个线程和100个进程的效率
从结果可知,启动100个线程只需要0.01秒,但是100个进程却要3.46秒
'''
from threading import Thread
from multiprocessing import Process
import time


def func(n):
    n += 1


if __name__ == "__main__":

    t_list = []
    p_list = []
    start = time.time()

    for i in range(100): #启动100个子线程
        t = Thread(target=func,args=(i,))
        t.start()
        t_list.append(t)

    for t in t_list:
        t.join()
    t1 = time.time() - start #计算执行时间

    start2 = time.time()

    for i in range(100): #启动100个子进程
        p =Process(target=func,args=(i,))
        p.start()
        p_list.append(p)

    for p in p_list:
        p.join()

    t2 = time.time() - start2 #计算执行时间

    print(t1,t2)
