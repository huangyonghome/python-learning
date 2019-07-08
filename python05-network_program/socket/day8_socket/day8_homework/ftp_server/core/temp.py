# -*- coding: utf-8 -*-
# @Time    : 2017-05-20 12:19
# @Author  : jesse
# @File    : temp.py

import os,os.path
import sys

sys.path.append('..')
from conf import account

import sys
import time


home='D:\\home\\jesse'
file='test.pdf'

if os.path.isfile(home+file):
    print("yes")
else:
    print("no")
