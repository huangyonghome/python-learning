# -*- coding: utf-8 -*-
# @Time    : 2019-07-30 23:32
# @Author  : jesse
# @File    : practise.py

# def decorator(func):
#     def inner():
#         print("i am decorator")
#         func()
#     return inner
#
# def decorator1(func):
#     def inner():
#         print("i am decorator")
#         func()
#     return inner
#
# # func = decorator(func)
# @decorator
# @decorator1
# def func():
#     print("i am func")
#     return func
#
# # func = decorator(func)
#
# func()


# func = map(lambda i : i * i ,[1,2,3,4])
# print(list(func))

# print(help(list.reverse))

l_sort = [('alex',2),('wusir',3),('jesse',4),('david',9)]

# l_sort1 = sorted(l_sort) #默认按照列表的每个元素的首字母进行排序
# print(l_sort1)

def f_sort(x):
        return x[1]


l2 = sorted(l_sort,key=f_sort)

print(list(l2))