#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/3 下午2:44
# @Author  : jesse
# @File    : python装饰器.py

# import time
# def timer(func):
#     def inner(*args,**kwargs):
#         start = time.time()
#         re = func(*args,**kwargs)
#         print(time.time() - start)
#         return re
#     return inner
#
# @timer   #==> func1 = timer(func1)
# def func1(a,b):
#     print('in func1')
#
# @timer   #==> func2 = timer(func2)
# def func2(a):
#     print('in func2 and get a:%s'%(a))
#     return 'fun2 over'
#
# func1('aaaaaa','bbbbbb')
# print(func2('aaaaaa'))
#
# def decorator(func):
#     def inner():
#         func()
#     return inner
#
# @decorator
# def index():
#     '''
#     这是一个主页信息
#     '''
#     print('from index')
#
# index()
#
# print(index.__doc__)
# print(index.__name__)

# def wrapper1(func):
#     def inner():
#         print('wrapper1 ,before func')
#         func()
#         print('wrapper1 ,after func')
#     return inner
#
# def wrapper2(func):
#     def inner():
#         print('wrapper2 ,before func')
#         func()
#         print('wrapper2 ,after func')
#     return inner
#
# @wrapper2
# @wrapper1
# def f():
#     print('in f')
#
# f()


# def decorator(func):
#     def inner():
#         print("I am decorator")
#         func()
#     # 此处删去inner调用
#     return inner
# def func():
#     print("I am func")
#     return func
# # func变量名覆盖了func()的函数名
# func1 = decorator(func)
# # 实际调用inner()
# func1()

# def wrapper(s1):
#     n = 1
#     def inner():
#         nonlocal n
#         n += s1
#         print(n)
#     return inner
#
# wrapper(5)()
# wrapper(5)()
# wrapper(5)()
# wrapper(5)()

#需求1.测试func1函数的执行时间

# import time
# def func1():
#     time.sleep(0.5)
#     print("i am func1")
#
#
# def timer():
#     start_time = time.time()
#     func1()
#     end_time = time.time()
#     print("it costs time: %f" %(end_time-start_time))
#
# timer()

#需求2.测试func1,func2这2个函数的执行时间

# import time
# def func1():
#     time.sleep(0.5)
#     print("i am func1")
#
# def func2():
#     time.sleep(0.5)
#     print("i am func2")
#
# def timer(f):
#     start_time = time.time()
#     f()
#     end_time = time.time()
#     print("it costs time: %f" %(end_time-start_time))
#
# #将函数名作为参数,传递到timer函数.但是函数(func1,func2)的本来的调用方式,已经发生了改变
# timer(func1)
# timer(func2)

#需求3.不能修改func1,func2函数本身,也不能修改调用方式

# import time
# def func1():
#     time.sleep(0.5)
#     print("i am func1")
#
# def func2():
#     time.sleep(0.5)
#     print("i am func2")
#
# def timer(f):
#     def inner(): #使用函数闭包
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print("it costs time: %f" %(end_time-start_time))
#     return inner
#
# #定义一个func的变量名,同时将func函数名作为参数传递给timer函数.此时func1是变量名,而非函数名.实际上func1 = inner.
# func1 = timer(func1)
# func2 = timer(func2)
#
# #此时函数调用方式仍然为func1(),func2()..没有改变函数调用方式.
# func1()
# func2()

#需求4.精简代码.使用语法糖格式

# import time
#
# def timer(f):
#     def inner(): #使用函数闭包
#         start_time = time.time()
#         f()
#         end_time = time.time()
#         print("it costs time: %f" %(end_time-start_time))
#     return inner
#
# @timer  #@函数名,这个就是语法糖.实际上这一行等同于 func1 = timer(func1)
# def func1():
#     time.sleep(0.5)
#     print("i am func1")
#
# @timer #实际上这一行等同于 func2 = timer(func2)
# def func2():
#     time.sleep(0.5)
#     print("i am func2")
#
#
# func1()
# func2()

#需求5.多个装饰器,装饰一个函数

import time

def timer1(f):
    print("i am timer1")
    def inner(): #使用函数闭包
        start_time = time.time()
        f()
        end_time = time.time()
        print("timer1 costs time: %f" %(end_time-start_time))
    return inner

def timer2(f):
    print("i am timer2")
    def inner(): #使用函数闭包
        start_time = time.time()
        f()
        end_time = time.time()
        print("timer2 costs time: %f" %(end_time-start_time))
    return inner


@timer1
@timer2 #@函数名,这个就是语法糖.实际上这一行等同于 func1 = timer(func1)
def func1():
    time.sleep(0.5)
    print("i am func1")


func1()
