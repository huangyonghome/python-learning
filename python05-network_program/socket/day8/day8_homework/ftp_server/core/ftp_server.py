# -*- coding: utf-8 -*-
# @Time    : 2017-05-19 22:53
# @Author  : jesse
# @File    : ftp_server.py

import socketserver
import json
import os,os.path
import sys
sys.path.append('..')
from conf import account


class Mysocket(socketserver.BaseRequestHandler):

    def authentication(self):
        '''
        1.获取客户端传递的用户密码.暂时没有使用md5加密
        2.从account账户文件读取账户,验证客户端输入的账号密码是否匹配
        3.使用while True循环接收用户发送的账号密码,一旦验证成功返回主函数
        4.从account文件获取用户家目录,磁盘配额限制
        '''
        self.finding = False #设定一个标记,解决for循环重复发error消息的Bug
        self.user_dict = account.user_info  # 获取用户账号文件信息
        # 服务器认证用户账号登录信息,登录成功返回用户一个磁盘配额
        while True:
            self.account = self.request.recv(1024).decode() # 接收服务器传递过来的用户账号信息
            self.user_account=json.loads(self.account) #获取用户传递过来的账号,密码字典
            self.user_name=self.user_account['username'] #获取用户输入的用户名
            self.user_passwd=self.user_account['password'] #获取用户输入的密码
            for dict in self.user_dict:
                for k,v in dict.items(): #读取account列表里的内嵌字典
                    if k == self.user_name: # 如果存在该账号,则判断密码是否正确
                        if v['passwd'] == self.user_passwd: #判断密码是否正确
                            self.quota = v['quota'] #如果账号,密码都正确则获取该用户的磁盘配额
                            self.home = v['home'] #获取该用户的初始目录
                            self.current_dir=self.home #获取用户的当前工作目录
                            print("账户验证成功")
                            self.request.send(self.quota.encode("utf-8")) #发送磁盘配额信息给客户端
                            self.finding = True
            if self.finding == True: # 如果为True,则表示通过验证,结束while循环
                break
            else: #如果finding为false,则表示顶层的for循环没有找到该账户,或者没有通过验证.则等for循环结束后一次性发送error错误消息
                  #这个问题调试了半个小时,如果在for循环语句中发送error消息,则一次for循环没找到账户,就发送一次error,多次for循环则发送多次error,
                  #所以for迭代完成,客户端会收到多个error错误,这样就会产生Bug
                self.request.send("error".encode("utf-8")) # 发送error消息

    def put(self,*args):
        '''
        :param args: 客户端传递的字典参数,包含用户名,指令,文件名,文件大小
        1.获取文件名,判断文件名是否存在,这里就默认如果文件存在直接覆盖
        2.获取文件大小,判断用户上传的文件是否超过磁盘配额
        3.传递一个客户端一个确认消息,如果允许上传则发送ok200,否则发送error404
        4.写入文件
        '''
        self.put_dict = args[0] # 获取客户端put方法传递过来的msg_dic字典
        self.put_filename = self.put_dict['filename'] #获取文件名
        #self.put_user = self.put_dict['username'] #获取用户名
        self.put_filesize = self.put_dict['size'] #获取文件大小
        put_rec_size=0
        if self.put_filesize > int(self.quota): #判断是否超过磁盘配额,
            self.request.send("error404".encode("utf-8")) #发送错误消息给客户端
            self.request.recv(1024)
            self.request.send(self.quota.encode()) #发送用户磁盘配额剩余空间
            return # 返回handle
        else:
            self.request.send("ok200".encode("utf-8")) #发送Ok给客户端,提示可以传送文件了
            f = open(self.current_dir+self.put_filename,'wb')
            while put_rec_size < int(self.put_filesize): #循环接收数据
                data = self.request.recv(1024)
                put_rec_size+=len(data)
                f.write(data)
            else: #文件传完后,更新self.quota的值.
                print("文件上传完成")
                self.quota = int(self.quota)-put_rec_size

    def get(self,*args):

        '''
          :param args: 客户端传递的字典参数,包含用户名,指令,文件名
          1.获取文件名,判断文件名是否存在,如果本地不存在则发送error505消息
          2.如果存在,这获取文件大小.并且发送给客户端,同时等待客户端确认消息
          3.读取文件,循环发送
          '''
        self.get_dict = args[0]  # 获取客户端get方法传递过来的msg_dic字典
        self.get_filename = self.get_dict['filename']  # 获取文件名
        #self.get_user = self.get_dict['username']  # 获取用户名
        if os.path.isfile(self.current_dir+self.get_filename): #判断文件是否存在
            self.get_size = os.path.getsize(self.current_dir+self.get_filename) #获取文件大小
            self.request.send(str(self.get_size).encode("utf-8")) #发送文件大小给客户端
            self.request.recv(1024) #接收客户端确认消息
            f=open(self.home+self.get_filename,'rb') #打开文件
            for line in f:# 循环发送文件
                self.request.send(line)
            f.close()

        else: # 如果不存在,发送错误消息
            self.request.send("error505".encode("utf-8"))

    def ls(self,*args):
        '''
          :param args: 客户端传递的字典参数,包含用户名,指令,路径
          1.获取客户端传递过来的目录,如果没有目录,则显示当前目录下文件,如果有指定目录,且目录不存在则发送error303消息
          2.如果目录正确,则显示命令结果.发送命令结果的长度给服务端,客户端循环接收
          '''
        self.ls_dict = args[0]  # 获取客户端ls方法传递过来的msg_dic字典
        self.ls_path = self.ls_dict['path']  # 获取路径
        #self.ls_user = self.ls_dict['username']  # 获取用户名
        if self.ls_path == False: #如果客户端ls命令没有携带路径,则显示当前路径下的文件
            path=self.current_dir
        else: #如果携带了路径,则获取该用户的绝对目录
            path=self.current_dir+self.ls_path

        if os.path.isdir(path):#判断该目录是否存在
            ls_file=os.listdir(path) #获取该目录下的所有的文件的一个列表
            ls_str = ','.join(ls_file)  # 将文件列表转换成字符串,发送给客户端 ---(列表数据不能直接send,也不能encode)
            self.request.send(str(len(ls_str)).encode("utf-8")) #发送该列表长度给客户端(一般来说列表不会超过1024字节,一次可以发完)
            self.request.recv(1024) #等待客户端确认
            self.request.send(ls_str.encode("utf-8")) #发送ls命令直接结果给客户端

        else: #如果目录不存在,则发送error303
            self.request.send("error303".encode("utf-8"))

    def mkdir(self,*args):
        '''
          :param args: 客户端传递的字典参数,包含指令,目录名
          1.获取客户端传递过来的目录,如果目录非法,则发送错误消息给客户端
          2.如果目录正确,则创建.发送ok200给客户端
          '''
        self.mkdir_dict = args[0]  # 获取客户端mkdir方法传递过来的msg_dic字典
        self.mkdir_dir = self.mkdir_dict['directory']  # 获取目录名
        try:#创建目录
            os.makedirs(self.current_dir+self.mkdir_dir)
        except (OSError,FileNotFoundError) as e: #如果目录名非法
            self.request.send(str(e).encode("utf-8")) #发送错误消息
        else:
            self.request.send("ok200".encode("utf-8")) #如果成功创建,则发送ok200

    def cd(self,*args):
        '''
         :param args: 客户端传递的字典参数,包含指令,目录名
         1.获取客户端传递过来的目录,判断是cd .. 还是 cd path
         2.如果是目录,且目录非法,则发送错误消息给客户端,如果目录正确,发送ok200给客户端,更新该用户的self.current_dir当前目录
         2.如果是cd ..,则比较用户的当前目录是否为家目录,如果是,发送错误消息,否则发送ok200给客户端,更新该用户的self.current_dir当前目录
         '''
        self.cd_dict = args[0]  # 获取客户端cd方法传递过来的msg_dic字典
        self.cd_path = self.cd_dict['path']  # 获取路径名
        if self.cd_path == "..": #如果是 cd ..
            if self.current_dir == self.home: #如果当前是在家目录下,返回一个202错误
                self.request.send("error202".encode("utf-8"))
            else:
                self.request.send("ok202".encode("utf-8")) #返回正常消息
                # 更新用户的当前工作目录,在目录结尾加上分隔符(如果没有分隔符,则路径+目录会出错)..因为current_dir结尾有分隔符,所以要用两次dirname
                self.current_dir=os.path.dirname(os.path.dirname(self.current_dir))+'\\'
                print (os.path.dirname(self.current_dir))
        else: #如果是 cd path
            try:  # 尝试移动目录
                os.chdir(self.current_dir + self.cd_path)
            except (OSError, FileNotFoundError) as e:  # 如果目录名非法
                self.request.send(str(e).encode("utf-8"))  # 发送错误消息
            else:
                self.request.send("ok202".encode("utf-8"))  # 如果成功创建,则发送ok202
                if self.cd_path.endswith("\\"):
                    self.current_dir=self.current_dir+self.cd_path #更新当前目录
                else:
                    self.current_dir=self.current_dir+self.cd_path+"\\"

    def pwd(self,*args):
        # 获取该用户的当前工作目录,返回给客户端
        self.request.send(self.current_dir.encode("utf-8"))



    def handle(self):
        self.authentication() #服务器验证用户登录账号
        while True:
            try:
                self.data = self.request.recv(1024).strip() #这是接收服务器传过来的Json数据,包括用户名,指令,(可能还有文件名)
                print("connect to client",self.client_address[0])
                self.data_dict = json.loads(self.data.decode()) #获取客户端发送的字典文件
                self.action = self.data_dict['action'] #获取字典里的action
                if hasattr(self,self.action): #判断是否存在该命令方法
                    self.cmd=getattr(self,self.action)
                    self.cmd(self.data_dict) #调用该命令,传递字典参数
                else:
                    print ("错误,找不到该命令")

            except ConnectionRefusedError as e:
                print ("error",e)
                break

if __name__ == "__main__":
    host,port = 'localhost',7001
    server = socketserver.ThreadingTCPServer((host,port),Mysocket)

    server.serve_forever()




