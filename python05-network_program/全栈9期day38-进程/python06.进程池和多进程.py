# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 18:59
# @Author  : jesse
# @File    : python06.进程池和多进程.py

'''
比较一下进程池和多进程的执行效率
'''


from multiprocessing import Process,Pool
import time

def fun(n):

    for i in range(10):
        print(n+i)



if __name__ == '__main__':

    #用5个子进程的线程池来并发处理fun函数
    start_time = time.time()
    pool = Pool(5)
    pool.map(fun,range(100))
    print("进程池共耗时",time.time()-start_time)

    #用子进程来处理fun函数

    start_time1 = time.time()
    p_list=[]
    for i in range(100):
        p = Process(target=fun,args=(i,))
        p_list.append(p)
        p.start()


    for p in p_list:
        p.join()

    print("多进程共耗时:",time.time()-start_time1)