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
# name[0] = name[0].upper()
# print(name)

#2.将tony变成首字母大写
# str = name[-1][-1].capitalize()
# name[-1][-1] = str
# print(name)


#练习

# print(name)
#
# print(name.index('alex'))
#
# print(name[1:3])
#
# print(name[-1])
#
# name.append('alita')
# print(name)
#
#
# name.insert(1,'new')
# print(name)
#
# name.insert(0,'end')
# print(name)
#
# name[0] = 'starts'
# print(name)
#
#
# name[:3] = '123'
#
# print(name)
#
# name[:3] = "a","b","c"
#
# print(name)
#
# name[:3] = ("x","y","z")
#
# print(name)
#
# name.pop(0)
#
# print(name)
#
# name.pop()
# print(name)
#
# name.remove('alex')
#
# print(name)
#
# del name[0]
#
# print(name)
#
# del (name[:2])
#
# print(name)
#
# name.clear()
#
# print(name)
#
#
# name = ['jesse','Lyon','alex','jerry',[1,'tony']]
#
# name1 = ['new','second','two']
#
# print (name + name1)
#
# name.extend(name1)
#
# print(name)
#
# name2 = name.copy()
# name3 = name
# name4 = name[:]
#
# name.clear()
#
# print(name)
# print(name2)
# print(name3)
# print(name4)

# print(name)
# name.pop()
#
# name.sort()
# print(name)
#
# name.reverse()
# print(name)

'''深浅copy
'''

#以下情况为浅copy
#1.赋值法: l2 = l1
#
# l1 = ['jesse','huang','alex',[ 'name','age',1,2],{"job":'IT',"company":'dwd'}]
#
# l2 = l1.copy()
#
# l1[-1]['industry'] = 'internet'
# l1.insert(0,'new')
# l1[1] = 'jessehuang'
# l1[-2].append('newlist')
#
# print(l1, id(l1),id(l1[-1]),id(l1[-2]))
# print(l2, id(l2),id(l2[-1]),id(l2[-2]))

#以下情况为深copy
#用copy模块的deepcopy方法

# import copy
# l1 = ['jesse','huang','alex',[ 'name','age',1,2],{"job":'IT',"company":'dwd'}]
#
# l2 = copy.deepcopy(l1)
#
#
# l1[-1]['industry'] = 'internet'
# l1.insert(0,'new')
# l1[1] = 'jessehuang'
# l1[-2].append('newlist')
#
# print(l1, id(l1),id(l1[-1]),id(l1[-2]))
# print(l2, id(l2),id(l2[-1]),id(l2[-2]))

#以下为深浅中等法
#1.copy法: l2 = l1.copy()
#2.切片法:  l2 = l1[:]

# l1 = ['jesse','huang','alex',[ 'name','age',1,2],{"job":'IT',"company":'dwd'}]
#
# l2 = l1[:]
#
# l1[-1]['industry'] = 'internet'
# # l1.append('new')
# # l1[0] = 'jessehuang'
# l1[-2].append('newlist')
#
# print(l1, id(l1),id(l1[-1]))
# print(l2, id(l2),id(l2[-1]))

#总结这3种的区别:

#对于浅copy: 1.修改原列表的任何元素,都会影响新列表.
#           2.源列表和新列表关联到同一个内存地址空间

#对于中等copy: 1.修改原列表内的可变元素(例如原列表本身,原列表的子列表,字典等可变元素)则会影响新列表.
#             2.修改原列表内的不可变元素(例如字符串),则不会影响到新列表
#             3.2个列表本身拥有不同的内存地址空间,但是,列表内的可变子元素(子列表,字典等)还是会关联到同一个内存地址.

#对于深copy: 1.修改原列表内的任何元素,都不会影响到新列表
#           2.列表本身,以及列表内的所有子元素,都关联到不同的内存地址



#列表的形参

# def f(x,l=[]):
#     for i in range(x):
#         l.append(i*i)
#     print(l)
#
# f(2)
# f(3,[3,2,1])
# f(3)


'''
练习题
'''

#1.将下列列表中奇数索引的元素删除

# l1 = [00,11,22,33,44,55,66]
# l2 = []
#
# #方法一.采取步长方式
#
# print(l1[::2])
#
# #方法二.判断是否能被2整除..因为列表是可变的,对列表的任何修改都会得到预期之外的结果.所以不能对列表进行直接操作
#
# for num in range(len(l1)):
#      if num % 2 == 0:
#          l2.append(l1[num])
#
# print(l2)
#
# #方法三..倒序循环列表,可以直接修改.因为修改列表(删除列表元素)对循环的索引没有影响.
#
# #注意,起始索引是列表长度-1,然后截止索引是-1,而不是0,步长是-1
#
# for num in range(len(l1)-1,-1,-1):
#     if num % 2 == 1:
#         del l1[num]
#
# print(l1)

#判断是否是列表的元素

# l1 = ['jesse','jerry']
#
# print('jesse' not in l1)