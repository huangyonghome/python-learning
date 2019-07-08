# -*- coding: utf-8 -*-
# @Time    : 2019-06-29 12:04
# @Author  : jesse
# @File    : 时间查询UDP服务器.py

#提供时间查询服务.
#接收客户端消息: 时间格式
#将目前的时间转换成客户端要求的时间格式,发送给客户端

import socket,time

server = socket.socket(type=socket.SOCK_DGRAM)

server.bind(('127.0.0.1',8080))

while True:
    data,client_addr = server.recvfrom(1024)

    #查询当前时间戳
    t = time.time()
    #将时间戳(秒数)转换成结构化时间
    st = time.localtime(t)
    #将结构化时间转换成客户端要求的时间格式
    ft = time.strftime(data.decode("utf-8"),st)

    #将得出的时间格式发送给客户端

    server.sendto(ft.encode("utf-8"),client_addr)

server.close()