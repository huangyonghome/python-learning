# -*- coding: utf-8 -*-
# @Time    : 2017-05-17 22:27
# @Author  : jesse
# @File    : day8_ftp_client.py

#FTP程序客户端

import socket
import hashlib
client = socket.socket()
host = socket.gethostname()
port=6969
m=hashlib.md5()
client.connect(('192.168.10.202',6969))

while True:
    cmd=input(">>>:").strip()
    if len(cmd) == 0:continue # none message is not allowd to send
    if cmd.startswith("get"):  # if Client download file from Server
        client.send(cmd.encode("utf-8")) # send command and filename to Server, request to download a file
        file_size = client.recv(1024).decode() # receive the file size from Server
        client.send(b"ACK") # send the ACK message to Server
        rec_size = 0 # set a variable of received file size
        filename = cmd.split()[1] # get the filename which user input
        f = open(filename + '.new','wb')  # create a file to write the data which received from server.
                                          # because the Client and Server exist in the same dir, so rename the file
        while rec_size < int(file_size):  # if received size less than total size ,then continue to receive
            data = client.recv(1024) # receive the real file contents
            m.update(data)
            rec_size+=len(data) # accumulate received size
            f.write(data) # write file
        else:
            md5=m.hexdigest()
            f.close()
            server_md5=client.recv(1024)
            print("文件传输完成")
            print("文件md5:",md5)
            print("服务端文件md5:",server_md5)
            print("总共收到文件大小:",rec_size)
            print("文件总共大小:",file_size)
client.close()