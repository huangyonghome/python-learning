#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/26 上午11:31
# @Author  : jesse
# @File    : python集合.py

#定义一个集合,集合用大括号表示

# s1 = {1,2,3,4}
#
# print(s1)
# print(type(s1))
#
#
# #添加一个集合
# s1.add(5)
# print(s1)
#
# #集合里不会有重复元素
# s1.add(5)
# print(s1)
#
# #添加多项元素.注意集合是无序的
#
# s1.update('7','8','9','0')
#
# print(s1)
#
# s1.update(['a','b','c','d'])
#
# print(s1)

## 集合测试

a = {1,2,3,4,5}
b = {1,2,3}

#测试b中的每一个元素是否都在a中,即b <= a
# print(b.issubset(a))
#
# #测试是否a中的每一个元素都在b中.即 b >= a
#
# print(b.issuperset(a))
#
# print(a.issuperset(b))


## 集合操作

a = {1,2,3,4}
b = {4,5,6}

#并集
print(a.union(b))

#或者
print(a|b)

#求交集

print(a.intersection(b))
#或者
print(a & b)

#求差集

print(a.difference(b))
print(b.difference(a))

#或者
print(a - b)

#求对称差集
print(a.symmetric_difference(b))
#或者
print(a ^ b)