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
    server=client.recv(1024).decode()
    print(server)

client.close()