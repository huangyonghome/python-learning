# -*- coding: utf-8 -*-
# @Time    : 2019-07-30 23:32
# @Author  : jesse
# @File    : practise.py


def iter():
    while True:
        x = yield
        print('**',x)

iter1 = iter()
# print(iter1)
next(iter1)
iter1.send(1)

# print(iter1.__next__())
# print(iter1.__next__())
# print(iter1.__next__())