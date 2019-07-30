#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午2:44
# @Author  : jesse
# @File    : set_request.py

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

from conf import config
import json
import uuid


def Set_Client():
    '''
    实例化一个client对象.
    :return: client对象
    '''
    '''
    获取阿里云账户的Token以及阿里云地域
    '''
    access_key = config.access_key
    key_secret = config.key_secret
    region_id = config.region_id

    # 实例化一个Client对象
    client = AcsClient(access_key, key_secret, region_id)

    return client #返回client对象


def Set_RunInstanse_Request():

    '''
    1.实例化RunInstances的request对象.
    2.获取配置文件中的key.也就是参数.配置文件的参数格式为:set_xxx .这个格式和request的方法匹配.
比如配置文件中的set_HostName配置,对应request.set_HostName方法
    3.遍历key,如果request里含有此方法就调用.这是为了防止配置文件中出现的不支持的参数导致程序执行错误
    :return: 返回request对象到主程序
    '''

    #实例化request对象
    request = RunInstancesRequest()
    request.set_ClientToken(str(uuid.uuid4())) #传递随机的字符串,保障程序的幂等性

    #生成set_xxx方法的列表
    params = [ x for x in dir(request) if x.startswith("set")]

    #遍历配置文件中的配置参数
    keys = [ x for x in dir(config) if x.startswith("set")]

    for key in keys: #遍历配置文件中的配置参数

        if key in params: #如果request对象支持此方法,则使用反射方法调用

            getattr(request,key)(config.__dict__[key])

    return request



def Set_Resource_Request():
    '''
    实例化DescribeAvailableResource接口的request..检查某个可用区下某个ECS规格的库存.如果没有库存,则不让创建.
    检查创建的ECS实例在当前可用区是否有足够多的资源
    :return: request对象

    ps: 后续可能会进一步开发.比如8核16的独享型实例规格没有库存,创建失败的话,自动创建8核16G的共享型实例规格
    '''
    #实例化request对象
    request = DescribeAvailableResourceRequest()
    request.set_accept_format('json')


    request.set_InstanceType(config.set_InstanceType) #ECS实例规格族.必选参数
    request.set_IoOptimized("optimized") #IO优化实例.对于新的ECS来说都是IO优化实例
    request.set_ZoneId(config.set_ZoneId) #可用区ID.必选参数
    request.set_DestinationResource("InstanceType") #检查的资源对象是实例类型.当然也还可以检查云盘资源等

    if hasattr(config,"set_InstanceChargeType"): #判断申请ECS的计费方式,默认是按量计费,如果有自定义配置成包年包月,则计费类型改成包年包月
        request.set_InstanceChargeType(config.set_InstanceChargeType)
    else:
        request.set_InstanceChargeType("PostPaid")

    return request #返回request对象


def  Set_Describe_Request(object,page_size,page_num):
    '''
    检查ECS实例是否为running状态
    实例化一个reqeust对象
    :param: object:传递过来要检查的对象.这个对象可能是个实例列表
    :return: 返回request对象
    '''
    request = DescribeInstancesRequest()
    request.set_InstanceIds(json.dumps(object))
    request.set_PageSize(page_size)
    request.set_PageNumber(page_num)

    return request