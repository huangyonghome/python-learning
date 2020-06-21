# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 10:38
# @Author  : jesse
# @File    : udp-server.py

import socket

sock = socket.socket(type=socket.SOCK_DGRAM)
host = socket.gethostname()
port = 8081
sock.bind((host,port))

while True:
    data,conn = sock.recvfrom(1024)
    data = data.decode('utf-8')
    print("Receive a message from [{}]:{}"\
          .format(conn,data))
    if data == 'q' or data == 'Q':
        break
    while True:
        info = input("please input message:")\
            .strip().encode('utf-8')
        if not info:
            print("can't be empty")
            continue
        sock.sendto(info,conn)
        break
sock.close()