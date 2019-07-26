#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午2:17
# @Author  : jesse
# @File    : practise1.py

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/16 下午4:03
# @Author  : jesse
# @File    : practice.py

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
from aliyunsdkecs.request.v20140526 import StopInstanceRequest
import json


client = AcsClient(
   "LTAIFl3FW7np6VQ3",
   "PQHQp0Hcx99YCEmgp1WLLv8a0VTZJ5",
   "cn-hangzhou"
)

request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)


#获取到ECS的信息
response = client.do_action_with_exception(request)

#转成字典格式
response = json.loads(response)

print(response.get('Instances').get('Instance'))



# #ECS详细信息
# ECS_detail = response["Instances"]["Instance"][0]
#
#
# #镜像ID:
# ImageId = ECS_detail["ImageId"]
#
# print(ImageId)
#
# #CPU和内存信息
# cpu = ECS_detail["Cpu"]
# mem = ECS_detail["Memory"]
#
#
# #主机相关信息
# host = ECS_detail["HostName"]
# type = ECS_detail["InstanceType"] #实例规格族
# instanceId =  ECS_detail["InstanceId"]  #实例ID
# instance_name = ECS_detail["InstanceName"]  #实例名
# ip_pri = ECS_detail["VpcAttributes"]["PrivateIpAddress"]["IpAddress"][0]  #内网IP地址
# ip_pub = ECS_detail["PublicIpAddress"]["IpAddress"][0] #外网IP地址
#
#
# print("主机名:{},私有IP地址:{},公网IP地址:{},规格族:{}".format(host,ip_pri,ip_pub,type))