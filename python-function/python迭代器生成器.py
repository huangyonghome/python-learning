#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午5:53
# @Author  : jesse
# @File    : python迭代器生成器.py

#支持__iter__方法就是可迭代对象,也就是迭代器

str1='jesse'
# print(dir(str1)) #查看是否有__iter__方法
# print( "__iter__" in dir(str1) ) #如果支持__iter__方法,则说明该对象是可迭代对象

# iter1 = iter(str1) #将一个可迭代对象转换成迭代器.可以使用iter()方法转换
# iter2 = str1.__iter__() #或者也可以使用__iter__()方法来转换
# print(iter1)
# print(iter2)
#
# print(iter1.__next__()) #遍历迭代器中的第1个元素
# print(iter1.__next__()) #遍历迭代器中的第2个元素
# print(iter1.__next__()) #遍历迭代器中的第3个元素
# print(iter1.__next__()) #遍历迭代器中的第4个元素
# print(iter1.__next__()) #遍历迭代器中的第5个元素
# print(iter1.__next__()) #遍历迭代器中的第6个元素 #如果超过迭代器的元素个数,则会报出StopIteration异常

# dir_list = dir([1,2])
# dir_iter = dir([1,2].__iter__())
# print(dir_list)
# print(dir_iter)
#
# diff = set(dir_iter)-set(dir_list)
# print(diff)
#
# l1 = [1,2,3]
# iter1 = l1.__iter__()
#
# print(iter1.__next__())
# # print(l1.__next__())

#函数生成器 yield

# def iter():
#     print(111)
#     for i in range(5):
#         yield i
#
# iter1 = iter()
# print(iter1)
#
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())

#复杂的yield
#
# def func1():
#     for i in 'AB':
#         yield i
#     for j in range(3):
#         yield j
#
#
# func = func1()
#
# print(func)
# # print(func.__next__())
# # print(func.__next__())
# # print(func.__next__())
#
# print(list(func1()))
#
# #yield from 从一个可迭代对象里生成
#
# def func2():
#     yield from 'AB'
#     yield from range(3)
#
#
# print(list(func2()))

#计算动态平均值

def averager():
    total = 0
    count = 0
    average = None
    while True:
        term = yield average
        total += term
        count += 1
        average = total/count


g_avg = averager()
print(g_avg)

next(g_avg)

print(g_avg.send(10))
print(g_avg.send(20))
print(g_avg.send(30))