# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 22:48
# @Author  : jesse
# @File    : python06.进程间通信-队列.py


#队列.实现主进程和子进程的通信

from multiprocessing import Queue,Process

def run(q):
    for i in range(3):
        # block参数设置False.则队列满异常,因为队列最多只允许3个
        q.put("jesse"+str(i),block=False)


if __name__ == '__main__':
    q = Queue(3)
    p = Process(target=run,args=(q,))
    p.start()
    print(q.get())
    print(q.get())
    print(q.get())
    print(q.get())
    # block设置为False,则异常,因为队列数据已经取完了
    print(q.get(block=False))