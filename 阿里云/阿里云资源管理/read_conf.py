#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 下午2:48
# @Author  : jesse
# @File    : read_conf.py

import configparser
import json
dict_conf = {}

def read_conf():
    '''
    读取conf下的aliyun.ini配置文件.返回所有的键列表
    :return: 键值对列表
    '''
    aliyun_conf = configparser.ConfigParser()
    aliyun_conf.read("conf/aliyun.ini")
    key_list = aliyun_conf.items("hsq")

    for key in key_list:
        print(key)
        print(key[0])
        # if dict_conf[key[0]] == "uniquesuffix":
        #     dict_conf[key[0]] = json.loads(key[1])
        #     print(dict_conf)

    return dict_conf


read_conf()