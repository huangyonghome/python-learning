# -*- coding: utf-8 -*-
# @Time    : 2017-05-20 11:09
# @Author  : jesse
# @File    : socket_server_temp.py
# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 22:52
# @Author  : jesse
# @File    : Day7_socket_TCP_server.py

import socket
import os

server=socket.socket()
host=socket.gethostname()
port=6964

server.bind((host,port))

server.listen(5)

while True:
    client,addr = server.accept()

    while True:
        cmd=client.recv(1024)
        client.send("1024M".encode("utf-8"))

server.close()
