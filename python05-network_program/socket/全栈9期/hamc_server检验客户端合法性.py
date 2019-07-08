# -*- coding: utf-8 -*-
# @Time    : 2019-06-30 11:42
# @Author  : jesse
# @File    : hamc_server检验客户端合法性.py

'''
hmac模块有点类似于hashlib模块的加盐加密
用Hamc模块来比较本地的秘钥和客户端发送过来的秘钥是否一致.

1.定义1个固定的secret_key,以及1个随机的字符串
2.用hmac.new方法将2个字符串实例化为一个对象
3.用实例对象的digest生成一个秘钥
4.用hmac.compare方法将本地的hmac.digest和从客户端接收到的hmac.digest进行对比.
  如果一致则说明客户端是合法的

'''

import socket,hmac,os

secret_key = b'egg' #2个字符串都要byte类型
server = socket.socket()
server.bind((socket.gethostname(),8080))
server.listen()
conn,addr = server.accept()


#定义检验合法性函数

def check_valid(conn):
    '''
    用hmac模块检验本地的密文和客户端发送的密文是否一致
    :param conn:
    :return:
    '''

    #新建一个随机的32位长度的byte类型的随机字节
    secret_byte = os.urandom(32)

    #将这个随机字节发送给客户端
    conn.send(secret_byte)

    #实例化一个对象为2个字符串
    h = hmac.new(secret_key,secret_byte)

    #将该对象加密,得到一个最终的秘钥
    digest= h.digest()

    #从客户端接收客户端发来的秘钥

    client_digest = conn.recv(1024)

    #加密服务端本地和客户端的秘钥,如果一致则为True,否则为False

    return hmac.compare_digest(digest,client_digest)


#调用checK_valid函数

res = check_valid(conn)

#如果结果为True

if res:
    print("是个合法的客户端")
    conn.close()

else:
    print("客户端非法!!!")
    conn.close()


