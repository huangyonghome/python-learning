# -*- coding: utf-8 -*-
# @Time    : 2019-06-29 21:32
# @Author  : jesse
# @File    : ftp_server.py

#全栈9期,day32

'''
1.客户端先发送了个4个字节的head头长度
2.客户端发送了head头过来,head头包括了文件名,文件大小
3.客户端循环发送文件


1.服务端先接收4个字节的head头
2.服务端接收上面接收到的头长度的head头
3.服务端循环接收文件,如果接收到的字符长度和head头里的文件大小一样,则说明接收完成
'''


import socket,json,struct,os

#新建一个socket实例对象
server = socket.socket()

#bind一个端口
host = socket.gethostname()
port = 8080
server.bind((host,port))

#侦听端口
server.listen()


#接收客户端的连接

client,client_addr = server.accept()

'''
接收head头部
'''

rec = client.recv(4) #先接收4个字节的head头长度信息

#unpack解压收到的head_len头长度,由于接收到的是个元祖,所以获取第一个元素,也就是head头信息
head_len = struct.unpack('i',rec)[0]

#接收客户端传来的head头.由于已经知道了head头长度,所以接收固定字符串长度

head = client.recv(head_len).decode('utf-8')

#接收到的是一个字符串,用json转成字典

json_head = json.loads(head)


'''
开始接收客户端发送的文件
1.先新建一个同名文件
2.定义一个起始file_size值
3.循环接收文件.直到file_size等于真实文件大小
'''
rec_size = 0

with open(json_head['filename'],'wb') as f:
    while rec_size < json_head['filesize']:
        data = client.recv(4096)
        rec_size += len(data)
        f.write(data)


#接收完成关闭连接
client.close()
server.close()


