# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 22:52
# @Author  : jesse
# @File    : Day7_socket_TCP_server.py

import socket

#下面是一个TCP的服务端例子

server=socket.socket() #创建一个socket对象

host=socket.gethostname()
port=6964

server.bind((host,port)) #绑定本机一个端口

server.listen() #侦听端口

client,addr = server.accept() #获取一个客户端的连接.已经完成了三次握手..这里会阻塞掉

data=client.recv(1024) #收取客户端的消息

client.send(b"Hi,This is a server")

server.close()
