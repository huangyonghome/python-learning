#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 上午11:45
# @Author  : jesse
# @File    : python类.py


#类的格式

#class 类名:
#    pass

#举个例子

#创建一个类
class Person():
    #构造函数,初始化属性

    def __init__(self,name):
        self.name = name

    #动态方法

    def eat(self):
        print("I am eating")



#实例化一个对象

p = Person('jesse')

