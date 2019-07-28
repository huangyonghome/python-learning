#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午2:44
# @Author  : jesse
# @File    : set_request.py


import json
import uuid
import sys
from common.log import logger as log
from conf import config as default_config
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest


class AliClient:
    def __init__(self, access_key=None, key_secret=None, region_id=None, config=None):
        self.config = config
        if not self.config:
            self.config = default_config
        self.access_key = access_key or self.get_config('access_key')
        self.key_secret = key_secret or self.get_config('key_secret')
        self.region_id = region_id or self.get_config('region_id')
        self.client = AcsClient(self.access_key, self.key_secret, self.region_id)

    def get_config(self, field):
        if hasattr(self.config, field):
            return getattr(self.config, field)
        raise AttributeError

    @property
    def request(self):
        return RunInstancesRequest()

    @property
    def describe_request(self):
        return DescribeAvailableResourceRequest()

    def create_request_object(self):
        req = RunInstancesRequest()
        req.set_ClientToken(str(uuid.uuid4()))
        request_methods = {k.lower(): v for k, v in RunInstancesRequest.__dict__.items()}
        params = filter(dir(self.config), lambda x: x.lower().startswith('set'))
        for param in params:
            if param.lower() in request_methods.keys():
                getattr(req, request_methods[param].__name__)(self.config, param)
        return req

    def check_resource(self):
        """
        实例化DescribeAvailableResource接口的request..检查某个可用区下某个ECS规格的库存.如果没有库存,则不让创建.
        检查创建的ECS实例在当前可用区是否有足够多的资源
        ps: 后续可能会进一步开发.比如8核16的独享型实例规格没有库存,创建失败的话,自动创建8核16G的共享型实例规格
        """
        req = self.describe_request
        req.set_accept_format('json')
        req.set_InstanceType(self.get_config('set_InstanceType'))  # ECS实例规格族.必选参数
        req.set_IoOptimized("optimized")  # IO优化实例.对于新的ECS来说都是IO优化实例
        req.set_ZoneId(self.get_config('set_ZoneId'))  # 可用区ID.必选参数
        req.set_DestinationResource(self.get_config('InstanceType'))  # 检查的资源对象是实例类型.当然也还可以检查云盘资源等
        req.set_InstanceChargeType(self.get_config('set_InstanceChargeType') or "PostPaid")
        return req  # 返回request对象

    def check_describe_status(self, object, page_size, page_num):
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

    def send_request(self, request):
        '''
        向阿里云API提交request的统一处理方法.
        :param client: client实例
        :param request: request对象
        :param log: log日志实例对象
        :return: 返回响应的json数据
        '''
        request.set_accept_format('json')
        try:
            response = self.client.do_action_with_exception(request).decode("utf-8")
            log.debug(response)
            response_detail = json.loads(response)
            return response_detail
        except Exception as e:
            log.error(e)
            sys.exit(1)
