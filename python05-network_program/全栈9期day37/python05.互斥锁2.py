# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 15:43
# @Author  : jesse
# @File    : python05.互斥锁.py

'''
在互斥锁.py的文件代码中得知,所有进程都能获取余票且购票.
所以需要一个机制能确保只能有一个进程购票,也就是说所有进程获取的库存(余票)是最新,最准确的
这个机制就是互斥锁..互斥锁实现了同一时刻,只能同一个进程使用某个资源.
只有当该进程执行完毕,释放锁后,其他进程才能拿到锁,使用资源,然后再释放.....

'''

#导入Lock互斥锁模块
from multiprocessing import Process,Lock
import time,json,random,os


def check_ticket():
    '''查看余票'''
    #time.sleep(random.randint(1, 3))  # 模拟网络延迟
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


def task(mutex):
    '''
    执行查看余票和购票2个函数
    :return:
    '''
    check_ticket()
    '''
    在查看当前余票的时候可以并发执行,允许获取余票的信息有一定的滞后性
    也就是说,获取的余票数量并不是真实数量,只有在购买页面获取的信息才是准确的
    '''
    #在购买票动作前上互斥锁
    mutex.acquire()
    buy_ticket()
    #购买票完成后,释放锁
    mutex.release()

if __name__ == '__main__':
    #初始化数据库
    ticket = {"count":1}
    json.dump(ticket, open('db.txt', 'w', encoding='utf-8'))

    #实例化一个互斥锁对象
    mutex = Lock()
    '''
    10个子进程并行执行,进行抢票.将主进程的互斥锁实例传入子进程.
    这样所有子进程使用同一把锁
    '''
    for i in range(10):
        p = Process(target=task,args=(mutex,))
        p.start()


#以上代码确保了只有一个进程优先获得购买票的权限.

'''
但是这里还有个问题就是.如果这个获得锁的进程不购票,一直等待状态.
那么其他进程也相当于卡死了.
'''
