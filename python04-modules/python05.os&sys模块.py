# -*- coding: utf-8 -*-
# @Time    : 2019-06-12 20:31
# @Author  : jesse
# @File    : python05.os&sys模块.py

import sys,os

#sys.path   #打印path环境变量
#sys.exit()  #程序退出

#sys.argv 实现从程序外部向程序传递参数.结果是一个列表..第一个为python文件名.第二个为python脚本的参数1.......


## os模块

###############################################################################
#和路径相关

print(__file__) #返回本文件的绝对路径

'''
os.path.abspath(path) 返回绝对路径
'''

print(os.path.abspath("."))

'''
os.path.basename(path) #返回目录名
'''
print(os.path.basename("D:\python-learning\python-modules"))

'''
os.path.dirname(path) #返回目录路径
'''
print(os.path.dirname("D:\python-learning\python-modules"))

'''
os.path.exists(path) 如果路径存在,返回True,否则返回False
'''
print(os.path.exists("D:\python-learning\python-modules"))

'''
os.path.getatime(path) 返回最近访问时间(浮点型秒数)
os.path.getmtime(path) 返回最近文件修改时间
os.path.getctime(path) 返回文件创建时间
'''
print(os.path.getatime("D:\python-learning\python-modules"))

'''os.path.getsize(path) 返回文件大小. 单位是byte字节
'''
print(os.path.getsize(r"D:\blogs.zip"))

## 路径检测

print(os.path.isabs(".")) #判断是否为绝对路径
print(os.path.isfile("D:\python-learning\python-modules")) #判断是否为文件
print(os.path.isdir(r"D:\blogs.zip")) #判断是否为目录


#路径处理
print(os.path.join("D:/python-learning","python01-basic")) #将这2个路径合并成一个.
print(os.path.split("D:\python-learning\python-modules")) #把路径和目录名拆分成2个元素,返回一个元祖
print(os.path.normpath("D:\python-learning\python-modules"))


dir = os.path.join("D:/python-learning","python01-basic")
dir1 = os.path.join(dir,"haha")
os.mkdir(dir1)










###############################################################################

#目录相关

'''
os.getcwd() #获取当前脚本目录
'''

#print(os.getcwd())

'''
os.chdir("dirname") 改变脚本工作目录.相当于cd命令
'''

#
# os.chdir("d:\python-learning")
# print(os.getcwd())   #路径已经发生了改变

'''
os.curdir  #返回当前目录
'''

# os.curdir

'''
os.pardir 获取当前目录的父目录字符串名
'''

# print(os.pardir)

'''
os.makedirs  #创建目录,可以创建多层目录 相当于 mkdir -p /dir1/dir2
os.removedirs #删除目录 .删除空目录.如目录下有文件,则不删除目录
'''
# os.makedirs("d:/test/test1/")
# os.removedirs("d:/test/test1/")

'''
os.mkdir #和上面方法一样.只是创建单级目录
os.rmdir
'''

'''
os.listdir  #列出指定目录下的所有文件和子目录,以列表形式返回
'''

# print(os.listdir("D:/"))

###############################################################################


#文件相关

'''
os.remove 删除一个文件
os.rename("oldname","newname") #重命名文件/目录
os.stat("path/filename")   #获取文件信息
'''

# os.remove("D:\sd.txt")  #删除
#print(os.stat(r"D:\test.txt")) #查看这个文件的信息.

###############################################################################

#操作系统差异相关

'''
os.sep  #路径分割符.windows是\\ linux是 /
os.linesep #换行符  windows是\r\n linux是 \n
os.name #当前平台. windows为nt linux是posix

'''


#os.getenv() 读取环境变量



# print(os.getenv())


# print(os.sep)