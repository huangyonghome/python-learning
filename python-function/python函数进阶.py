#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/29 上午11:52
# @Author  : jesse
# @File    : python函数进阶.py

#函数嵌套

# 全局变量name
# name = "Lyon_1"
#
#
# def func():
#     # 第一层局部变量name
#     name = "Lyon_2"
#     print("第1层打印", name)
#
#     # 嵌套
#     def func2():
#         # 第二层局部变量name
#         name = "Lyon_3"
#         print("第2层打印", name)
#
#         # 嵌套
#         def func3():
#             # 第三层局部变量
#             name = "Lyon_4"
#             print("第3层打印", name)
#
#
#         # 调用内层函数
#         func3()
#         # 调用内层函数
#
#     func2()
#
#
# func()
# print("最外层打印", name)

# def func(arg):
#     n = arg
#     def func1():
#         n = 2
#         def func2():
#             nonlocal n      # n = 2
#             n += 1
#         func2()
#         print(n)        # n = 3
#     func1()
#     print(n)
# func(10)


# def decorator(func):
#     """func变量在inner函数外部"""
#     print("I am decorator")
#     def inner():
#         print("I am inner")
#         # 内部函数引用外部变量func,而func是一个函数对象,因此我们可以进行调用,此处闭包
#         func()
#     # 内部调用inner函数
#     inner()
#     # 返回inner,函数名 → 内存地址
#     print(inner)
#     return inner
#
# # decorator函数的参数函数
# def decorator_arg():
#     print("I am decorator_arg")
#     # 返回decorator_arg,函数名 → 内存地址
#     return decorator_arg
# # result接收的是inner函数名
# # result = decorator(decorator_arg)
# decorator(decorator_arg)()
# print('-------------------')
# # 实际调用的是嵌套函数中内部的inner函数
# #print(result)

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
# func = decorator(func)
# # 实际调用inner()
# func()
#
#
# def func():
#     print("I am func")
#     return
# def decorator(func):
#     print("I am decorator")
#     func()
#     return decorator
# func = decorator(func)
# print(func)
# func(func)

# def decorator(func):
#     # 此处将原始func参数进行打包
#     def inner(*args,**kwargs):
#         print("I am decorator")
#         # 此处将原始func参数进行拆包返还
#         func(*args,**kwargs)
#     return inner
# def func(*args,**kwargs):
#     print("I am func")
#     print(args,kwargs)
#     return func
# func = decorator(func)
# # inner(*args,**kwargs)
# func( )


# def func():
#     name = "Lyon"
#     def inner():
#         print(name)
#     return inner
# func = func()
# # 调用之前name的值已经传入inner中
# func()




# def func():
#     l = []
#     for i in range(10):
#         # inner函数并没有进行调用,但是for循环已经执行完毕,此时i=9
#         def inner(x):
#             return i + x
#         l.append(inner)
#     return l
# res = func()
# print(res)
# print(res[0](10))
# print(res[1](10))
# print(res[2](10))
# print(res[3](10))

# s = [lambda x: x + i for i in range(10)]
# print(s[0](10))
# print(s[1](10))
# print(s[2](10))
# print(s[3](10))

# def func():
#     name = "Lyon"
#     def inner():
#         print(name)
#     return inner
# # 内部inner
# print(func().__closure__)


#外部函数调用内部函数

# def decorate(func):
#     print("I am decorate")
#     def inner():
#         print("i am inner")
#         func()
#     return inner
#
#
# def func():
#     print("I am func")
#
#
# func = decorate(func)
# func()


# def decorate(func):
#     print(" I am decorate")
#     def inner():
#         print("i am inner")
#         func()
#     return inner
#
# @decorate
# def func():
#     print("I am func")
#
# func()


def decorate(func):
    print(" I am decorate")
    def inner():
        print("i am inner")
        func()
    return inner

def decorate2(func):
    print(" I am decorate2")
    def inner():
        print("i am inner2")
        func()
    return inner

@decorate
@decorate2
def func():
    print("I am func")

func()



