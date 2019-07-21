# -*- coding: utf-8 -*-
# @Time    : 2019-07-07 23:05
# @Author  : jesse
# @File    : python08.进程池的socket_client.py


import socket

client = socket.socket()

client.connect((socket.gethostname(),8080))

res = client.recv(1024)
print(res.decode("utf-8"))
msg = input(">>>:").encode("utf-8")

client.send(msg)

res = client.recv(1024)
print("recieved")

print(res.decode("utf-8"))

client.close()