# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 10:52
# @Author  : jesse
# @File    : Day7_socket_TCP_client.py

import socket

client=socket.socket()

host=socket.gethostname()
port=6969

client.connect((host,port))

while True:
    msg=input(">>>")

    client.send(msg.encode("utf-8"))

    data=client.recv(1024)

    print ("I received from server:",data.decode())