# -*- coding: utf-8 -*-
# @Time    : 2017/5/12 10:48
# @Author  : jesse
# @File    : Day7_socket_TCP_server.py

import socket
import os

server=socket.socket() #实例化一个socket对象.

host=socket.gethostname()
port=6969

server.bind((host,port)) #绑定IP地址和端口
server.listen() #侦听端口

while True:
    print("等待接受新指令")
    conn,addr = server.accept()  #获得客户端实例化对象和地址.conn是socket的客户端对象,addr是客户端的IP地址和端口
    while True:
        cmd=conn.recv(1024)  #接收客户端发送过来的命令
        if not cmd:  #如果没有命令进来,就等待客户端输入
            print("等待用户输入")
        cmd_res=os.popen(cmd.decode("utf-8")).read() #执行命令
        if len(cmd_res) == 0:  #如果命令执行没有结果,则显示错误命令
            cmd_res="wrong command"
        conn.send(str(len(cmd_res)).encode("utf-8")) #先发送命令执行结果的长度给客户端
        ack_rec=conn.recv(1024)  #先接受一个客户端发送过来的确认消息,如果客户端没有发送确认,则程序会一直卡在这里,
        conn.send(cmd_res.encode("utf-8")) #发送命令的执行结果给客户端.如果命令没有执行结果,则发送的是"wrong command"
        print ("send done")

server.close()



server.close()