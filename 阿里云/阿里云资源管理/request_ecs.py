# -*- coding: utf-8 -*-
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526 import DescribeInstancesRequest
import json
import configparser
import uuid

aliyun_conf = configparser.ConfigParser()
aliyun_conf.read("conf/aliyun.ini")

access_key = aliyun_conf.get("access","access_key")
key_secret =  aliyun_conf.get("access","key_secret")
region_id =  aliyun_conf.get("access","region_id")

client = AcsClient(
    access_key,
    key_secret,
    region_id
)



request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(100)
request.set_Tags([
  {
    "value": "hsq",
    "key": "hsq"
  }
])

response = client.do_action_with_exception(request).decode("utf-8")

response = json.loads(response)
print(response)
response_detail = (response.get("Instances").get("Instance"))
instance_list = []

for instance in response_detail:

    instance_list.append(instance.get('InstanceName'))

print(instance_list)


# print(request.__dict__)
#
# l1 = response.get('Instances').get('Instance')
#
# for i in l1:
#     print(i.get("InstanceName"))

# ECS_detail = response["Instances"]["Instance"][0]
#
#
# ImageId = ECS_detail["ImageId"]
#
#
# cpu = ECS_detail["Cpu"]
# mem = ECS_detail["Memory"]
#
#
# host = ECS_detail["HostName"]
# type = ECS_detail["InstanceType"] #实例规格族
# instanceId =  ECS_detail["InstanceId"]  #实例ID
# instance_name = ECS_detail["InstanceName"]  #实例名
# ip_pri = ECS_detail["VpcAttributes"]["PrivateIpAddress"]["IpAddress"][0]  #内网IP地址
# ip_pub = ECS_detail["PublicIpAddress"]["IpAddress"][0] #外网IP地址
#
#
# print("主机名:{},私有IP地址:{},公网IP地址:{},规格族:{}".format(host,ip_pri,ip_pub,type))
