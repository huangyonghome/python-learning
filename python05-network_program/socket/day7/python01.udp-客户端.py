# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 22:14
# @Author  : jesse
# @File    : python01.udp-服务端.py

from socket import *

client = socket(AF_INET,SOCK_DGRAM)


while True:

    msg = input(">>:").strip()

    client.sendto(msg.encode('utf-8'),('127.0.0.1',8080))

    data,server_addr = client.recvfrom(1024)

    print(data.decode("utf-8"))
