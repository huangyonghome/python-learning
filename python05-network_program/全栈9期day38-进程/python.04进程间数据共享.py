# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 14:15
# @Author  : jesse
# @File    : python.04进程间数据共享.py

'''
Manager组件实现主进程和子进程数据共享

'''

# from multiprocessing import Manager,Process
#
#
#
# def func(dic):
#
#     dic['count'] -= 1
#
#
# if __name__ == '__main__':
#     m = Manager()
#
#     dic = m.dict({'count':100})
#     p_list=[]
#
#     for i in range(50):
#         p = Process(target=func,args=(dic,))
#         p.start()
#         p_list.append(p)
#
#     for i in p_list:i.join()
#     print("主进程:",dic)


'''
以上代码执行后,每次结果都不一样,并不是每次count都减去了50.
这是因为可能存在多个子进程同时修改一份数据的情况,
为了避免这种现象,就需要给子进程加锁,一次只允许修改一个子进程修改一个数据
但是这样,代码执行效率会有影响.执行速度明显慢了许多
'''


#
# from multiprocessing import Manager,Process,Lock
#
#
#
# def func(dic,mutex):
#
#     mutex.acquire()
#     dic['count'] -= 1
#     mutex.release()
#
# if __name__ == '__main__':
#     m = Manager()
#     mutex = Lock()
#
#     dic = m.dict({'count':100})
#     p_list=[]
#
#     for i in range(50):
#         p = Process(target=func,args=(dic,mutex))
#         p.start()
#         p_list.append(p)
#
#     for i in p_list:i.join()
#     print("主进程:",dic)