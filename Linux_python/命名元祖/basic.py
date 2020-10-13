#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 上午11:25
# @Author  : jesse
# @File    : basic.py

#导入colletions模块
from collections import namedtuple

#定义一个命名元祖,
MyTupleClass = namedtuple('MyTupleClass','name age course')

#实例化一个元祖
obj = MyTupleClass("jesse",22,'English')

#可以通过属性获取元祖的值
print(obj.name,obj.age,obj.course)

print(obj)

my_class = MyTupleClass(name='jesse',age=33,course='English')
print(my_class)
print(my_class.age)
print('my name is: %s,%d years old,I am learning %s' % my_class)
# print(type(obj))
# print(type(MyTupleClass))