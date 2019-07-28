# -*- coding: utf-8 -*-
# @Time    : 2019-07-06 9:18
# @Author  : jesse
# @File    : python.01事件.py


#事件模块:Event

from multiprocessing import Event

#一个事件被创建后,默认是阻塞状态

e = Event() #创建一个事件

print(e.is_set()) #查看一个事件的状态,默认被设置成False,也就是阻塞,
print(123)
e.set() #将事件状态,也就是is_set的值改成True
e.wait() #根据is_set的值来决定是否阻塞.如果是False,阻塞,True则不阻塞
print(456)
e.clear() #将事件状态修改为False
print(e.is_set())
e.wait(1)
print(789)


'''
set和clear 用来修改一个事件的状态.要么为True,要么为False

is_set()   查看一个事件的状态.

wait       依据事件的状态,来决定是否阻塞.False为阻塞,True为不阻塞
'''