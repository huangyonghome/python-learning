#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/25 上午10:40
# @Author  : jesse
# @File    : python匿名函数.py

#匿名函数关键字:lambada

#lambda是一个表达式 , 而并非语句 , 所以可以出现在def语句所不能出现的位置 ,
# 并且不需要指定函数名; lambda表达式还可以提高代码的可读性 , 简化代码

#例如传统函数

def func(x):
    return x*x

print(func(5))

#匿名函数写法

func1 = lambda x : x*x
print(func1(5))

#匿名函数后面还可以直接传参数

func2 = (lambda x,y : x if x > y else y)(1,2)
print(func2)

#匿名函数接非固定参数

func3 = (lambda *args : max(args))(1,2,4,5,6)
print(func3)

#下面是几个匿名函数的使用例子

#计算列表中元素的平方

func4 = map(lambda i : i*i,[1,2,3,4,5])
print(list(func4))
