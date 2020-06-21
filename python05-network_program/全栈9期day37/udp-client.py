# -*- coding: utf-8 -*-
# @Time    : 2020-06-20 12:42
# @Author  : jesse
# @File    : udp-client.py

import socket
sock = socket.socket(type=socket.SOCK_DGRAM)

host = socket.gethostname()
port = 8081


while True:
    info = input("message input:").strip().encode("utf-8")
    if not info:
        print("can't be empty")
        continue
    elif info == 'q' or info == "Q":
        break
    else:
        sock.sendto(info,(host,port))
        data,addr = sock.recvfrom(1024)
        data = data.decode('utf-8')
        print("receive message from [{}]:{}".format(addr,data))
sock.close()