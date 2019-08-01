#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/31 上午9:47
# @Author  : jesse
# @File    : describinstance.py

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

client = AcsClient('LTAIdL4dFHXnznpn', 'QdlXmv881cbUs2pWlJZkbWE78vFZvF', 'cn-hangzhou')

request = DescribeInstancesRequest()
request.set_accept_format('json')
request.set_PrivateIpAddresses(["10.111.30.188", "10.111.5.73"])
request.set_EipAddresses(["47.96.185.233"])
response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))