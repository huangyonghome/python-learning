# -*- coding: utf-8 -*-
# @Time    : 2017/5/19 10:32
# @Author  : jesse
# @File    : day8_socket_forever_server.py

'''
1.使用socketserver实现多用户同时连接,实现并发.
2.接收用户命令,并且返回命令执行结果给客户端
'''
#socketserver的客户端和普通socket客户端代码一致
import socket

client=socket.socket()

host,port='localhost',6969

client.connect((host,port))

while True:
    cmd=input(">>>:").strip()
    if len(cmd) == 0:continue
    client.send(cmd.encode("utf-8"))
    total_size = client.recv(1024).decode() #接收服务端发送的命令结果字节数
    print(total_size)
    client.send(b"ACK") #给服务端发送一个确认消息
    rec_size=0
    #rec_data=''
    while rec_size < int(total_size): #如果接收到的字节数小于总字节数,说明数据还没传完
        data=client.recv(1024)
        rec_size+=len(data) #累加接收到的长度
        #rec_data+=data
        print(data.decode())
    else:
        print("接收到总字节长度:",rec_size)
        print("服务器发送的长度:",total_size)
        #print(rec_data.decode())



client.close()
