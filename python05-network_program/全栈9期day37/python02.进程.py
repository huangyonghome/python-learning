# -*- coding: utf-8 -*-
# @Time    : 2019-06-23 9:38
# @Author  : jesse
# @File    : python02.进程.py

#开启进程的方法1:

#导入multiprocessing模块的Process类

# from  multiprocessing import Process
# import os
#
#
# def pro(name):
#     print("开启一个子进程:%s" %name)
#     #调用task方法,看看子进程的PPID和PID
#     task()
#
#
#
# def task():
#     # 打印当前进程的父进程PID
#     print("the current process ppid: %s" %os.getppid())
#     #打印当前进程PID
#     print("the current process pid: %s" %os.getpid())
#
#
# #windows下启用进程的写法,需要__name__ = __main__
#
# if __name__ == '__main__':
#
#     #打印当前进程的PPID和PID
#     task()
#
#     '''
#     实例化Process类
#     target: 函数对象
#     args:传入位置参数
#     '''
#     p = Process(target=pro,args=("process1",))
#
#     #调用start方法启动子进程.
#     p.start()


#开启进程的方法2.创建个类继承Process类:

from  multiprocessing import Process
import os

class My_Process(Process):
    #继承并且重写Process的__init__
    def __init__(self,name):
        super().__init__()
        self.name = name

    def run(self):
        '''
        重写Process类的run方法.必须存在run函数.
        因为Process的start()方法就是调用run函数
        :return:
        '''

        print("开启一个子进程:%s" %self.name)
        # 调用task方法,看看子进程的PPID和PID
        self.task()


    def task(self):
        # 打印当前进程的父进程PID
        print("the current process ppid: %s" % os.getppid())
        # 打印当前进程PID
        print("the current process pid: %s" % os.getpid())



# windows下启用进程的写法,需要__name__ = __main__

if __name__ == '__main__':

    '''
    实例化My_Process类
    '''
    p = My_Process(name='jesse')

    # 打印当前进程的PPID和PID
    p.task()

    # 调用start方法启动子进程.
    p.start()

