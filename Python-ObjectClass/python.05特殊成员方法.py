#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 下午6:09
# @Author  : jesse
# @File    : python.05特殊成员方法.py

# ########## __doc__方法查看描述信息
#
# class Foo:
#     '''
#     这是一个类,里面什么都没有
#     '''
#     def __init__(self):
#         pass
#
# print(Foo.__doc__)
#
#
#
# ########__module__查看当前操作对象位于哪个模块
#
# from my_module import Foo
#
# print(Foo.__module__)
#
#
#
# #######查看对象的类:__class__
#
# class Foo:
#     def __init__(self):
#         pass
#
# a = Foo()
# print(a.__class__)
# print(type(a))
# print(type(Foo))
#
# ######### __dict__ 查看类或对象中的所有成员
#
# class Person:
#     __country = 'China'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         print('func')
#
# print("打印类成员".center(30,'-'))
# # print(Person.__dict__)
# for i in Person.__dict__:
#     print('{}:{}'.format(i,Person.__dict__[i]))
#
# p = Person('jesse',22)
# print("打印对象成员".center(30,'-'))
# for i in p.__dict__:
#     print('{}:{}'.format(i,p.__dict__[i]))

##__call__
#构造方法的执行是由创建对象触发的 , 而对于\_\_call\_\_ 方法的执行是由对象后加括号触发的

# class A:
#     def __init__(self):
#         print("执行init")
#
#     def __call__(self, *args, **kwargs):
#         print("执行call")
#
# a = A()
# a()

## \_\_str\_\_  \  \_\_repr\_\_  🍀

#改变对象的字符串显示 , 这两个方法都只能返回字符串

# class A:
#     def __str__(self):
#         return "I am str"
#
# a = A()
# print(str(a))
# print(repr(a))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # def __hash__(self):
    #     return hash(self.name)
    def __eq__(self, other):
        if self.name == other.name:
            return True

p_lst = []
for i in range(84):
    p_lst.append(Person('Lyon', i))
print(p_lst)
print(set(p_lst))
