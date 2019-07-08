# -*- coding: utf-8 -*-
# @Time    : 2017/5/19 10:32
# @Author  : jesse
# @File    : day8_socket_forever_server.py

'''
1.使用socketserver实现多用户同时连接,实现并发.
2.接收用户命令,并且返回命令执行结果给客户端
'''
import socketserver
import os

#第一步:创建一个类,并且是基于socketserver的BaseRequestHandler的子类
class mysocket(socketserver.BaseRequestHandler):
    #第二步:重构父类的handle方法.服务器接收数据,和客户端交互都是在handle方法中完成
    def handle(self):
        while True:
            self.cmd=self.request.recv(1024).strip() #使用self.request.recv来接收客户端消息.
            if not self.cmd:
                print("客户端断开")
                break
            self.cmd_res=os.popen(self.cmd.decode("utf-8")).read() #得出命令执行结果
            if len(self.cmd_res) == 0: #如果没有执行结果,则说明命令错误
                self.cmd_res="wrong command"
            else: #如果有执行结果,则先发送命令结果的数据包长度,解决粘包
                self.request.send(str(len(self.cmd_res.encode())).encode("utf-8")) #发送命令结果的字节长度给客户端
            self.request.recv(1024) #接收客户端的确认消息

            self.request.send(self.cmd_res.encode("utf-8")) #使用self.request.send发送消息给客户端.这次发送实际数据


#第三步:实例化一个socketserver.TCPServer或者socketsever.UDPServer类对象,并且传递服务端地址和上面创建的类名

host,port='localhost',6969

server=socketserver.ThreadingTCPServer((host,port),mysocket) #把服务端地址,还有创建的子类传递给socketserver

#第四步:调用serve_forever()实现多用户同时连接服务端
server.serve_forever()

server.server_close() #关闭服务端
