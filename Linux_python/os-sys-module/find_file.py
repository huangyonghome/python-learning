#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 下午12:00
# @Author  : jesse
# @File    : find_file.py

import os
import fnmatch

def is_file_match(filename,patterns):
    for pattern in patterns:
        if fnmatch.fnmatch(filename,pattern):
            return True

    return False


def find_specific_files(root,patterns=['*'],exclude_dirs=[]):
    for root,dirnames,filenames in os.walk(root):
        for filename in filenames:
            if is_file_match(filename,patterns):
                yield os.path.join(root,filename)

        for d in exclude_dirs:
            if d in dirnames:
                dirnames.remove(d)


# 查找tmp目录下的所有文件,不包括com.google.Keystone子目录
# for item in find_specific_files('/tmp',exclude_dirs=["com.google.Keystone"]):
#     print(item)


# 查找tmp目录下所有文件,并且找到最大的10个文件
files = {name: os.path.getsize(name) for name in find_specific_files('/tmp')}
print(files)


result = sorted(files.items(), key=lambda d: d[1], reverse=True)[:10]
print(result)
for i, t in enumerate(result, 1):
    print(i, t[0], t[1])

