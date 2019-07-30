#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午2:44
# @Author  : jesse
# @File    : set_request.py



import json
import uuid
import sys
import os
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerRequest import CreateLoadBalancerRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerHTTPSListenerRequest import CreateLoadBalancerHTTPSListenerRequest
from aliyunsdkslb.request.v20140515.CreateLoadBalancerHTTPListenerRequest import CreateLoadBalancerHTTPListenerRequest
from aliyunsdkslb.request.v20140515.AddTagsRequest import AddTagsRequest

BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)

from .handle_log import log
from conf import config as default_config




class AliClient:
    def __init__(self, access_key=None, key_secret=None, region_id=None, config=None):
        self.config = config
        if not self.config:
            self.config = default_config
        self.access_key = access_key or self.get_config('access_key')
        self.key_secret = key_secret or self.get_config('key_secret')
        self.region_id = region_id or self.get_config('region_id')
        self.client = AcsClient(self.access_key, self.key_secret, self.region_id)


    def get_config(self,field,default=None):
        if hasattr(self.config, field):
            return getattr(self.config, field)
        elif default:
            return default
        else:
            raise AttributeError

    @property
    def run_instance_request(self):
        return RunInstancesRequest()

    @property
    def describe_request(self):
        return DescribeAvailableResourceRequest()

    @property
    def create_slb_request(self):
        return  CreateLoadBalancerRequest()

    @property
    def create_slb_https_request(self):
        return CreateLoadBalancerHTTPSListenerRequest()

    @property
    def create_slb_http_request(self):
        return CreateLoadBalancerHTTPListenerRequest()

    @property
    def add_slb_tag_request(self):
        return AddTagsRequest()




    def initiate_ecs_reques(self):
        req = self.run_instance_request
        req.set_ClientToken(str(uuid.uuid4()))
        # 生成set_xxx方法的列表
        params = [x for x in dir(req) if x.startswith("set")]

        # 遍历配置文件中的配置参数
        keys = [x for x in dir(self.config) if x.startswith("set")]

        for key in keys:  # 遍历配置文件中的配置参数

            if key in params:  # 如果request对象支持此方法,则使用反射方法调用

                getattr(req, key)(self.config.__dict__[key])

        return req


    def initiate_createSLB_request(self,slbdict,LoadBalanceName):
        '''
        初始化CreateSlb接口的request对象.
        :param slbdict: 接收slb的参数字典
        :param LoadBalanceName: 接收slb实例的名字
        :return: 返回request对象
        '''
        req = self.create_slb_request #实例化createSLB的request对象
        req.set_ClientToken(str(uuid.uuid4()))

        #初始化一些通用的request对象
        req.set_LoadBalancerName(LoadBalanceName) #slb实例名
        req.set_MasterZoneId(self.get_config("set_MasterZoneId")) #slb主可用区
        req.set_SlaveZoneId(self.get_config("set_SlaveZoneId"))  # slb备可用区
        req.set_PayType(self.get_config("set_PayType")) #计费方式.

        #初始化一些特殊的request对象参数.
        # 循环接收到的SLB配置参数字典.字典里包含了创建的SLB类型,实例规格等信息
        params = [x for x in dir(req) if x.startswith("set")]
        for key in slbdict.keys():
            if key in params:
                getattr(req, key)(slbdict[key])

        #额外的request初始化参数
        if slbdict.get("set_AddressType") == "internet": #如果是要创建公网SLB
            req.set_InternetChargeType(self.get_config("set_InternetChargeType"))  # 公网类型实例的付费方式

        elif slbdict.get("set_AddressType") == "intranet": #如果是要创建私网SLB,还需要额外定义以下参数

            req.set_VSwitchId(self.get_config("set_VSwitchId")) #虚拟交换机网段
            req.set_VpcId(self.get_config("set_VpcId")) #虚拟VPC ID
        else:
            raise NameError("SLB类型配置错误")

        return req

    def initiate_createSLBlistener_request(self,listener,slbdict,slb_id):
        '''
        初始化SLB的Listener侦听器接口的request对象.
        :param listener: 接收slb的侦听器类型.是https还是http
        :param slbdict: SLB配置参数,有可能会有一些自定义和通用参数有冲突的参数
        :param slb_id: 接收slb实例ID
        :return: 返回request对象
        '''
        if listener == "https": #如果是要创建https侦听器
            req = self.create_slb_https_request #实例化createSLBlistner的request对象
            req.set_ListenerPort(443)  # 前端侦听端口
            req.set_Bandwidth(-1) #监听带宽.由于我们都是按流量计费,所以不限制带宽
            req.set_HealthCheck("off") #关闭健康检查,一般健康检查由http侦听器完成
            req.set_ServerCertificateId(self.get_config("set_ServerCertificateId"))  # 服务器证书ID
            req.set_EnableHttp2(self.get_config("set_EnableHttp2", default="on"))  # 是否开启http2

        elif listener == "http": #如果是要创建Http侦听器
            req = self.create_slb_http_request #实例化createSLBlistner的request对象
            req.set_ListenerPort(self.get_config("set_ListenerPort",default=80))  # 前端侦听端口
            req.set_HealthCheck(self.get_config("set_HealthCheck")) #是否开启健康检查
            if self.get_config("set_HealthCheck") == "on": #如果开启了健康检查
                req.set_HealthCheckDomain(self.get_config("set_HealthCheckDomain"))  # 健康检查域名
                req.set_HealthCheckInterval(self.get_config("set_HealthCheckInterval"))  # 健康检查间隔
                req.set_HealthCheckURI(self.get_config("set_HealthCheckURI")) #健康检查URI
                req.set_HealthCheckTimeout(self.get_config("set_HealthCheckTimeout")) #健康检查超时时间
                req.set_HealthyThreshold(self.get_config("set_HealthyThreshold")) #健康阈值
                req.set_UnhealthyThreshold(self.get_config("set_UnhealthyThreshold")) #故障检测阈值


        #初始化一些通用的request对象
        req.set_LoadBalancerId(slb_id)
        req.set_BackendServerPort(self.get_config("set_BackendServerPort",default="80")) #后端侦听端口
        req.set_StickySession(self.get_config("set_StickySession",default="off")) #是否开启会话保持



        #初始化一些特殊的request对象参数.有可能SLB字典定义了一些自定义配置,覆盖上面的通用配置
        # 循环接收到的SLB配置参数字典.
        params = [x for x in dir(req) if x.startswith("set")]
        for key in slbdict.keys():
            if key in params:
                getattr(req, key)(slbdict[key])


        return req

    def initiate_add_slb_tag_request(self,LoadBalancerId,SlbTags = None,SlbDict = None):
        '''
        初始化创建SLB实例标签的request对象.
        :param LoadBalancerId: 实例ID
        :param SlbDict: slb配置列表
        :return: 返回request对象
        '''
        req = self.add_slb_tag_request
        req.set_LoadBalancerId(LoadBalancerId)

        if not SlbTags: #如果没有指定tag就从配置文件中读取
            SlbTags = self.get_config("SlbTags")

        req.set_Tags(SlbTags)

        if SlbDict: #如果有传递SLB配置参数

            params = [x for x in dir(req) if x.startswith("set")]
            for key in SlbDict.keys():
                if key in params:
                    getattr(req, key)(SlbDict[key])

        return req


    def initiate_check_resource_request(self):
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
        req.set_DestinationResource("InstanceType")  # 检查的资源对象是实例类型.当然也还可以检查云盘资源等

        req.set_InstanceChargeType(self.get_config('set_InstanceChargeType',default = "PostPaid")) #这里检查计费方式,如果有自定义配置,那么就参考自定义配置,否则就按"postpaid"也就是按量计费


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

    def check_instance_running(self, instance_ids):
        '''
        检查实例的状态是否为Running状态,如果是,则计数器加1.
        :param client: client对象
        :param instance_ids: 一个包含要检查的实例ID的列表
        :param log: log对象
        :return: 返回状态为running的实例个数
        '''
        # 因为阿里云单次每页最大展示资源数量是100个,所以如果查询的数量超过最大值,一次无法展示所有资源.此时就需要循环查询
        instances_mount = len(instance_ids)  # 待查询的资源数量
        page_size = 20  # 单页显示资源数量
        page_num = 1  # 初始页面值
        instances_list = []  # 循环查询所有页面结束后,所有的实例信息列表

        while True:

            # 初始化一个request对象,传递request的set参数,页面初始值是1
            request = self.check_describe_status(instance_ids, page_size, page_num)

            # 发起request调用
            response = self.send_request(request)

            if response.get('Code') is None:
                ECS_list = response.get('Instances').get('Instance')  # 拿到实例列表
                instances_list.extend(ECS_list)  # 将实例列表加入到instances_list
                rest_instances_mount = instances_mount - page_size  # 判断是否还有剩余资源要查询,如果有则继续下一页查询,否则跳出循环.

            if rest_instances_mount > 0:  # 如果剩余资源数量大于0,则设置页面值为2,继续循环查询.同时将待查询的资源数量减page_size.

                page_num += 1
                instances_mount -= page_size  # 待查询的资源数量
                continue

            else:  # 查询完毕,则跳出循环
                break

        # 循环实例信息列表.计算running状态的实例总数
        running_count = 0
        for instance_detail in instances_list:

            if instance_detail.get('Status') == "Running":
                running_count += 1

        return running_count

    def check_resource_stock(self):

        '''
        检查某个可用区下某个实例规格的库存检查工作.接收一个client对象.
        向阿里云接口进行库存查询工作.查询要创建的ECS的库存状态
        :param client:
        :return: 返回库存状态. 有三种状态:
        1.WithStock 库存充足
        2.ClosedWithStock: 库存有,但是保障不足
        3.WithoutStock: 库存告罄
        '''
        # 调用Check_Rec_Request方法初始化request参数
        request = self.initiate_check_resource_request()

        # 调用Handle_Send_Request方法发起request请求.查询库存状态.接收到一个返回的详细信息
        response = self.send_request(request)

        # 获取到各ECS实例的库存信息列表.但是如果配置文件中指定了一个明确的实例规格族,则这里的列表只有一个实例规格.
        # 如果配置文件中没有明确指定实例规格,而是指定CPU和内存的配置.那么这个列表就有许多可选实例规格.有可能是独享型,有可能是共享型.
        Ecs_Stock_List = response["AvailableZones"]["AvailableZone"][0]["AvailableResources"]["AvailableResource"][0][
            "SupportedResources"]["SupportedResource"]
        log.info("当前可用区下的相关资源库存情况:{}".format(Ecs_Stock_List))

        for ecs_stock in Ecs_Stock_List:  # 遍历列表.

            if ecs_stock["Value"] == self.config.set_InstanceType:  # 查找配置文件中指定的规格族的库存状态

                stock_status = ecs_stock["StatusCategory"]

            else:
                stock_status = None

        return stock_status


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
