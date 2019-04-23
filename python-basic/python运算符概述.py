# -*- coding: utf-8 -*-
# @Time    : 2019-04-19 15:02
# @Author  : jesse
# @File    : python运算符概述.py

# a = 10
# b = 20
#
# print (a is b)
#
# b = 10
#
# print (a is b)

# ID函数

# a = 10
# b = 10
#
# print(id(a))
# print(id(b))

# is 和 ==的区别

print "#####下面这个情况,b和a指向同样的内存地址空间#########"
a = [1,2,3]
b = a
print (a == b)
print(a is b)

print "#########下面这2种情况,虽然b和a的值完全一样,但是不是同一个内存地址空间########"
a = [1,2,3]
b = [1,2,3]

print (a == b)
print(a is b)

print "#########下面这种情况也是一样########"
b=a[:]
print b
print(a == b)
print(a is b)