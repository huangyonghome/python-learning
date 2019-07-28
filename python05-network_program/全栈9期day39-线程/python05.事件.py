# -*- coding: utf-8 -*-
# @Time    : 2019-07-27 11:40
# @Author  : jesse
# @File    : python05.事件.py

'''
利用事件演示模拟数据库连接失败,超时等情况.
一个线程去执行数据库连接,事件默认状态为False.尝试连接数据库.如果在3次尝试时,t2线程仍然处在sleep状态,还未将事件状态设置为True的话,那么3次尝试都会失败,抛出异常.
e.wait(1).表示阻塞1秒就继续往下执行,如果没有参数,则一直阻塞
'''

import time,random
from threading import Thread,Event

def connect_db(e):
    count = 0

    while count < 3:
        e.wait(1) #状态为False的时候,等待1s就结束

        if e.is_set() == True: #如果事件状态为True,就模拟数据库连接正常
            print("连接数据库")
            break

        else: #如果事件状态为False.模拟数据库连接超时
            count += 1
            print("第%s次连接失败" %count)

    else: #如果3次还未连接上.则主动抛出一个timeout的异常

        raise TimeoutError("数据库连接超时")

def check_web(e):
    time.sleep(random.randint(0,3)) #模拟网络延时,或者超时
    e.set() #将事件值设为True,此时就不阻塞


e = Event()

t1 = Thread(target=connect_db,args=(e,))
t2 = Thread(target=check_web,args=(e,))
t1.start()
t2.start()

