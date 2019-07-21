# -*- coding: utf-8 -*-
# @Time    : 2019-07-10 21:18
# @Author  : jesse
# @File    : python09.进程池的返回值.py

from multiprocessing import Pool
import time
import os
#
# def func(i):
#     time.sleep(0.5)
#     return i*i
#
#
#
# if __name__ == "__main__":
#
#     p = Pool(5)
#
#     for i in range(10):
#         # res = p.apply(func,args=(i,)) #apply的结果就是func的返回值
#         # print(res)
#
#         # res = p.apply_async(func,args=(i,))
#         # print(res.get()) #如果是用apply_async,则get方法会阻塞
#
#         res = p.map(func,range(10))
#         print(res)



def func(i):

    print("func:",os.getpid())
    return i+1


def func1(n):
    print("func1:",os.getpid())
    print(n*n)



if __name__ == '__main__':
    print("main:",os.getpid())
    p = Pool(5)


    p.apply_async(func,args=(10,),callback=func1)
    p.close()
    p.join()

