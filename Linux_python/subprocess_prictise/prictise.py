#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/5 下午5:19
# @Author  : jesse
# @File    : prictise.py

import subprocess

## call方法,将命令和参数作为一个列表传入.执行shell命令.
# 返回值是命令退出状态码.和Linux一样,0为正常.

# subprocess.call(['ls','-al'])

result = subprocess.call("ping -c 1 -W 1 172.16.10.254",shell=True)

print(result)
# if subprocess.call("ping -c 1 172.16.10.8",shell=True):
#     print("avaliable")
# else:
#     print("unavaliable")

## 也支持字符串命令,设置Shell为True,这样python先启动一个Shell环境,.然后再执行命令
# 这有点类似于docker的entrypoint和cmd区别

# result = subprocess.call("ls -al",shell=True)
#
# print("返回值: %s" % result)


# check_call函数和call函数类似,不同的是,check_call函数返回值不是0的时候会直接抛出异常

# subprocess.check_call("exit 1", shell=True)