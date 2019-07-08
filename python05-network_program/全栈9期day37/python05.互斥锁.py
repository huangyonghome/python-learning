# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 15:43
# @Author  : jesse
# @File    : python05.互斥锁.py

'''
下面模拟一个抢票功能,演示多个进程共享同一个文件操作资源时,由于缺乏竞争机制
导致多个进程同时操作同一个文件时的数据错乱问题.
'''

from multiprocessing import Process
import time,json,random,os


def check_ticket():
    '''查看余票'''
    #time.sleep(random.randint(1, 3))  # 模拟网络延迟
    #f = open('db.txt', 'r', encoding='utf-8')
    #data = f.read()
    #print(data)
    ticket = json.load(open('db.txt','r',encoding='utf-8'))
    left_ticket = ticket['count']
    print("进程%s查看到当前余票还有%s:" %(os.getpid(),left_ticket))

def buy_ticket():
    '''
    买票.
    1.先获取余票数量
    2.如果余票数量大于0,则允许购票
    3.购票后,修改余票数量
    :return:
    '''
    '''查看余票'''
    ticket = json.load(open('db.txt','r',encoding='utf-8'))
    left_ticket = ticket['count']

     #判断余票数量,如果大于0,则库存-1
    if left_ticket > 0:
        # time.sleep(100)
        ticket['count']-=1
        #time.sleep(random.randint(1,3)) #模拟网络延迟
        json.dump(ticket,open('db.txt','w',encoding='utf-8')) #修改数据库
        print("%s 购票成功" %os.getpid())
    else:
        print("%s 购票失败,当前票数%s:" %(os.getpid(),left_ticket))


def task():
    '''
    执行查看余票和购票2个函数
    :return:
    '''
    check_ticket()
    buy_ticket()


if __name__ == '__main__':
    #初始化数据库
    ticket = {"count":1}
    json.dump(ticket, open('db.txt', 'w', encoding='utf-8'))

    '''
    10个子进程并行执行,进行抢票.
    '''
    for i in range(10):
        p = Process(target=task)
        p.start()



