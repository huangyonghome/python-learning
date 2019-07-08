# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 8:20
# @Author  : jesse
# @File    : python.02生产消费者模型.py

'''
用进程队列模拟生产者和消费者.
用joinableQueue来解决消费者一直阻塞无法感知生产者已经生产结束问题

'''
from multiprocessing import Process,JoinableQueue

import time,random

def consumer(name,q):

    while True:

        food = q.get()
        print('\033[31m{}吃掉了{}\033[0m'.format(name,food))

        #task_done方法标志消费者已经处理完了这条消息
        #每处理完一条消息,计数器就减1
        q.task_done()


def producer(name,food,q):

    for i in range(5):
        time.sleep(random.randint(1,3))
        foo = '{}生产了{}{}'.format(name,food,i)
        print(foo)
        q.put(food+str(i))

    #joinablequeue的join方法会将每次生产的消息计数器加1.
    #然后会接收到comsumer的task_done计数器减1.
    # 这里是阻塞的.直到计数器减到0..也就标志着消费者全部消费完.
    q.join()



if __name__ == '__main__':

    #用JoinableQueue方法替代Queue
     q = JoinableQueue()
     p1 = Process(target=producer,args=('jesse','包子',q))
     p1.start()
     p2 = Process(target=producer, args=('Lyon', '油条', q))
     p2.start()
     c1 = Process(target=consumer, args=('Alex',q))
     c2 = Process(target=consumer, args=('wusir', q))

     '''
    在c1,c2启动前,把他们设置为守护进程
    守护进程的作用是,当主进程结束,守护进程自动结束
     '''
     c1.daemon = True
     c2.daemon = True
     c1.start()
     c2.start()

     '''
    #当生产者的q.join方法结束,也就标志着消费者也已经全部消费完了.
    #此时主进程等待生产者结束,主进程也就结束了
    #由于守护进程的缘故,主进程结束,消费者也就结束了.
    #所以即使消费者没有采取任何跳出while循环的措施.但是进程也会和主进程一起结束
     '''

     p1.join()
     p2.join()
