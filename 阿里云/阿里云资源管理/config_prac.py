#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 下午5:59
# @Author  : jesse
# @File    : config_prac.py

import configparser


conf = configparser.ConfigParser()

conf.read("aliyun.ini")

sec = conf.sections()

print(sec)