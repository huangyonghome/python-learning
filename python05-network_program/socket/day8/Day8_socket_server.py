# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 22:52
# @Author  : jesse
# @File    : Day7_socket_TCP_server.py

import socket
import os

server=socket.socket()
host=socket.gethostname()
port=6964

server.bind((host,port))

server.listen(5)

while True:
    client,addr = server.accept()

    while True:
        cmd=client.recv(1024)
        print ("执行指令")
        if not cmd:
            print("client is lost")
            break
        cmd_res=os.popen(cmd.decode("utf-8")).read()
        if len(cmd_res) == 0:
            cmd_res = "command is wrong!"
        data_size=len(cmd_res)
        client.send(str(data_size).encode("utf-8"))
        client.send(cmd_res.encode("utf-8"))
        print("send done")

server.close()

