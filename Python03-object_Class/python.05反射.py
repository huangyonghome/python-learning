# -*- coding: utf-8 -*-
# @Time    : 2019-06-05 22:49
# @Author  : jesse
# @File    : python.05反射.py

#
#反射主要是指程序可以访问、检测和修改它本身状态或行为的一种能力

#Python面向对象中的反射是通过字符串的形式来操作对象相关的属性 , 在Python中一切皆对象 , 并且只要是对象就可以使用反射


#hasattr 判断对象中是否具有给定名称的属性
#
# name = 'jesse'
#
# print(hasattr(name,'__len__'))
# print(hasattr(name,'upper'))
# print('jesse'.__len__)
# print('jesse'.upper)
#

# import sys
# def s1():
#     pass
# def s2():
#     pass
# this_modules = sys.modules[__name__]
# print(this_modules)
# print(type(this_modules),hasattr(this_modules,'s1'))


# class A:
#     pass
#
# A.a = lambda _: 1
# A.b = 1
#
# s = lambda _ : 12
# print(s(111))
#
# _,b = 1,2
# print(b)
#
#
# import sys
#
# def s1():
#     pass
#
# def s2():
#     pass
#
# this_modules = sys.modules[__name__]
# print(type(this_modules),hasattr(this_modules,'s1'))
# print(sys.modules[__name__])


#
# class A:
#     #创建个方法
#     def method1(self):
#         pass
#
#
# a = A() #实例化
#
# print(hasattr(a,'method2')) #判断a对象是否有method2的方法,显然结果为false


## getattr 从一个对象中获取属性名称

# class A:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def hello(self):
#         print('hello {}'.format(self.name))
#
#
# a = A('jesse',22)
#
# #获取静态属性age
# print(getattr(a,'age'))
# #获取动态属性,也就是方法
# print(getattr(a,'hello'))
#
# #如果不存在属性就报错
# # print(getattr(a,'sex'))
#
# #设置default参数,这样如果属性不存在就输出默认值
#
# sex = getattr(a,'sex','男')
# print(sex)



#setattr 修改一个属性的值

# class B:
#     def __init__(self):
#         pass
#
# b = B()
#
# #新增一个age属性
#
# setattr(b,'age',18)
#
# #打印age属性
# print(b.age)
#
# #新增add方法
# setattr(b,'add',lambda age: age + 1)
#
# #修改age属性,并且把b.age的值作为参数传递给lambda函数,接受lambda函数范围值
# b.age = b.add(b.age)
#
# #打印新增的add()方法返回值
# print(b.age)
#
#
#
# #删除对象中的属性
#
#
class C:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def add(self):
        self.age = self.age + 1

c = C('jesse',22)

#删除c的name属性

# delattr(c,'name')
#
# print(c.name) #抛出异常

# delattr(c,'add')
#
# c.add() #抛出异常