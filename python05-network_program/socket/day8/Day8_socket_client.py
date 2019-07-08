# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 22:55
# @Author  : jesse
# @File    : Day7_socket_TCP_client.py

import socket

client = socket.socket()
host = socket.gethostname()
port = 6964

client.connect((host,port))
rec_size=0
while True:
    cmd=input(">>>:")
    client.send(cmd.encode("utf-8"))
    cmd_size=client.recv(1024) #接收服务端发过来的命令长度
    print("命令结果大小:",cmd_size)
    while rec_size <= int(cmd_size.decode()):
        data = client.recv(1024)
        rec_size+=len(data)
        print(data.decode("utf-8"))
        print("总共收到:,",rec_size)

client.close()