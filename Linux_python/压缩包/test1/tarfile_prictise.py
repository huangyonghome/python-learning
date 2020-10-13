#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 下午12:58
# @Author  : jesse
# @File    : tarfile_prictise.py

# 打包文件

import tarfile

# with tarfile.open('test.tar',mode='w') as out:
#     out.add('test_tar.py')


# 查看压缩包内的文件
# with tarfile.open('test.tar') as t:
#     # for member_info in t.getmembers():
#     #     print(member_info)
#     print(t.getnames())
#     print(t.getmembers())


# 用gz或者bz压缩打包

# with tarfile.open('pdb.tar.gz',mode='w:gz') as out:
#     out.add('test_tar.py')


# 打开gz压缩包

# with tarfile.open('pdb.tar.gz', mode='r:gz') as t:
#     print(t.getnames())
