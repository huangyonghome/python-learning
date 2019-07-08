# -*- coding: utf-8 -*-
# @Time    : 2019-06-29 21:32
# @Author  : jesse
# @File    : ftp_client.py


#用struct模块.

#1.客户端先定义一个head头数据.里面包括文件名,文件大小,文件路径.
#2.计算这个head头的长度,然后发送给服务端,服务端根据这个长度来收取head头,避免黏包
#3.循环上传文件.


import  socket,struct,json,os

#新建socket对象

client  = socket.socket()

host = socket.gethostname()
port = 8080

#新建连接
client.connect((host,port))


# 定义一个head头

head = {'filename': r'03 python fullstack s9day30 基于tcp协议的socket.mp4',
        'filedirname': r'E:\Python\全栈9期\day30',
        'filesize': None}

#计算文件大小

filepath = os.path.join(head['filedirname'],head['filename'])

head['filesize'] = os.path.getsize(filepath)


'''
用struct模块发送4个字节的信息,这4个字节主要是告诉服务端,head头长度是多少
然后服务端就可以收取固定长度的head头.避免黏包
'''

#将head字典转为字符串
json_head = json.dumps(head)

#head头长度
head_len = len(json_head.encode('utf-8'))

'''
struct的pack方法将head_len转换为一个固定为4个字符的byte数据.
参数i表示整数类型.
'''
pack_head = struct.pack('i',head_len)


'''
发送4个字节的head_len长度,然后再发送head头到服务端
'''
client.send(pack_head)
client.send(json_head.encode('utf-8'))

'''
开始发送文件
'''


with open(filepath,'rb') as f:
        for line in f:
                #每次发送一行数据
                client.send(line)

client.close()
