# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 22:14
# @Author  : jesse
# @File    : python01.udp-服务端.py

# import socket
#
# server = socket(socket.AF_INET,socket.SOCK_DGRAM)


#UDP服务端不需要进行监听,也不需要建立连接.在启动服务之后只能被动的等待客户端发送消息.
#客户端发送消息过来还会携带客户端的地址,服务端回复消息的时候需要指定客户端地址

import socket

server = socket.socket(type=socket.SOCK_DGRAM)

server.bind(('127.0.0.1',8080))

while True:

#发送过来的也是2个参数
    data,client_addr = server.recvfrom(1024)

    print(data.decode("utf-8"))

#sendto方法需要两个参数:1.byte类型的数据.2.对方的地址
    server.sendto(data.upper(),client_addr)