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

print(type(access_key),access_key)
print(type(key_secret),key_secret)
print(client.__dict__)

request = DescribeInstancesRequest.DescribeInstancesRequest()
request.set_PageSize(10)


#获取到ECS的信息
response = client.do_action_with_exception(request).decode("utf-8")

#转成字典格式
response = json.loads(response)

#ECS详细信息
ECS_detail = response["Instances"]["Instance"][0]


#镜像ID:
ImageId = ECS_detail["ImageId"]


#CPU和内存信息
cpu = ECS_detail["Cpu"]
mem = ECS_detail["Memory"]


#主机相关信息
host = ECS_detail["HostName"]
type = ECS_detail["InstanceType"] #实例规格族
instanceId =  ECS_detail["InstanceId"]  #实例ID
instance_name = ECS_detail["InstanceName"]  #实例名
ip_pri = ECS_detail["VpcAttributes"]["PrivateIpAddress"]["IpAddress"][0]  #内网IP地址
ip_pub = ECS_detail["PublicIpAddress"]["IpAddress"][0] #外网IP地址


print("主机名:{},私有IP地址:{},公网IP地址:{},规格族:{}".format(host,ip_pri,ip_pub,type))