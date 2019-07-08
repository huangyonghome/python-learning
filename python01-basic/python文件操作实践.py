# -*- coding: utf-8 -*-
# @Time    : 2019-07-08 22:23
# @Author  : jesse
# @File    : python文件操作实践.py

'''
批量替换文件内容

迭代目录,替换文件中的内容
'''
import docx


import os,sys

path = r"D:\等保测评管理制度"

old_str = "上海证大喜马拉雅网络科技有限公司"
new_str = "上海多维度网络科技股份有限公司"

def modify_file(file_path,old_str,new_str):
    with open(file_path,"r",encoding="ISO-8859-1") as f1,open("%s.bak" %file_path, "w",encoding="GB2312") as f2:
        for line in f1:
            if old_str in line:
                line = line.replace(old_str,new_str)
            f2.write(line)
    os.remove(file_path)
    os.rename("%s.bak" %file_path,file_path)



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
