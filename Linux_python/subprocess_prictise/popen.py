#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 下午7:38
# @Author  : jesse
# @File    : popen.py

import subprocess

def execute_cmd(cmd):
    p = subprocess.Popen(cmd,
                         shell=True,
                         stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE,
                         stderr=subprocess.PIPE)


    stdout, stderr = p.communicate()
    if p.returncode != 0:
        return p.returncode, stderr

    return p.returncode,stdout


# result = execute_cmd("df -h")[1].decode('utf-8')


# result2 = execute_cmd("ps aux | grep php-fpm | grep -v grep")
result2 = execute_cmd("jhahah")

print(result2)