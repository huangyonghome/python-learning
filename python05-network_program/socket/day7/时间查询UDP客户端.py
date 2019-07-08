# -*- coding: utf-8 -*-
# @Time    : 2019-06-20 22:14
# @Author  : jesse
# @File    : python01.udp-服务端.py


#定义一个需要的时间格式,发送给服务端,然后接收到具体时间日期信息


import socket
client = socket.socket(type=socket.SOCK_DGRAM)

ip_Port = ('127.0.0.1',8080)

while True:

    time_structure = input(">>:").strip().encode("utf-8")

    client.sendto(time_structure,ip_Port)

    data,server_addr = client.recvfrom(1024)

    print(data.decode("utf-8"))
