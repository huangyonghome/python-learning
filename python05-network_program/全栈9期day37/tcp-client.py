# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 10:31
# @Author  : jesse
# @File    : tcp-client.py

import socket
sock = socket.socket()
sock.connect(('127.0.0.1',8080))

while True:
    info = input("please input your message:")\
        .strip().encode('utf-8')

    if not info:
        print("can't be empty")
        continue

    elif info == 'q' or info == 'Q':
        break

    else:
        sock.send(info)
        data = sock.recv(1024).decode('utf-8')
        print("message from [{}]:{}".format(('127.0.0.1',8080),data))

sock.close()