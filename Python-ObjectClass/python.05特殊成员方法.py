#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 下午6:09
# @Author  : jesse
# @File    : python.05特殊成员方法.py

########## __doc__方法查看描述信息

class Foo:
    '''
    这是一个类,里面什么都没有
    '''
    def __init__(self):
        pass

print(Foo.__doc__)



########__module__查看当前操作对象位于哪个模块

from my_module import Foo

print(Foo.__module__)



#######查看对象的类:__class__

class Foo:
    def __init__(self):
        pass

a = Foo()
print(a.__class__)
print(type(a))
print(type(Foo))

######### __dict__ 查看类或对象中的所有成员

class Person:
    __country = 'China'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def func(self):
        print('func')

print("打印类成员".center(30,'-'))
# print(Person.__dict__)
for i in Person.__dict__:
    print('{}:{}'.format(i,Person.__dict__[i]))

p = Person('jesse',22)
print("打印对象成员".center(30,'-'))
for i in p.__dict__:
    print('{}:{}'.format(i,p.__dict__[i]))