#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午3:15
# @Author  : jesse
# @File    : check_resources.py

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest

from conf import config
import json

access_key = config.access_key
key_secret = config.key_secret
region_id = config.region_id


client = AcsClient(access_key,key_secret, region_id)

request = DescribeAvailableResourceRequest()
request.set_accept_format('json')

#request.set_InstanceType("ecs.n4.2xlarge")
request.set_Memory("16")
request.set_Cores(8)
request.set_IoOptimized("optimized")
request.set_ZoneId("cn-hangzhou-b")
request.set_InstanceChargeType("PostPaid")
request.set_DestinationResource("InstanceType")

response = client.do_action_with_exception(request).decode("utf-8")

response = json.loads(response)

res_dict = response["AvailableZones"]["AvailableZone"][0]["AvailableResources"]["AvailableResource"][0]["SupportedResources"]["SupportedResource"]
# print(res_dict)
for i in res_dict:
    # print(i)
    # print(i['Value'],i['StatusCategory'])
    if i['Value'] == config.set_InstanceType:

        print(i['StatusCategory'])
