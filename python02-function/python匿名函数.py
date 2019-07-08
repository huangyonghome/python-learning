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

#匿名函数写法.(函调调用的时候传参)

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

#filter 筛选偶数

func5 = filter(lambda x : x % 2 == 0,[1,2,3,4,5,6])
print(list(func5))

#max 筛选最大值(按照子元素的第二个值)

dic1 = {'k1':10,'k2':200,'k3':30}
func6 = max(dic1,key=lambda x : dic1[x])
print(func6)


#嵌套使用

def func6(x):
    return lambda y : x + y

f = func6(2)
print(f(6))


func7 = lambda x: (lambda y : x + y)

f = func7(6)
print(f(6))