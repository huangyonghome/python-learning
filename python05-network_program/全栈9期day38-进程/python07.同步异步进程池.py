# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 22:17
# @Author  : jesse
# @File    : python07.同步异步进程池.py

'''
演示pool的另外2种同步和异步方法
'''

# from multiprocessing import Pool
# import time
# import os
#
# def func(n):
#     print("第%s个进程开始..PID是%s" %(n,os.getpid()))
#     time.sleep(1)
#     print("第%s个进程结束,PID是%s" %(n,os.getpid()))
#
#
# if __name__ == '__main__':
#     pool = Pool(5)
#
#     for i in range(10):
#         # pool.apply(func,args=(i,)) #这是同步阻塞,串行执行
#         pool.apply_async(func,args=(i,)) #这是异步执行,但是主进程不会等待进程池的子进程执行完成才结束
#
#     pool.close() #子进程全部执行完毕
#     pool.join() #主进程接收到子进程结束的信号



#同步调用

# from multiprocessing import Pool
# import os
# import time
# def run(n):
#     print("%s run..." % os.getpid())
#     # 不令其阻塞,结果会同时打印
#     time.sleep(2)
#     return n**2
# if __name__ == '__main__':
#     # 进程池没满就新创建进程执行请求,否则就等待
#     # 注意,这里指定进程池数量为3,会一直是这三个进程在执行,只不过执行的请求可能改变
#     pool = Pool(3)
#     res_list = []
#     for i in range(10):
#         # 获取执行结果,同步运行,会阻塞等待拿到结果,等待过程中无论是否阻塞都会在原地等
#         # 注意等待过程中由于阻塞,其cpu权限会被夺走
#         res = pool.apply(run, args=(i,))
#         res_list.append(res)
#     print(res_list)


#异步调用
from multiprocessing import Pool
import os
import time
def run(n):
    print("%s run..." % os.getpid())
    time.sleep(2)
    return n**2
if __name__ == '__main__':
    # 进程池没满就新创建进程执行请求,否则就等待
    # 注意,这里指定进程池数量为3,会一直是这三个进程在执行,只不过执行的请求可能改变
    pool = Pool(3)
    res_list = []
    for i in range(10):
        res = pool.apply_async(run, args=(i,))
        res_list.append(res)
    pool.close()
    pool.join()
    print(type(res_list),res_list)
    for res in res_list:
        print(res.get())


