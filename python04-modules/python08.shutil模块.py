# -*- coding: utf-8 -*-
# @Time    : 2019-06-16 15:25
# @Author  : jesse
# @File    : python08.shutil模块.py

import shutil

#高级的 文件、文件夹、压缩包 处理模块


#
# #将文件内容拷贝到另外一个文件中
#
# shutil.copyfileobj(open('sys.log','r'),open('new.log','w'))
#
# #文件拷贝,如果目的文件不存在,则新建一个
# shutil.copyfile('sys.log','sys_copy.log')
#
# #仅拷贝权限..内容,组,用户均不变.目标文件必须实现存在
# shutil.copymode('sys.log','sys_copy.log')
#
# #仅拷贝状态的信息.目标文件必须实现存在
# shutil.copystat('sys.log','sys_copy.log')
#
# #拷贝文件和权限
#
# shutil.copy('sys.log','sys_copy.log')
#
#
# #递归拷贝目录.注意对目录父级目录要有可写权限，ignore的意思是排除.并且目标目录不能存在
#
# shutil.copytree('module2','module2_copy',
#                 ignore=shutil.ignore_patterns("__init__.py"))
#
#
# #拷贝软连接
#
# shutil.copytree('module2','module2_copy',symlinks=True,
#                 ignore=shutil.ignore_patterns("__init__.py"))
#
# #递归删除目录
#
# shutil.rmtree('module2_copy')


#创建压缩包

'''
创建压缩包并返回文件路径，例如：zip、tar

base_name： 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径，
如 data_bak                       =>保存至当前路径
如：/tmp/data_bak =>保存至/tmp/
format：	压缩包种类，“zip”, “tar”, “bztar”，“gztar”
root_dir：	要压缩的文件夹路径（默认当前目录）
owner：	用户，默认当前用户
group：	组，默认当前组
logger：	用于记录日志，通常是logging.Logger对象

'''

#打包module2目录为module2.tar.gz.放到当前文件

# ret = shutil.make_archive(base_name="module2",
#                           format="gztar",
#                           root_dir='module2')
#
# print(ret)
#
# import zipfile
#
# z = zipfile.ZipFile('module2.zip','w')
# z.write('module2')
# z.close()


#解压shutil压缩包

shutil.unpack_archive('module2.tar.gz',extract_dir='log',format='gztar')


import zipfile,os,tarfile

#压缩单个文件

# with zipfile.ZipFile('log.zip','r') as z:
#     # z.write('sys.log')
#     # z.write('test.log')
#     # z.write('advance.log')
#     print(z.namelist())

#解压单个文件
#
# with zipfile.ZipFile('log.zip','r') as z:
#     print(z.namelist())
#     print(z.read(z.namelist()[0]))
#     z.extractall(path='log')




# 追加单个文件

# with zipfile.ZipFile('log.zip','a') as z:
#     z.write('user.db')
#     #查看文件
#     print(z.namelist())





# for root,dirs,files in os.walk('module2'):
#     print(root)
#     print(dirs)
#     print(files)



#压缩某个目录下所有文件
# def addfile(zipfilename, dirname):
#     if os.path.isfile(dirname):
#         with zipfile.ZipFile(zipfilename, 'w') as z:
#             z.write(dirname)
#     else:
#         with zipfile.ZipFile(zipfilename, 'w') as z:
#             for root, dirs, files in os.walk(dirname):
#                 for single_file in files:
#                     if single_file != zipfilename:
#                         filepath = os.path.join(root, single_file)
#                         z.write(filepath)
#
#
#
# addfile('module2-1.zip', 'module2')

#查看压缩包内的文件
# with zipfile.ZipFile('module2-1.zip') as z:
#     print(z.namelist())

#
# #添加现有文件到zip包中
#
# with zipfile.ZipFile('module2-1.zip','a') as z:
#     z.write('user.db')


#tarfile模块

#
# with tarfile.open('module2.tar','w') as tar:
#     tar.add('sys.log')
#     tar.add('test.log')


#压缩目录下的所有文件
#
# def compress_file(tarfilename, dirname):    # tarfilename是压缩包名字，dirname是要打包的目录
#     if os.path.isfile(dirname):
#         with tarfile.open(tarfilename, 'w') as tar:
#             tar.add(dirname)
#     else:
#         with tarfile.open(tarfilename, 'w') as tar:
#             for root, dirs, files in os.walk(dirname):
#                 for single_file in files:
#                     # if single_file != tarfilename:
#                     filepath = os.path.join(root, single_file)
#                     tar.add(filepath)
#
#
#
# compress_file('module2-3.tar','module2')