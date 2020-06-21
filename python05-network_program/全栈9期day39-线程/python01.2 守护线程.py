# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 8:58
# @Author  : jesse
# @File    : python01.2 守护线程.py

"""
join方法是等所有子线程执行完毕,而守护线程则完全相反.
守护线程机制是只要主线程执行完毕,立刻退出,而不管子线程有没有执行完毕

守护线程方法是setDaemon().

无论是守护进程还是守护线程,会等待主进程(线程)运行完毕后被销毁

"""

import threading,time


#此时,主线程会执行完毕,程序自动退出,而t1,t2这2个子线程还没执行完毕.

# def run(name):
#     print("my name is %s" %name)
#     #睡2s
#     time.sleep(2)
#     print("%s wake up,keep working" %name)
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run,args=('jesse',))
#     t2 = threading.Thread(target=run,args=('Lyon',))
#
#     #设置守护线程,必须在启动前设置
#     t1.setDaemon(True)
#     t2.setDaemon(True)
#
#     t1.start()
#     t2.start()
#
#     print("I am the main thread.i am done to run")


#由于t2没有设置守护线程,t1设置了守护线程.主程序会等待t2执行完毕退出,
#而t1此时由于多睡了1s,所以还未执行就被退出了

# def run(num):
#     print("my name is %s" % num)
#     # 睡2s
#     time.sleep(int(num))
#     print("%s wake up,keep working" % num)
#
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run, args=('3',))
#     t2 = threading.Thread(target=run, args=('2',))
#
#     # 设置守护线程,必须在启动前设置
#     t1.setDaemon(True)
# #    t2.setDaemon(True)
#
#     t1.start()
#     t2.start()
#
#     print("I am the main thread.i am done to run")

#主线程阻塞调用

# def run(num):
#     print("I like num %d" %num)
#     time.sleep(2)
#     print("%s wake up,i am keep working" %num)
#
# def main():
#     for i in range(1,6):
#         #创建线程实例
#         t = threading.Thread(target=run,args=(i,))
#         #启动线程
#         t.start()
#         #阻塞调用
#         t.join()
#
# if __name__ == '__main__':
#     #创建一个主线程.调用main函数,而不是run
#     m = threading.Thread(target=main,args=[])
#
#     #设置为守护线程
#     m.setDaemon(True)
#
#     #启动主线程
#     m.start()
#     print("I am the main thread")
#
#     #阻塞调用
#     m.join()


# 给阻塞调用设置一个超时时间

def run(num):
    print("I like num %d" %num)
    time.sleep(2)
    print("%s wake up,i am keep working" %num)

def main():
    for i in range(1,6):
        #创建线程实例
        t = threading.Thread(target=run,args=(i,))
        #启动线程
        t.start()
        #阻塞调用
        t.join()

if __name__ == '__main__':
    #创建一个主线程.调用main函数,而不是run
    m = threading.Thread(target=main,args=[])

    #设置为守护线程
    m.setDaemon(True)

    #启动主线程
    m.start()
    print("I am the main thread")

    #阻塞调用
    m.join(4)