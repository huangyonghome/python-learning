# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 8:20
# @Author  : jesse
# @File    : python.02生产消费者模型.py

'''
用进程队列模拟生产者和消费者
'''
from multiprocessing import Process,Queue
import time,random

def consumer(name,q):

    while True:
        #如果所有消费者都接收到一个None,说明生产者已经结束.此时消费者也应该结束
        food = q.get()
        if not food:
            print('\033[32m{}接收到None\033[0m'.format(name))
            break

        print('\033[31m{}吃掉了{}\033[0m'.format(name,food))


def producer(name,food,q):

    for i in range(5):
        time.sleep(random.randint(1,3))
        foo = '{}生产了{}{}'.format(name,food,i)
        print(foo)
        q.put(food+str(i))



if __name__ == '__main__':
     q = Queue()
     p1 = Process(target=producer,args=('jesse','包子',q))
     p1.start()
     p2 = Process(target=producer, args=('Lyon', '油条', q))
     p2.start()
     c1 = Process(target=consumer, args=('Alex',q))
     c1.start()
     c2 = Process(target=consumer, args=('wusir', q))
     c2.start()

     #为了解决消费者无限等待生产者的问题
     #主进程等待生产者生产结束..此时往队列里加个None.
     #由于有2位消费者,所以要put2次.否则其中一个消费者接收到None,另外一个消费者还是会继续等待
     p1.join()
     p2.join()
     q.put(None)
     q.put(None)