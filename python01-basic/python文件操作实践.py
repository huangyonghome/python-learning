# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 22:23
# @Author  : jesse
# @File    : python文件操作实践.py

'''
批量替换文件内容

迭代目录,替换文件中的内容..下面这个代码有问题,涉及到doc文件的格式编码,还不能这样简单的进行操作.但是循环遍历目录下的所有文件是没问题的
'''


import os,sys

path = r"D:\等保测评管理制度"
#
old_str = "上海证大喜马拉雅网络科技有限公司"
new_str = "上海多维度网络科技股份有限公司"

def modify_file(file_path,old_str,new_str):

    #只读方式打开word文件,.同时以写的方式打开另外一个bak备份word文件
    with open(file_path,"r",encoding="ISO-8859-1") as f1,open("%s.bak" %file_path, "w",encoding="GB2312") as f2:

        for line in f1: #按行读取word文件

            if old_str in line: #如果存在要替换的内容
                line = line.replace(old_str,new_str) #将内容替换成新的字符串
            f2.write(line) #将原文件写入到一个新的备份文件

    os.remove(file_path) #删除原文件
    os.rename("%s.bak" %file_path,file_path) #将备份文件重命名为原文件



#循环目录下的文件以及子目录下的所有文件

for i in os.listdir(path):

    #如果是文件,则直接用modify_file函数来执行替换动作..将文件的绝对路径传递进去
    if os.path.isfile(os.path.join(path,i)):
        file_path = os.path.join(path,i)
        modify_file(file_path,old_str,new_str)

    else:
        #如果是目录,则循环目录下的所有子目录和文件
       for root,dirs,files in os.walk(os.path.join(path,i)): #获取子目录下的所有文件和父目录名

           for single_file in files:

                file_path = os.path.join(root,single_file) #将子目录和目录下的文件名路径拼接
                modify_file(file_path,old_str,new_str)




