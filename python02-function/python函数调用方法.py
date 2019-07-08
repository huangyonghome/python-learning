# -*- coding: utf-8 -*-
# @Time    : 2019-06-30 17:09
# @Author  : jesse
# @File    : python函数调用方法.py

'''
当实例化对象调用任何方法时,要先从最底层的子类开始主机向上寻找
在父类中调用方法,如果这个方法在父类和子类都同时存在,那么会调用子类的方法

'''


class A:
    def __init__(self):
        self.request()

    def middle(self):
        self.request()


    def request(self):
        print("call request method of parent A Class")



class B(A):

    def request(self):
        print("call request method of B class")



class C(B):





    def request(self):
        print("call request method of C class")


ins = C()

ins.middle()