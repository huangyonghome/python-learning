#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/24 上午9:54
# @Author  : jesse
# @File    : python内置函数.py

## str类型代码的执行(3个)
#exec 将字符串当做表达式执行,没有返回值

# l1 = '1+2+3'
# exec('1+2+3')

#eval 将字符串当做表达式执行,并返回执行结果
### 但是eval不能执行数据流语句. 而exec可以

# print(eval(l1))
#
# str2 = '''for i in range(1,10):
#                 print(i)
#                 '''

# print(eval(str2))
# exec(str2)

#compile

# code3 = 'name = input("please input your name:")'
# compile3 = compile(code3,'','single')
#
# exec(compile3)
# print(name)
#


#进制转换

#转换为2进制

# print(bin(10)) #0b开头表示为一个二进制数

#转换为十六进制

# print(hex(10)) #0x开头表示为一个十六进制






###数学运算

#返回一个数的绝对值

# num = -3
# print(abs(num))


#返回两个数的商和余

# print(divmod(5,2)) #第一个数为整除,第二个为取余


# min 返回最小值,如果多个参数最小值,则返回第一个

# print(min(1,2,3,4))

# l1 = [(1,2),(1,5),(1,1),(1,6)]
# print(min(l1))

#max 返回最大值,如果多个参数最大值,则返回第一个

# print(max(1,2,3,4))

# l1 = [(2,2),(1,5),(2,1),(2,6)]
# print(max(l1))
#
# l2 = [('a',5),('a',4),('b',1),('b',2)]
# print(min(l2))

#求和.sum

# l1 = [i for i in range(1,11)]
#
# print(sum(l1))

#小数精确 round(数字,保留小数位数)

# print(round(1.2345,2))

#幂运算

# print(pow(2,10))






#列表和元祖

#list方法将一个可迭代对象转换成列表
#tuple方法将一个可迭代对象转换成元祖
str1 = 'jesse'
l1 = list(str1)

print(list(str1))

print(tuple(str1))


#reversed顺序翻转,与list中reverse的区别在于,该翻转为新生成了一个对象,而不是在原对象上操作..
#reversed没有返回值
l2 = reversed(l1) #不修改源列表

print(list(l2))

l1.reverse() #源列表已被修改

print(l1)

#slice切片

slice1 = slice(0,1,None)

print(l1[slice1])

#字符串
#str转换为字符串
s1 = str(l1)  #将列表转换成字符串
print(s1,type(s1))

#bytes方法可以将字符串转成bytes类型

str2 = bytes('jesse',encoding='utf-8')
print(str2)

#还可以用Unicode转换

b = 'jesse'
b1 = b.encode('utf-8')
print(b1)


#字典

#其他内置函数

#enumerate.将一个可迭代对象的每个元素加上自定义序号,默认从0开始

# l2 = enumerate(l1,0)
#
# for i,k in l2:
#     print(i,k)


#all.判断一个可迭代对象里的元素是否都为空
# print(l1)
# l3 = []
# print(all(l3))
# print(all(l1))
#
# #any 判断一个可迭代对象里是否有真元素
#
# print(any(l1))
# print(any(l3))

#zip将两个长度相同的序列整合成键值对,返回一个zip对象可以用dict方法转换查看

# l1 = ["k1","k2","k3","k4"]
# l2 = ["v1","v2","v3","v4"]
#
# ret = zip(l1,l2)
# # dic1 = dict(ret)
#
# print(dict(ret))
# print(dic1)

# for k,v in dic1.items():
#     print(v)

#filter 筛选过滤,把可迭代对象中的元素一一传入function中进行过滤.

# def func(x):
#     if x % 2 == 0:
#         return x
#
# ret = filter(func,[1,2,3,4,5,6,7,8])
#
# for i in ret:
#     print(i)

# map(*function*, *iterable*, *...*)  将可迭代对象中的元素一一传入function中执行并返回结果

# def func(x):
#     return x +' hello'
#
# ret = map(func,['jesse','world'])
# ret1 = list(ret)
# print(ret1)

# sorted(*iterable*, ***, *key=None*, *reverse=False*)
# 为一个对象进行排序,在list中有个sort方法;区别:sort会改变原list,而sorted则不会改变原list

# l1 = [2,3,4,6,7,9,0,1]
# l1.sort()
# print(l1)#l1 列表已经改变
#
# l2 = [2,3,4,6,7,9,0,1]
# l3 = sorted(l2)
# print(l2) #l2列表不会改变
# print(l3)

#sorted排序还支持像函数传参,接收函数返回值,从而对返回值进行排序

l_sort = [('alex',2),('wusir',3),('jesse',4),('david',9)]

l_sort1 = sorted(l_sort) #默认按照列表的每个元素的首字母进行排序
print(l_sort1)

#使用函数来返回列表中每个子元素的第二个元素,对第二个元素(也就是数字)来进行排序

def f_sort(x): #函数指定形参,接收sorted方法传递的参数
    return x[1]

l_sort2 = sorted(l_sort,key=f_sort) #key关键字指定一个函数名(只是函数名,不是函数调用)
print(l_sort2)

## 迭代器/生成器相关(3个) 🍀

# `range`(*stop*)  👈

# `range`(*start*, *stop*[, *step*])   👈

#返回一个序列,为一个可迭代对象,并可用下标取值

# l1 = range(10)
# print(list(l1))
# print(l1[0])

#next 从迭代器里取值,一次只取一个,取完如果继续取会报StopIteration异常

# iter1 = iter([1,2,3,4])
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())

#iter创建一个迭代器
#
# iter1 = iter([1,2,3,4])
# print(iter1)

#help查找官方说明

# print(help(str))

#repr 返回一个对象的字符串形式.(也就是返回的结果有字符串引号)

s1 = 'jesse'
print(s1)
print(repr(s1))

#repr还有另外一种用法就是格式化输出的时候,%r表示法 .

print("my name is %s,I am %r" %('alex','sb'))

#其他还有以下内置函数

'''
dir() 查找内置方法
input() 输入
id() 查看对象内存地址
open() 打开文件
type() 查看对象类型
hash() 返回hash对象
callable() 查看对象是否可以被调用
'''