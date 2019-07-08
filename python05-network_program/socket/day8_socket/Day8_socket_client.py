
# @File    : Day7_socket_TCP_client.py

import socket

client=socket.socket()  #实例化一个socket对象.

host=socket.gethostname()
port=6969

client.connect((host,port)) #连接服务器端的IP地址和端口

while True:
    cmd=input(">>>")
    if len(cmd) == 0:continue #不能发送空消息,如果输入为空,则继续下一轮循环
    client.send(cmd.encode("utf-8")) #客户端发送指令 . 把命令发送给服务器
    cmd_size=client.recv(1024).decode() #接收服务器端返回结果 .服务器先返回一个命令执行结果的长度
    print("服务器发送长度:",cmd_size)

    client.send(b"ACK") #客户端收到服务器第一次send过来的数据包长度时,发送一个确认消息给服务端
    rec_size=0
    rec_data=b''
    while rec_size < int(cmd_size): #判断当前接收到的字节大小是否小于服务器端发送过来的总字节大小.如果小于,则继续接收
        data=client.recv(1024)
        rec_size+=len(data)  #每接收一次,则当前接收的字节数加上本次接收的数据长度,
        rec_data+=data #总数据加上本次接收的实际数据

    else: #while语句执行完,则执行else.说明接收到的字节长度等于或者大于服务器发送的长度
        print("实际收到长度:",rec_size)
        print (rec_data.decode())  #显示服务器返回来的命令执行结果
