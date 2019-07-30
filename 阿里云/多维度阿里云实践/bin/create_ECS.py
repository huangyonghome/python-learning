#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午4:29
# @Author  : jesse
# @File    : create_ECS.py

import sys,os


BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)


from conf import config
from conf import slb_config
from common import client
from common.handle_log import log

import time

class CreateInstance:

    def __init__(self):

        #实例化一个client对象
        self.client = client.AliClient()

    def create_ecs(self):
        '''
        1.实例化一个client对象
        2.检查需要创建的ECS规格族的阿里云库存资源.如果库存告罄或者库存为None,则不创建库存
        3.调用set_request下的Set_Create_ECS_Request函数实例化一个request对象
        4.发起调用
        :return:

        '''

        #获取资源库存状态
        stock_status = self.client.check_resource_stock()

        #判断资源库存状态,是否还有库存.如果还有库存.则创建ECS
        if not stock_status or stock_status == "WithoutStock":
            log.error("当前实例规格库存不足,请选择其他实例规格.......")
            return

        else:
            #初始化RunInstances接口的request对象
            request = self.client.initiate_ecs_reques()
            #发送request申请创建实例
            log.info("开始创建ECS服务器")
            response = self.client.send_request(request)

            #检查是否所有主机状态都是running了
            log.info("开始检查所有的ECS实例状态")
            if response.get('Code') is None:
                instance_ids = response.get('InstanceIdSets').get('InstanceIdSet')
                running_amount = 0
                while running_amount < config.set_Amount:
                    time.sleep(10)
                    running_amount =  self.client.check_instance_running(instance_ids)
            log.info("ecs instance {} is running".format(instance_ids))



    def create_slb(self):

        if hasattr(config,"slb_list"): #如果有定义SLB配置列表参数
            SlbAmount = len(config.slb_list) #获取列表的元素个数


            i = 0

            while i <= SlbAmount - 1: #循环列表中的元素.可能有定义公网SLB或者私网SLB,有可能2个类型都有定义
                SlbDict = config.slb_list[i]   #获取列表中的子字典

                Amount = SlbDict.get('Amount') #获取要创建的SLB实例个数
                LoadBalanceNameList = SlbDict.get("LoadBalanceName") #获取slb名字的个数
                Listener = SlbDict.get("listener") #获取要配置的侦听器的类型

                if not Amount or not LoadBalanceNameList or not Listener: #如果获取配置失败,抛出异常
                    raise AttributeError
                elif len(LoadBalanceNameList) < Amount:   #抛出异常
                    raise IndexError("SLB名称数量小于要创建的SLB个数")

                for j in range(Amount):  #根据要创建的SLB数量,循环初始化request,创建SLB
                    LoadBalanceName = LoadBalanceNameList[j]
                    request = self.client.initiate_createSLB_request(SlbDict,LoadBalanceName) #调用初始化request函数,传入要创建的SLB字典和SLB名称
                    log.info("开始创建SLB实例,实例名:{}".format(LoadBalanceName))
                    response = self.client.send_request(request)
                    LoadBalancerId = response.get("LoadBalancerId")  # 获取创建的SLB实例ID

                    #给实例添加标签
                    self.add_slb_tag(LoadBalancerId,SlbDict)

                    #创建SLB的侦听器
                    LoadBalancerId = response.get("LoadBalancerId") #获取创建的SLB实例ID
                    for listen in Listener: #循环创建侦听器
                        request = self.client.initiate_createSLBlistener_request(listen,SlbDict,LoadBalancerId) #实例化创建侦听器request对象.传入3个参数.分别是侦听器类型,slb字典参数,以及刚创建的SLB实例ID
                        log.info("开始创建SLB的{}侦听,实例名:{}".format(listen,LoadBalanceName))
                        response = self.client.send_request(request) #创建侦听器

                    j += 1 #循环创建下一个SLB
                i += 1 #循环下一个SLB字典

    def add_slb_tag(self,LoadBalancerId,SlbDict=None):
        '''
        给SLB实例添加标签
        :param LoadBalancerId:
        :param SlbDict:
        :return:
        '''
        #实例化request对象
        request = self.client.initiate_add_slb_tag_request(LoadBalancerId,SlbDict)
        #调用add_tag的API接口
        response = self.client.send_request(request)








instance = CreateInstance()
instance.create_slb()


