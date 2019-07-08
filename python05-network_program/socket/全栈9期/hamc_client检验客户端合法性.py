# -*- coding: utf-8 -*-
# @Time    : 2019-06-30 11:43
# @Author  : jesse
# @File    : hamc_client检验客户端合法性.py

'''
hmac模块有点类似于hashlib模块的加盐加密
用Hamc模块来比较本地的秘钥和客户端发送过来的秘钥是否一致.

1.定义1个固定的secret_key,以及从客户端接收到的随机字符串
2.用hmac.new方法将2个字符串实例化为一个对象
3.用实例对象的digest生成一个秘钥
4.将该秘钥发送给服务端,以便服务端监测是否合法

'''

import socket,hmac

client = socket.socket()
client.connect((socket.gethostname(),8080))

#定义一个secret_key

secret_key = b'egg1'

#从客户端接收随机字符串

secret_byte = client.recv(1024)

#将2个字符串实例化一个对象

h = hmac.new(secret_key,secret_byte)

#将该对象加密

client_digest = h.digest()

#将该秘钥发送给服务端

client.send(client_digest)

