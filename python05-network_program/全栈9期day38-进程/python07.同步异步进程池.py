# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 22:17
# @Author  : jesse
# @File    : python07.同步异步进程池.py

'''
演示pool的另外2种同步和异步方法
'''

from multiprocessing import Pool
import time
import os

def func(n):
    print("第%s个进程开始..PID是%s" %(n,os.getpid()))
    time.sleep(1)
    print("第%s个进程结束,PID是%s" %(n,os.getpid()))


if __name__ == '__main__':
    pool = Pool(5)

    for i in range(10):
        # pool.apply(func,args=(i,)) #这是同步阻塞,串行执行
        pool.apply_async(func,args=(i,)) #这是异步执行,但是主进程不会等待进程池的子进程执行完成才结束

    pool.close() #子进程全部执行完毕
    pool.join() #主进程接收到子进程结束的信号