# -*- coding: utf-8 -*-
# @Time    : 2019-07-27 8:29
# @Author  : jesse
# @File    : python04.线程锁.py

'''
线程和进程一样.当多个线程访问同一个数据时,就会产生不安全问题.例如下个例子.当多个线程同时对n进行进行操作.可能会得到意料之外的结果
'''

from threading import Thread
import time


# def func():
#
#     global n
#     temp = n
#     time.sleep(0.2)
#     n = temp - 1
#
#
# n = 10
#
# t_list=[]
#
# for i in range(10):
#
#     t = Thread(target=func)
#     t.start()
#     t_list.append(t)
#
#
# for t in t_list:
#     t.join()
#
# 这个时候n打印结果是9,而不是0 .这因为所有线程读取到的n的值都是10.因为在time.sleep的时间内,所有线程都拿到了n的起始值.
# print(n)

'''
此时就要使用锁机制.和进程锁一模一样.此时得出期望的结果.但是执行效率因此变得慢了许多
'''

# from threading import Lock
#
# def func(mutex):
#
#     global n
#     mutex.acquire()
#     temp = n
#     time.sleep(0.2)
#     n = temp - 1
#     mutex.release()
#
#
# n = 10
#
# t_list=[]
# mutex = Lock()
# for i in range(10):
#
#     t = Thread(target=func,args=(mutex,))
#     t.start()
#     t_list.append(t)
#
#
# for t in t_list:
#     t.join()
#
#
# print(n)

'''
但是如果是两把锁,就可能产生死锁.比如下面的科学家吃面的例子
'''

# from threading import Thread,Lock
#
# def eat1(name):
#     '''
#     先拿面条锁,再拿叉子锁才能吃到面条
#     :return:
#     '''
#     noodle_lock.acquire()
#     print("%s拿到了面条锁" %name)
#     fork_lock.acquire()
#     print("%s拿到了叉子锁" %name)
#     print("%s开始吃面条" %name)
#     fork_lock.release()
#     noodle_lock.release()
#
# def eat2(name):
#     '''
#     先拿叉子锁,再拿面条锁,才能吃到面条
#     :return:
#     '''
#     fork_lock.acquire()
#     print("%s拿到了叉子锁" % name)
#     time.sleep(1)
#     noodle_lock.acquire()
#     print("%s拿到了面条锁" % name)
#     print("%s开始吃面条" % name)
#     noodle_lock.release()
#     fork_lock.release()
#
# #一把面条锁
# noodle_lock = Lock()
#
# #一把叉子锁
# fork_lock = Lock()
#
# Thread(target=eat1,args=("Alex",)).start()
# Thread(target=eat2,args=("Wusir",)).start()
# Thread(target=eat1,args=("Jesse",)).start()
# Thread(target=eat2,args=("Lyon",)).start()

'''
此时,就要引入递归锁来解决这个问题
'''

from threading import Thread,RLock

def eat1(name):
    '''
    先拿面条锁,再拿叉子锁才能吃到面条
    :return:
    '''
    noodle_lock.acquire()
    print("%s拿到了面条锁" %name)
    fork_lock.acquire()
    print("%s拿到了叉子锁" %name)
    print("%s开始吃面条" %name)
    fork_lock.release()
    noodle_lock.release()

def eat2(name):
    '''
    先拿叉子锁,再拿面条锁,才能吃到面条
    :return:
    '''
    fork_lock.acquire()
    print("%s拿到了叉子锁" % name)
    time.sleep(1)
    noodle_lock.acquire()
    print("%s拿到了面条锁" % name)
    print("%s开始吃面条" % name)
    noodle_lock.release()
    fork_lock.release()

#一把面条锁,一把叉子锁,可以理解为一把钥匙串.
#RLock是递归锁
noodle_lock = fork_lock = RLock()


Thread(target=eat1,args=("Alex",)).start()
Thread(target=eat2,args=("Wusir",)).start()
Thread(target=eat1,args=("Jesse",)).start()
Thread(target=eat2,args=("Lyon",)).start()


#总结:

'''
Lock 互斥锁. 只允许一个线程访问一把锁.但是如果有两把锁,那可能2个线程分别拿到两把.造成死锁
Rlock 递归锁. 只允许一个线程访问多把锁.多把锁相当于一个钥匙串.如果一个线程访问其中的一把锁,则其他线程无法访问这把锁和这个钥匙串中的其他锁.保证数据安全
'''
