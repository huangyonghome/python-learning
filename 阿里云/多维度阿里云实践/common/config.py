#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/1 下午4:50
# @Author  : jesse
# @File    : config.py

class config:
    '''
    公共配置文件类.定义公共的配置属性
    '''
    def __init__(self):

        '''
        accessy相关
        '''
        self.access_key = "xxx"
        self.key_secret = "xxx"
        self.region_id = "cn-hangzhou"

        '''
        ecs相关
        '''
        self.set_ZoneId = "cn-hangzhou-b" #可用区
        self.set_InstanceChargeType = "PostPaid" #按量计费


        '''
        SLB相关
        '''
        self.set_InternetChargeType="paybytraffic" #按流量计费
        set_HealthCheck = "on"
        set_ListenerPort = 80
        set_BackendServerPort = 80
        set_StickySession = "off"
        set_EnableHttp2 = "on"
        set_HealthCheckInterval = 50
        set_HealthCheckURI = "/"
        set_HealthCheckTimeout = 50
        set_HealthyThreshold = 2
        set_UnhealthyThreshold = 2


class hsq(config):

    '''
    好食期项目自定义配置类
    '''
    def __init__(self):
        super().__init__()
        # ECS相关
        self.set_ImageId = "m-bp12jrdsuyuy2vu51nbg"
        self.set_InstanceType = "ecs.sn1.xlarge"
        self.set_SecurityGroupId = "sg-bp11h64dz1tlkgla5344"
        self.set_Tags = [{"Key": "hsq", "Value": "hsq"}]
        self.set_VSwitchId = "vsw-bp188m3tbdypjmsi4qhtt"

        #SLB相关
        set_MasterZoneId = "cn-hangzhou-b"
        set_SlaveZoneId = "cn-hangzhou-d"
        set_PayType = "PayOnDemand"
        set_VSwitchId = "vsw-bp188m3tbdypjmsi4qhtt"
        set_VpcId = "vpc-bp11mmoyrvgbqzt1q2gb4"


class hsq_activity(hsq,config):
    '''
    好食期会员日活动配置模板
    '''
    def __init__(self):
        super().__init__()
        #ECS相关
        OpenImageID = "m-bp1htc4i0js5ddns89zn"
        RpcImageID = "m-bp12jrdsuyuy2vu51nbg"
        self.set_PasswordInherit = True  # 使用镜像密码
        set_InstanceType = "ecs.n4.8xlarge"
        set_UniqueSuffix = True

        #slb相关
        set_HealthCheckDomain = "m.testapi.haoshiqi.net"
        set_ServerCertificateId = "1930648065870840_1697bae2890_-959453864_1832952232"


        slb_list = [
            {"Amount": 1, "set_AddressType": "internet",
             "LoadBalanceName": ["hsq-openapi-temp7", "hsq-openapi-temp2", "hsq-openapi-temp3"],
             "set_LoadBalancerSpec": "slb.s1.small",
             "listener": ["https", "http"],
             "backends": ["hsq-openapi-temp", "hsq-api5"]},
            {"Amount": 1, "set_AddressType": "intranet",
             "LoadBalanceName": ["hsq-user-temp7", "hsq-message-temp", "hsq-trade-temp"],
             "set_LoadBalancerSpec": "slb.s1.small",
             "listener": ["http"],
             "set_HealthCheckDomain": "user.center.haoshiqi.net",
             "backends": ["hsq-openapi-temp", "hsq-api5"]}
        ]






