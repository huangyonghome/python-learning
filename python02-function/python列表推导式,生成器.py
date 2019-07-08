#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/22 下午6:00
# @Author  : jesse
# @File    : python列表推导式,生成器.py

# l1 = []
# for i in range(1,21):
#     l1.append(i)
#
# print(l1)

#列表
l1 = [1,2,3,4,5,6,7,8,9,10]
#列表推导式.
l2 = [i for i in range(1,11)]

print(l2)

#生成器表达式.生成器表达式和列表推导式的写法区别一个是中括号,一个是小括号
#生成器表达式是一个生成器对象

l3 = (i for i in range(1,11))

print(l3)

#生成器对象支持next()方法

print(next(l3))
print(l3.__next__())

#而列表和列表推导式不支持这个方法

print(l2.__next__())


#下面这个就是列表推导式的格式:
#[列表变量 for 列表变量 in 可迭代对象]

# l2 = [i for i in range(0,21)]
# print(l2)

#利用列表推导式.构建一个列表['python1期','python2期','python3期','python4期']

#下面是用循环处理
# l3 = []
# for i in range(1,5):
#     a='python' + str(i) +'期'
#     l3.append(a)
#
# print(l3)

#下面是用列表推导式
# l4 = ['python'+str(i)+'期' for i in range(1,5)]
# print(l4)

#可以用占位符来格式化输出
# l5 = ['python%s期' %i for i in range(1,5)]
# print(l5)

#筛选模式,带条件的列表推导式

# l1 = [i for i in range(0,31) if i % 2 == 0]
# print(l1)

#列表推导式练习题

#1.10以内所有数的平方的列表

l1=[i**2 for i in range(1,11)]
print(l1)

#2.30以内能被3整除的数的平方,
l2 = [i**2 for i in range(1,31) if i % 3 == 0]
print(l2)

#3.下面是个列表.过滤掉长度小于3的字符串,并将剩下的转换成大写字母
l3 = ['alex','jesse','taibai','re','ab']

l4 = [i.upper() for i in l3 if len(i)>= 3]
print(l4)