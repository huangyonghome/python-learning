#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 上午9:19
# @Author  : jesse
# @File    : set_password.py

from passlib.hash import sha512_crypt
import getpass
print(sha512_crypt.using(rounds=5000).hash(getpass.getpass()))
