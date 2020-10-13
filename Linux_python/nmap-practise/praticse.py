#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/7 上午10:22
# @Author  : jesse
# @File    : praticse.py

# 使用python-nmap模块使用linux的nmap命令


import nmap

# 创建一个nmap的扫描器对象
nm = nmap.PortScanner()

# 指定扫描某个iP下的哪些端口
nm.scan('172.16.10.151','22-9000',arguments='')

#扫描命令
print(nm.command_line())

#扫描信息
print(nm.scaninfo())

# 扫描的远程服务器
print(nm.all_hosts())

# 查看服务器状态
print(nm['172.16.10.151'].state())

# 查看扫描的端口协议
print(nm['172.16.10.151'].all_protocols())

# 查看远程服务器开放的端口
print(nm['172.16.10.151']['tcp'].keys())

# 查看具体端口的信息
print(nm['172.16.10.151']['tcp'][80])