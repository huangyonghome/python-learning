#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/29 下午4:30
# @Author  : jesse
# @File    : read_stdin.py

# import sys
#
# for line in sys.stdin:
#     print(line, end="")

import fileinput

for line in fileinput.input():
    meta = [fileinput.filename(),fileinput.isstdin(),fileinput.isfirstline()]
    print(meta,end="\n")
    print(line,end="")