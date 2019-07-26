#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/23 下午2:40
# @Author  : jesse
# @File    : build_request.py

from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from conf import read_conf
import json

def build_request():
    '''
    构建创建ECS的request参数.
    :return:
    '''

    #实例化一个RunInstancesRequest的requst对象
    request = RunInstancesRequest()
    request.set_accept_format('json')

    #接收配置文件读取后返回来的字典数据
    dict_conf = read_conf()

    #由于配置文件读取出来的key全是小写字母.不能直接用request.set_xxx的方式调用.所以需要做一些处理
    #1.调出request的所有属性
    namespace = dir(request)
    #.将set开头的属性做一个字典映射.key是小写字母,对应的值是reqeust的原始方法.比如将set_HostName做个绑定关系.set_hostname:set_HostName
    params = { k.lower():k for k in namespace if k.startswith('set')}


    for key,value in dict_conf.items(): #循环配置文件中的键值对

        key = 'set_' + key #拼接key
        value = json.loads(value)

        if key in params: #如果配置文件中的键和params匹配,则调用params对应的方法.比如imageid这个键对应的方法就是request.set_ImageId()这个方法
                print(getattr(request,params[key]))



build_request()