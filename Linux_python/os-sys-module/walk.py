#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/3 上午11:29
# @Author  : jesse
# @File    : walk.py

import os

for root,dirnames,filenames in os.walk(os.path.expanduser("~/Desktop")):
    print(root)
    print(dirnames)
    print(filenames)


# print(os.walk(os.path.expanduser("~/Desktop")))