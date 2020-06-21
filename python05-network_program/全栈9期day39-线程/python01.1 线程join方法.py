# -*- coding: utf-8 -*-
# @Time    : 2020-06-21 8:48
# @Author  : jesse
# @File    : python01.1 线程join方法.py

import threading,time


#结果分析.主线程会自动一直执行,而不等待子线程执行完毕

# def run(name):
#     print("my name is %s" %name)
#     #睡2s
#     time.sleep(2)
#     print("wake up,keep working")
#
# if __name__ == '__main__':
#     t1 = threading.Thread(target=run,args=('jesse',))
#     t2 = threading.Thread(target=run,args=('Lyon',))
#
#     t1.start()
#     t2.start()
#     print("I am the main thread.i am done to run")


#join方法表示需要等待所有子线程执行完毕,主线程才继续往下执行

def run(name):
    print("my name is %s" %name)
    #睡2s
    time.sleep(2)
    print("%s wake up,keep working" %name)

if __name__ == '__main__':
    t1 = threading.Thread(target=run,args=('jesse',))
    t2 = threading.Thread(target=run,args=('Lyon',))

    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("I am the main thread.i am done to run")
