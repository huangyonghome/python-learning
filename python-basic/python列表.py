#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/21 下午6:16
# @Author  : jesse
# @File    : python列表.py

name = ['jesse','Lyon','alex','jerry']

#### 1.切片和字符串一样,

####2.追加
# name.append("new")
# print(name)

####3.插入
#insert需要指定下标.
# name.insert(1,'insert')
# print(name)
#
# #如果下标不存在就插入到最后一个
# name.insert(111,'no one')
# print(name)

#### 4.迭代(扩展)
##新建另外一个列表
# name1=['new','second']
#
# name.extend(name1)
#
# print(name)

####5.删除

#按照索引删除
# name.pop(1)
# print(name)

#注意pop方法有返回值,返回的是删除的那个元素.例如
# print(name.pop(1))

#如果不指定索引,则删除最后一个
# name.pop()
# print(name)

#2.删除一个指定的真实元素
#
# name.remove('jesse')
# print(name)

#3.支持切片删除方法
#删除单个索引
# del name[1]
# print(name)

#删除切片
# del name[1:]
# print(name)

#4.清空列表.clear()方法

# name.clear()
# print(name)

####6.修改
# name[1]='jessehuang'
# print(name)

#切片修改
# name[:2] = "huang"
# print(name)

#查找

# print(name.index('jesse'))

# #len函数查找列表的长度
# print(len(name))
#
# #4.count函数,查找某个元素在列表里出现的次数
# print(name.count('jesse'))


#练习题

name = ['jesse','Lyon','alex','jerry',[1,'tony']]


#1.将jesse变成大写
name[0] = name[0].upper()
print(name)

#2.将tony变成首字母大写
str = name[-1][-1].capitalize()
name[-1][-1] = str
print(name)