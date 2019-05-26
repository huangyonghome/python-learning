# -*- coding: utf-8 -*-
# @Time    : 2019-05-26 15:45
# @Author  : jesse
# @File    : python递归函数.py


#计算10以内的和

# def func(n):
#     if n == 1:
#         return n
#
#
#     return func(n-1) + n
#
# print(func(10))

#计算10的斐波那契数列

#1. 计算斐波那契数列中的第10个元素值
# def fib(x):
#      if (x == 1 or x == 2):
#
#          return 1
#      return fib(x-1) +fib(x-2)
#
#
# print(fib(10))

#2.计算斐波那契10个元素的列表
# l1 = []
# def fib(x):
#     if x == 0:
#         return 0
#     if (x == 1 or x == 2):
#         return 1
#     return fib(x - 1) + fib(x - 2)
#
# for i in range(10):
#     l1.append(fib(i))
#
# print(l1)

#2.2 下面这个写法也能实现同样的效果,此外还能定义其实数字

l1 = []

def fib(n1,n2,nt):
    if len(l1) == nt:
        return "stop"

    l1.append(n1)
    n3 = n1 + n2
    fib(n2,n3,nt)

fib(21,22,10)
print(l1)
