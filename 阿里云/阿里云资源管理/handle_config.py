#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 上午10:09
# @Author  : jesse
# @File    : handle_config.py

from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from conf import config

# print(dir(config))
request = RunInstancesRequest()
request.set_accept_format('json')


keys = [ x for x in dir(config) if x.startswith("set")]

for key in keys:
    value = config.__dict__[key]

    print(value,type(value))
    # print(getattr(request,key))