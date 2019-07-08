# -*- coding: utf-8 -*-
# @Time    : 2017-05-14 15:35
# @Author  : jesse
# @File    : socket_client_ubuntu.py

# -*- coding: utf-8 -*-
# @Time    : 2017-05-11 22:55
# @Author  : jesse
# @File    : Day7_socket_TCP_client.py

import socket
import os
import os.path

client = socket.socket()
host = socket.gethostname()
port = 6964
f = open('vedio', 'wb')
client.connect((host, port))
last_data = 0
i=0
while True:
    msg = raw_input(">>>:")
    client.send(msg)
    while True:
        # msg = raw_input(">>>:")
        # client.send(msg)
        data = client.recv(10240000)
        f.write(data)
        f.flush()
        if last_data != len(data):
            last_data=len(data)
        elif last_data == len(data) and i<5:
            i+=1
        else:
            print("transmission is done")
            break
        print ("last_data:",last_data)
        print ("cur_data:",len(data))
        print ("i:",i)




