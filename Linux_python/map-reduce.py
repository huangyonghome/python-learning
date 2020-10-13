#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/11 下午2:50
# @Author  : jesse
# @File    : map-reduce.py


from threading import Thread

class Cal():
    def __init__(self,start,end):
        self.result = 0
        self.start = start
        self.end = end


    def map(self):
        for i in range(self.start,self.end):
            self.result += i

    def reduce(self,other):
        self.result += other.result


def generate_worker(data):
    for index in range(1,len(data)):
        cal = Cal(data[index-1], data[index])
        yield cal

def generate_threads(workers):
    for worker in workers:
        thread = Thread(target=work.map)




