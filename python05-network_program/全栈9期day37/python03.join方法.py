# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 11:09
# @Author  : jesse
# @File    : python03.join方法.py


'''
主进程和子进程同时进行.但是调用join方法,主进程会等待子进程结束后才继续执行.
'''

from multiprocessing import Process

import time,os

def run(name,i):
    print("process %s is starting" %name)
    task()
    time.sleep(i)
    print("child process is done")

def task():
    print("the current process ppid is %s" %os.getppid())
    print("the current process pid is %s" %os.getpid())



if __name__ == '__main__':
    task()
    # p = Process(target=run,args=('jesse',))
    # p.start()

    '''
    主进程这个print动作,会在子进程之前就已经执行了,
    '''
  #  print("main process is done")

    '''加上join方法,主进程会等待子进程执行完毕'''
   # p.join()
   # print("main process is done")


'''
下面这个是多个子进程下调用join方法
'''

from multiprocessing import Process

import time,os

def run(name,i):
    print("process %s is starting" %name)
    task()
    time.sleep(i)
    print("child process is done")

def task():
    print("the current process ppid is %s" %os.getppid())
    print("the current process pid is %s" %os.getpid())


if __name__ == '__main__':

    task() #获取当前进程的PID

    start_time = time.time()

    #实例化3个进程对象
    p1 = Process(target=run, args=('jesse1', 1))
    p2 = Process(target=run, args=('jesse2', 2))
    p3 = Process(target=run, args=('jesse3', 3))

    p_ins = [p1,p2,p3]

    #启动3个进程
    for p in p_ins:
        p.start()

    #等待3个进程执行完毕
    for p in p_ins:
        p.join()

    stop_time = time.time()
    print("main process is done")
    #获取整个程序执行的时间.因为子进程是并发执行的.
    #在p1执行完,p2还需要睡眠1秒,p3需要睡眠2秒...
    #所以以此类推,最大执行时间就是p3的3秒
    #所以这里总共耗时就是P3的子进程执行时间

    print("cost time is: %f" %(stop_time - start_time))