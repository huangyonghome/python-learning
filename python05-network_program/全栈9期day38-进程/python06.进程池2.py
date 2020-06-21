# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 18:45
# @Author  : jesse
# @File    : python06.进程池2.py


from multiprocessing import Pool
from time import sleep
from datetime import datetime
import os

class forMap:
    def __init__(self):
        self.name = '没啥用的初始化'

    def forPrinit(self, i):
        print(os.getpid())
        # sleep(i)
        # print(i)
        return i ** 2


if __name__ == '__main__':
    s = datetime.now()
    tt = forMap()
    # 进程池中创建两个进程，调用计算机的两个内核去帮我做事。
    p = Pool(3)

    l = [2, 4, 6]
    rList = p.map(tt.forPrinit, l)
    print("rList",rList)

    p.close()
    p.join()

    e = datetime.now()
    print('多进程执行时间：', e - s)