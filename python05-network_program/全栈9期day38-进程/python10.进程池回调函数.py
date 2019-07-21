# -*- coding: utf-8 -*-
# @Time    : 2019-07-21 9:29
# @Author  : jesse
# @File    : python10.进程池回调函数.py

'''
进程池的回调函数.回调函数是主进程执行的
'''

from multiprocessing import Pool

import os


def func1(n):
    print("func1 pid:",os.getpid())
    return n*n

def func2(m):
    print("func2 pid:",os.getpid())
    print(m)


if __name__ == "__main__":

    print("主进程PID:",os.getpid())

    p = Pool(5)

    for i in range(10):
        p.apply_async(func1,args=(10,),callback=func2)
    p.close()
    p.join()