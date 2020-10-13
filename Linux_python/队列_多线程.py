#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/6 下午8:28
# @Author  : jesse
# @File    : 队列_多线程.py

import subprocess
import threading
# from Queue import Queue
# from Queue import Empty

import queue


def call_ping(ip):
    if subprocess.call("ping -c 1 -W1 {} > /dev/null 2>&1".format(ip),shell=True):
        print("{0} is unreachable".format(ip))

    else:
        print("{0} is alive".format(ip))


def is_reacheable(q):
    while True:
        if not q.empty():
            ip = q.get()
            call_ping(ip)
        else:
            break

def main():
    q = queue.Queue()
    for i in range(250):
        ip = '172.16.10.' + str(i)
        q.put(ip)

    threads = []
    for i in range(10):
        thr = threading.Thread(target=is_reacheable,args=(q,))
        thr.start()
        threads.append(thr)

    for thr in threads:
        thr.join()


if __name__ == '__main__':
    main()