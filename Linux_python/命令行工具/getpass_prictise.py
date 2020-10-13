#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 下午5:36
# @Author  : jesse
# @File    : getpass_prictise.py

import getpass

user = getpass.getuser()
passwd = getpass.getpass("your password: ")
print(user,passwd)