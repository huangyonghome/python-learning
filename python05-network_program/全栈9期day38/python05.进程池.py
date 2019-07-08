# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 17:37
# @Author  : jesse
# @File    : python05.进程池.py

'''
进程池.有两种

类似于PHP
1.static..固定起一个数量的进程
2.dynamic..定义一个最小进程数,一个最大进程数
'''

from multiprocessing import Pool
import os
import time

def fun(n):
    print("第%s个子进程ID:%s" %(n,os.getpid()))
    time.sleep(n)



if __name__ == '__main__':
    pool = Pool(3) #定义进程池里的进程数量

    pool.map(fun,range(10)) #3个子进程依次执行fun工作


