#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午4:57
# @Author  : jesse
# @File    : request_zoneID.py


from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest

import configparser
import uuid

aliyun_conf = configparser.ConfigParser()
aliyun_conf.read("aliyun.ini")

access_key = aliyun_conf.get("access","access_key")
key_secret =  aliyun_conf.get("access","key_secret")
region_id =  aliyun_conf.get("access","region_id")

# 创建 AcsClient 实例
client = AcsClient(
    access_key,
    key_secret,
    region_id
)


request = DescribeAvailableResourceRequest()
request.set_accept_format('json')

request.set_DestinationResource("Zone")

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))