# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 22:59
# @Author  : jesse
# @File    : python08.进程池的socket_server.py

'''
演示进程池在socket中的使用
'''


from  multiprocessing import Pool
import socket
import os


def talk(conn):
    print(os.getpid())
    conn.send(b'hello')
    res = conn.recv(1024)
    print(res.decode("utf-8"))
    # msg = input(">>>:")
    # print(os.getpid())
    # conn.send(msg.encode("utf-8"))
    # print("send finishied")



if __name__  == "__main__":
    server = socket.socket()
    server.bind((socket.gethostname(), 8080))
    server.listen()

    pool = Pool(5) #开启5个子进程

    while True:
        conn, conn_client = server.accept()  #循环等待客户端的连接
        pool.apply_async(talk,args=(conn,))  #采用异步的方式执行talk函数,也就是服务端和客户端是实际交互

    conn.close()
    server.close()