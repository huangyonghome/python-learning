# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 22:55
# @Author  : jesse
# @File    : Day7_socket_TCP_client.py

import socket

client = socket.socket()
host = socket.gethostname()
port = 6964

client.connect((host,port))

while True:
    msg = input(">>>:")
    client.send(msg.encode('utf-8'))
    data = client.recv(1024)
    print ('receive from server:',data.decode('utf-8'))