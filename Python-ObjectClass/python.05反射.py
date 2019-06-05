# -*- coding: utf-8 -*-
# @Time    : 2019-06-05 22:49
# @Author  : jesse
# @File    : python.05反射.py

#
#反射主要是指程序可以访问、检测和修改它本身状态或行为的一种能力

#Python面向对象中的反射是通过字符串的形式来操作对象相关的属性 , 在Python中一切皆对象 , 并且只要是对象就可以使用反射


#hasattr 判断对象中是否具有给定名称的属性

name = 'jesse'

print(hasattr(name,'__len__'))
print(hasattr(name,'upper'))
print('jesse'.__len__)
print('jesse'.upper)

class A:
    pass

A.a = lambda _: 1
A.b = 1

s = lambda _ : 12
print(s(111))

_,b = 1,2
print(b)