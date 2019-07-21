#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 下午5:32
# @Author  : jesse
# @File    : create_single_ECS.py


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import CreateInstanceRequest
import json
import configparser

aliyun_conf = configparser.ConfigParser()
aliyun_conf.read("aliyun.ini")

access_key = aliyun_conf.get("access","access_key")
key_secret =  aliyun_conf.get("access","key_secret")
region_id =  aliyun_conf.get("access","region_id")

# 创建 AcsClient 实例
client = AcsClient(
    access_key.,
   key_secret,
   region_id
)
# 创建 request，并设置参数
request = CreateInstanceRequest.CreateInstanceRequest()
request.set_ImageId("alinux_17_01_64_20G_cloudinit_20171222.vhd")
request.set_InstanceName("MyInstance")
request.set_SecurityGroupId("<your-security-group-id>")
request.set_InstanceType("ecs.t1.small")
request.set_ClientToken("<uuid>")
# 发起 API 请求并打印返回
response = client.do_action_with_exception(request)
print response