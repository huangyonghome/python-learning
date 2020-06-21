# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 10:22
# @Author  : jesse
# @File    : tpc-server.py

import socket

sock = socket.socket()

sock.bind(('127.0.0.1',8080))
sock.listen()

while True:
    conn,addr = sock.accept()
    print("your friend {} is online".format(addr))

    while True:
        info = conn.recv(1024)
        info = info.decode('utf-8')
        print("Message from [{}]:{}".format(addr,info))
        if info == 'q' or info == 'Q':
            break
        else:
            while True:
                date = input("please input the messages to be send:")\
                    .strip().encode('utf-8')
                if not date:
                    print("can't be empty")
                    continue
                conn.send(date)
                break
    print("your friend is offline....".format(addr))
    conn.close()
sock.close()