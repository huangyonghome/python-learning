#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午4:29
# @Author  : jesse
# @File    : create_ECS.py

import sys,os


BASE_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(BASE_PATH)


from conf import config
from common import set_request
from common import handle_request
from common import handle_log
import time

log = handle_log.load_my_logging_cfg()


def Create_Ecs():
    '''
    1.实例化一个client对象
    2.检查需要创建的ECS规格族的阿里云库存资源.如果库存告罄或者库存为None,则不创建库存
    3.调用set_request下的Set_Create_ECS_Request函数实例化一个request对象
    4.发起调用
    :return:

    '''
    client = set_request.Set_Client() #实例化client对象

    #获取资源库存状态
    stock_status = handle_request.Handle_Resource_Check(client,log)

    #判断资源库存状态,是否还有库存.如果还有库存.则创建ECS
    if not stock_status or stock_status == "WithoutStock":
        log.error("当前实例规格库存不足,请选择其他实例规格.......")
        return

    else:
        #初始化RunInstances接口的request对象
        request = set_request.Set_RunInstanse_Request()
        #发送request申请创建实例
        log.info("开始创建ECS服务器")
        response = handle_request.Handle_Send_Request(request,client,log)

        #检查是否所有主机状态都是running了
        log.info("开始检查所有的ECS实例状态")
        if response.get('Code') is None:
            instance_ids = response.get('InstanceIdSets').get('InstanceIdSet')
            running_amount = 0
            while running_amount < config.set_Amount:
                print(running_amount)
                print(config.set_Amount)
                time.sleep(10)
                running_amount =  handle_request.Handle_Instance_Running(client,instance_ids,log)
        log.info("ecs instance {} is running".format(instance_ids))




Create_Ecs()


