# -*- coding: utf-8 -*-
# @Time    : 2019-07-28 8:53
# @Author  : jesse
# @File    : python06.线程池.py

'''
有一个新的模块支持线程池和进程池:concurrent.futures
线程池的方法是ThreadPoolExecutor.
进程池也有相应的方法ProcessPoolExecutor..用法和Pool一样

下面的例子是线程池的方法.如果是进程池.只需要将ThreadPoolExecutor替换成ProcessPoolExecutor
'''

from concurrent.futures import ThreadPoolExecutor
import time

def func(n):
    time.sleep(2)
    print(n)
    return n*n


tpool = ThreadPoolExecutor(max_workers=5) #max_workers参数定义了线程池的大小,一般建议不超过CPU cores的5倍

t_list = []

for i in range(20):

    ##submit(fn, *args, **kwargs) #submit方法异步提交任务
    t = tpool.submit(func,i)
    t_list.append(t)

'''
shutdown方法相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前
'''
tpool.shutdown()  #如果注释,则主线程不会等待所有子线程执行完毕..而是一旦接收到任意子线程返回值就马上执行下面的代码

#result方法接收函数的返回值
for t in t_list:
    print("***",t.result())


'''
map方法可以替代for循环的submit的提交任务.直接异步提交.但是map方法无法接收到返回值'''

# def func(n):
#     time.sleep(2)
#     print(n)
#     return n*n
#
#
# tpool = ThreadPoolExecutor(max_workers=5) #max_workers参数定义了线程池的大小,一般建议不超过CPU cores的5倍
#
# t_list = []
#
#
# #map(func, *iterables, timeout=None, chunksize=1) 第一个参数是函数,第二个参数是一个可迭代对象
# tpool.map(func,range(20))
# # for i in range(20):
# #
# #     ##submit(fn, *args, **kwargs) #submit方法异步提交任务
# #     t = tpool.submit(func,i)
# #     t_list.append(t)
#
# '''
# shutdown方法相当于进程池的pool.close()+pool.join()操作
# wait=True，等待池内所有任务执行完毕回收完资源后才继续
# wait=False，立即返回，并不会等待池内的任务执行完毕
# 但不管wait参数为何值，整个程序都会等到所有任务执行完毕
# submit和map必须在shutdown之前
# '''
# tpool.shutdown()
#
# #result方法接收函数的返回值
# for t in t_list:
#     print("***",t.result())


'''
回调函数 add_done_callback(fn)方法
'''

from concurrent.futures import ThreadPoolExecutor
import time

def func(n):
    time.sleep(2)
    print(n)
    return n



def call_back(n):

    print(n*n)


tpool = ThreadPoolExecutor(max_workers=5) #max_workers参数定义了线程池的大小,一般建议不超过CPU cores的5倍


for i in range(20):

    tpool.submit(func, i).add_done_callback(call_back) #回调函数

'''
shutdown方法相当于进程池的pool.close()+pool.join()操作
wait=True，等待池内所有任务执行完毕回收完资源后才继续
wait=False，立即返回，并不会等待池内的任务执行完毕
但不管wait参数为何值，整个程序都会等到所有任务执行完毕
submit和map必须在shutdown之前
'''
#tpool.shutdown()  #如果注释,则主线程不会等待所有子线程执行完毕..而是一旦接收到任意子线程返回值就马上执行下面的代码
