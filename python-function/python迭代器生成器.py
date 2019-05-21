#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/21 下午5:53
# @Author  : jesse
# @File    : python迭代器生成器.py

#支持__iter__方法就是可迭代对象,也就是迭代器

str1='jesse'
# print(dir(str1)) #查看是否有__iter__方法
# print( "__iter__" in dir(str1) ) #如果支持__iter__方法,则说明该对象是可迭代对象

iter1 = iter(str1) #将一个可迭代对象转换成迭代器.可以使用iter()方法转换
iter2 = str1.__iter__() #或者也可以使用__iter__()方法来转换
print(iter1)
print(iter2)

print(iter1.__next__()) #遍历迭代器中的第1个元素
print(iter1.__next__()) #遍历迭代器中的第2个元素
print(iter1.__next__()) #遍历迭代器中的第3个元素
print(iter1.__next__()) #遍历迭代器中的第4个元素
print(iter1.__next__()) #遍历迭代器中的第5个元素
print(iter1.__next__()) #遍历迭代器中的第6个元素 #如果超过迭代器的元素个数,则会报出StopIteration异常

