# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 10:48
# @Author  : jesse
# @File    : Day7_socket_TCP_server.py

import socket

server=socket.socket()

host=socket.gethostname()
port=6969

server.bind((host,port))
server.listen()

conn,addr=server.accept()


while True:

    data=conn.recv(1024)
    print("received from client:", data)
    conn.send(data)



server.close()