# -*- coding: utf-8 -*-
# @Time    : 2017-05-17 22:13
# @Author  : jesse
# @File    : day8_ftp_server.py

#编写一个FTP程序

import socket
import os
import os.path
import hashlib

server = socket.socket()
host = socket.gethostname()
port = 6969
server.bind((host,port))
m=hashlib.md5()
server.listen()
conn,addr = server.accept()
print ("等待用户指令")
while True:
    data = conn.recv(1024) # receive the command and the filename from Client
    if not data:  # if send nothing,client has lost
        print("lost client")
    cmd,filename=data.decode().split() # get the command and the filename
    if os.path.isfile(filename): # check if the filename exists
        file_size=os.path.getsize(filename) # get the size of the file
        conn.send(str(file_size).encode()) # send the total size of file to Client
        conn.recv(1024) # receive the ack message from Client
        f = open(filename,'rb') # open the file
        for line in f: # read the file
            m.update(line)
            conn.send(line)
        f.close()
        md5=m.hexdigest()
        print(md5)
        print ("文件传输完成")
        conn.send(md5.encode())

server.close()
