#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/20 上午9:41
# @Author  : jesse
# @File    : python数据类型.py

#浮点数的除法

# print(9 / 3)
#
# a = (9 / 3)
# print(type(a))


## 布尔值

# print(3 > 2)
# print(3 > 5)

## 布尔值的and运算

# print(3 > 2 and 3 < 5)
#
# print(3 > 1 and 3 < 1)

# 布尔值的or运算

# print (True or False)
# print (3 > 9 or 3 < 5)

#布尔值的Not运算

# print(not True)
# print(not 3 > 9)

#空值和布尔值的关系

# a = ""
# b = None
#
# if a:
#     print("a is True")
# else:
#     print("a is False")



#
# if b:
#     print("b is True")
# else:
#     print("b is False")

##====================================

#变量

# a = 'ABC'
# b = a
# a = 'XYZ'
# print(b)

# r表示不用转义特殊字符,例如

# s3 = r'Hello, "Bart"'
# s4 = r'''Hello,
# Lisa!'''
#
# print(s3)
# print(s4)


# a = 10
# b = 100
# a,b = b,a
# # a = b
# # b =a
# print(a,b)


#bytes数据类型

# s1 = 'jesse'
# s2 = b'jesse'
#
# print(s1 , type(s1))
# print(s2, type(s2))
#
# s3 = '您好'
# s4 = '您好'.encode('utf-8')
#
# print(s3, type(s3))
# #\x表示一个字节.一个中文占用3个字节
# print(s4, type(s4))
#
#
# s3 = s1.encode('utf-8')
#
# print(s1, type(s1))
# print(s3, type(s3))
#
#
# #字符解码.decode方法
#
# b1 = b'\xe6\x82\xa8\xe5\xa5\xbd'
#
# b2 = b1.decode('utf-8')
# print(b2, type(b2))