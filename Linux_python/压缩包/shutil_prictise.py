#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 下午4:51
# @Author  : jesse
# @File    : shutil_prictise.py

import shutil
## 创建压缩包,默认情况下是压缩当前目录下所有的文件和子目录

# get_archive_formats可以查看shutil支持的压缩格式
print(shutil.get_archive_formats())


# make_archive方法有2个必选参数,分别是base_name和format.
# base_name表示压缩包名,这里是backup. format表示压缩成什么格式,这里是gz格式.
# make_archive会自动将base_name的后面加上gz后缀.
# shutil.make_archive('backup','gztar')

# 压缩成zip格式

# shutil.make_archive('backup','zip')

# 用tarfile模块查看压缩包内的文件

# import tarfile
#
# with tarfile.open('backup.tar.gz','r:gz') as f:
#     print(f.getnames())

## shutil模块的unpack_archive方法也可以解压

### 将backup.tar.gz解压缩到test1目录下.即使test1目录不存在也会自动创建.

# shutil.unpack_archive('backup.tar.gz',extract_dir='test1',format='gztar')


### shutil还可以指定压缩哪个目录下的文件

# shutil.make_archive('tmp',root_dir='/tmp',format='gztar')

## 用tarfile查看tmp.tar.gz下的文件

import tarfile

with tarfile.open('tmp.tar.gz',mode="r:gz") as f:
    print(f.getnames())