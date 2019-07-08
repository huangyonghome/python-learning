# -*- coding: utf-8 -*-
# @Time    : 2017-05-19 23:00
# @Author  : jesse
# @File    : ftp_client.py

import json
import socket
import os,os.path
import sys

class FTPclient(object):
    '''
    创建一个客户端类.包括连接服务器,和服务器交互数据.以及发送不同指令的方法
    1.在interactive函数中分析用户的具体指令
    2.使用反射hasattr方法判断是否存在该指令方法

    '''
    def __init__(self):
        self.client=socket.socket()

    def view_bar(self,name,num,total):
        '''
        显示上传,或者下载文件进度条函数
        :param name 文件名称
        :param num 接收或者下载的文件大小
        :param total:总的文件大小
        '''
        rate = num / total #用接收文件大小,除以总文件大小得到一个小数. 比如1/2=0.5
        rate_num = int(rate * 100) #把小数转化成百分比整数.比如将0.5转化成百分比50
        # 格式化字符串,"\r"表示行首打印,接收多少百分比,就打印多少#号和剩余的""空号,直到接收100%
        r = '\r%s[%s%s]%d%%' % (name,"#" * rate_num, " " * (100 - rate_num), rate_num,)
        sys.stdout.write(r) # 终端输出格式化字符串
        sys.stdout.flush() # 刷新屏幕


    def help(self): #ftp程序使用指南
        msg='''
        ftp用法:
        ls
        cd path
        cd ..
        pwd
        mkdir directory
        get filename
        put filename
        '''
        print(msg)

    def connect(self,host,port): #连接服务器
        self.client.connect((host,port))
        self.authenticate()  # 验证用户登录

    def authenticate(self):
        '''
        用户认证函数,传递服务端用户名和密码,如果存在该账号,则服务端返回该用户的磁盘配额
        '''
        while True:
            self.user=input("请输入用户名:").strip()
            self.passwd=input("请输入密码:").strip()
            #创建一个字典传递给服务端
            self.user_dict={
                'username':self.user,
                'password':self.passwd
            }
            self.client.send(json.dumps(self.user_dict).encode("utf-8")) #传递用户密码给服务端认证
            self.server_respond = self.client.recv(1024).decode() #接收服务端返回的数据
            if self.server_respond == "error": #判断用户密码是否输入错误
                print("账号或者密码输入错误,请重新输入")
                continue
            else: # 如果服务端验证成功,则返回一个该用户的磁盘配额
                print("登录成功")
                print("您的剩余空间还有:",self.server_respond)
                break
        self.interactive() #调用交互接口

    def interactive(self):
        while True:
            self.cmd_con = input(">>>:") #等待用户输入命令
            if len(self.cmd_con) ==0:
                continue
            self.cmd = self.cmd_con.split()[0] #获取到用户的命令
            if hasattr(self,"cmd_%s" % self.cmd):  # 使用反射hasattr方法检测是否存在这个命令方法,如果不存在,则提示用户输入错误
                cmd_call=getattr(self,"cmd_%s" % self.cmd)  # 如果存在该命令,则调用相关命令的方法
                cmd_call(self.cmd_con) # 调用方法,同时传递用户的命令
            else:
                print("命令输入错误,请重新输入")
                self.help() #给用户显示使用方法

    def cmd_put(self,*args):#如果用户输入的是put命令.则调用此方法
        '''
        :param args: 接收传递进来的cmd_con变量.此变量包含2个值:put命令和文件名
        args参数是一个元祖类型,要先转换成列表,然后判断列表长度是否大于1(如果列表长度为1,则表示用户只输入了命令,没有输入文件名)
        1.获取文件名
        2.判断文件名本地是否存在
        3.创建一个Json数据,包括指令行为,文件名,文件大小
        '''
        self.cmd_list = args[0].split() #获取用户指令,获得一个列表类型,包括指令和文件名
        if len(self.cmd_list) >1:
            self.filename=self.cmd_list[-1] #获取文件名
            if os.path.isfile(self.filename):#判断文件名是否存在
                self.file_size=os.path.getsize(self.filename) #获取文件的大小
                #创建一个msg_dic字典,包括用户名,密码,指令,文件名,大小等信息传递给服务器
                msg_dic={
                    "username":self.user,
                    "action":'put',
                    "filename":self.filename,
                    "size":self.file_size
                }
                self.client.send(json.dumps(msg_dic).encode("utf-8")) #把文件基础信息发送给服务器
                server_response = self.client.recv(1024).decode() #等待服务器确认,并且等待服务器判断文件是否超过磁盘配额限制
                if server_response == 'error404':#如果服务器传递过来的是404错误,则表示超过磁盘配额
                    print("文件太大,超过磁盘配额")
                    self.client.send(b"get the disk quota") #向服务器获取剩余的磁盘配额
                    quota = self.client.recv(1024).decode()
                    print("磁盘剩余空间:",quota)
                elif server_response == 'ok200': #如果一切正常,则开始上传文件
                    f=open(self.filename,'rb') #读取文件
                    for line in f:
                        self.client.send(line) #发送数据给服务器
                    f.close()
                    print("文件传输完成")
                else:
                    print("上传错误!")
            else:
                print("文件名不存在")


        else: # 如果用户没有指定文件,则打印错误消息
            print("请指定上传的文件名")

    def cmd_get(self,*args): #如果客户端输入get命令,则调用此方法
        '''
        :param args: 接收传递进来的cmd_con变量.此变量包含2个值:get命令和文件名
        args参数是一个元祖类型,要先转换成列表,然后判断列表长度是否大于1(如果列表长度为1,则表示用户只输入了命令,没有输入文件名)
        1.获取文件名
        2.等待服务器判断文件名是否存在
        3.接收服务器传递过来的文件大小
        3.循环接收数据
        '''
        self.get_list = args[0].split()  # 获取用户指令,获得一个列表类型,包括指令和文件名
        if len(self.get_list) > 1:
            self.get_filename = self.get_list[-1]  # 获取文件名
        else:  # 如果用户没有指定文件,则打印错误消息
            print("请指定下载的文件名")
            return
        # 创建一个msg_dic字典,包括用户名,指令,文件名,大小等信息传递给服务器
        msg_dic = {
            "username": self.user,
            "action": 'get',
            "filename": self.get_filename,
        }
        # 发送字典给服务端,等待服务端确认文件是否存在,如果存在则发送文件大小给客户端
        self.client.send(json.dumps(msg_dic).encode("utf-8"))
        self.get_respond = self.client.recv(1024).decode()
        if self.get_respond == "error505": #如果服务端发送错误消息,表示文件不存在
            print("指定的文件名,服务器不存在,请重新输入!")
            return
        else: #如果不是error消息,则表示服务端发送的是文件大小.
            self.get_size = int(self.get_respond)
            self.client.send(b"ACK") #向服务端发送确认消息,表示开始下载文件
        recv_size = 0 #定义一个大小变量
        f=open(self.get_filename,'wb') #打开一个文件,如果有重名文件,直接覆盖
        while recv_size < self.get_size: #循环接收文件
            data=self.client.recv(1024)
            f.write(data)
            recv_size+=len(data)
            self.view_bar(self.get_filename,recv_size,self.get_size) #调用view_bar函数,显示下载进度条


        else:#下载完毕
            f.close()
            print("文件下载完成")

    def cmd_ls(self,*args):
        '''
        :param args: 用户输入的命令
        1.判断args长度是否为1,如果为1,则表示用户输入的是ls命令.如果是2,则表示ls 后面跟着一个路径.(暂时只允许用户查看1个路径下的文件内容)
        2.发送用户名,命令到服务端.
        3.服务端先返回命令结果长度,客户端给一个确认消息
        3.服务端返回ls结果.客户端循环接收
        '''
        self.ls_list = args[0].split()  # 获取用户指令,获得一个列表类型,包括指令和文件名
        if len(self.ls_list) > 2:
            print("命令输入错误,请重新输入")
            return
        elif len(self.ls_list) == 1: #表示用户输入的是ls,后面路径为空
            self.ls_path = False
        else: #如果长度为2,表示ls 后面跟着一个路径
            if self.ls_list[1].startswith("\\"): #判断用户是不是指定了一个绝对路径,如果是则报错
                print("路径错误,不允许绝对路径,请重试")
                return
            else:
                self.ls_path =self.ls_list[1]

        #创建字典,包括用户名,命令,是否携带路径
        msg_dic = {
            "username": self.user,
            "action": 'ls',
            "path": self.ls_path,
        }
        self.client.send(json.dumps(msg_dic).encode("utf-8")) #发送给服务端
        self.ls_result=self.client.recv(1024).decode() #接收服务端数据,如果目录不存在,服务端发送error303,如果存在,则发送ls命令结果的字节长度
        if self.ls_result == "error303": #如果服务端发送错误消息,则表示路径不正确
            print("没有该目录,请重试")
        else:#如果目录正确,服务端发送过来的是一个命令执行结果的大小字节
            self.client.send(b"ACK") #发送确认消息,开始接收数据
            rec_size=0 #定义接收字节变量
            rec_data=""
            while rec_size < int(self.ls_result):
                data=self.client.recv(1024).decode()
                rec_size+=len(data)
                rec_data+=data
            else:
                rec_data = rec_data.split(',') #为了输出显示效果更好,把接收到的字符串格式的data数据,转换成列表,再多行打印.
                for i in rec_data:
                    print(i)

    def cmd_mkdir(self,*args):
        '''
       :param args: 用户输入的命令
       1.判断args长度是否为1,如果为1,则输入错误.如果是2,则表示后面跟着一个目录.如果大于2,则输入错误
       2.发送命令,目录到服务端.
       3.服务端判断该目录是否合法,如果合法则创建一个目录,返回客户端ok200
       4.如果不合法,则返回错误消息
       '''
        self.mkdir_list = args[0].split()  # 获取用户指令,获得一个列表类型,包括指令和文件名
        if len(self.mkdir_list) !=2:
            print("命令输入错误,请重新输入")
            return
        else: #如果长度为2,判断目录是否为相对路径
            if self.mkdir_list[1].startswith("\\"): #判断用户是不是指定了一个绝对路径,如果是则报错
                print("路径错误,不允许绝对路径,请重试")
                return
            else:
                self.mkdir_dir =self.mkdir_list[1]

        # 创建字典,包括用户名,命令,是否携带路径
        msg_dic = {
            "action": 'mkdir',
            "directory": self.mkdir_dir,
        }
        self.client.send(json.dumps(msg_dic).encode("utf-8"))  # 发送给服务端
        self.mkdir_result = self.client.recv(1024).decode()  # 接收服务端数据,如果目录非法,服务端发送error606,否则发送OK606
        if self.mkdir_result != "ok200":  # 如果服务端发送的不是正确消息,则表示目录非法
            print(self.mkdir_result)

    def cmd_cd(self,*args):
        '''
          :param args: 用户输入的命令
          1.判断args长度是否为2,如果不为2,则表示命令输入错误
          2.判断用户输入cd ..还是 cd path
          3.如果cd 目录正确,则进入到该目录.发送ok202消息,否则服务端发送错误消息
          4.如果当前用户是家目录,cd ..会返回一个error202错误
          '''
        self.cd_list = args[0].split()  # 获取用户指令,获得一个列表类型,包括指令和文件名
        if len(self.cd_list) != 2:
            print("命令输入错误,请重新输入")
            return
        else:  # 如果长度为2,表示ls 后面跟着一个路径.(让服务端判读是cd ..还是cd path)
            self.cd_path=self.cd_list[-1]

        # 创建字典,包括命令,带路径
        msg_dic = {
            "action": 'cd',
            "path": self.cd_path
        }
        self.client.send(json.dumps(msg_dic).encode("utf-8"))  # 发送给服务端
        self.cd_result = self.client.recv(1024).decode()  # 接收服务端数据
        if self.cd_result == "error202":  # 如果服务端发送的是error202.则表示目前是在家目录
            print("只允许访问您个人用户目录")
        elif self.cd_result != "ok202": #如果不是正确消息,表示目录非法
            print(self.cd_result)

    def cmd_pwd(self,*args):
        '''
        :param args: 用户输入的命令
        1.判断args长度是否为1,如果不为1 ,则说明命令错误
        2.发送pwd命令到服务端.
        3.服务端返回当前路径名
        '''
        self.pwd_list = args[0].split()  # 获取用户指令,获得一个列表类型,包括指令
        if len(self.pwd_list) != 1:
            print("命令输入错误,请重新输入")
            return
        # 创建字典,包括命令
        msg_dic = {
            "action": 'pwd'
        }
        self.client.send(json.dumps(msg_dic).encode("utf-8"))  # 发送给服务端
        self.pwd_result = self.client.recv(1024).decode()  # 接收服务端发送过来的当前路径名
        print(self.pwd_result)



client=FTPclient()
client.connect('localhost',7000)

