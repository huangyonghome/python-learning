#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 下午4:47
# @Author  : jesse
# @File    : handle_request.py



import set_request
from conf import config
import handle_log
import json
import sys

from aliyunsdkecs.request.v20140526.DescribeAvailableResourceRequest import DescribeAvailableResourceRequest


def Handle_Send_Request(request,client,log):
    '''
    向阿里云API提交request的统一处理方法.
    :param client: client实例
    :param request: request对象
    :param log: log日志实例对象
    :return: 返回响应的json数据
    '''
    request.set_accept_format('json')
    try:
        response = client.do_action_with_exception(request).decode("utf-8")
        log.debug(response)
        response_detail = json.loads(response)
        return response_detail
    except Exception as e:
        log.error(e)
        sys.exit(1)

def Handle_Instance_Running(client,instance_ids,log):
    '''
    检查实例的状态是否为Running状态,如果是,则计数器加1.
    :param client: client对象
    :param instance_ids: 一个包含要检查的实例ID的列表
    :param log: log对象
    :return: 返回状态为running的实例个数
    '''
    #因为阿里云单次每页最大展示资源数量是100个,所以如果查询的数量超过最大值,一次无法展示所有资源.此时就需要循环查询
    instances_mount = len(instance_ids)  #待查询的资源数量
    page_size = 20 #单页显示资源数量
    page_num = 1 #初始页面值
    instances_list = [] #循环查询所有页面结束后,所有的实例信息列表

    while True:

        # 初始化一个request对象,传递request的set参数,页面初始值是1
        request = set_request.Set_Describe_Request(instance_ids, page_num)

        # 发起request调用
        response = Handle_Send_Request(request, client, log)

        if response.get('Code') is None:
            ECS_list = response.get('Instances').get('Instance')  # 拿到实例列表
            instances_list.extend(ECS_list)  # 将实例列表加入到instances_list
            rest_instances_mount = instances_mount - page_size  # 判断是否还有剩余资源要查询,如果有则继续下一页查询,否则跳出循环.




        if rest_instances_mount > 0: #如果剩余资源数量大于0,则设置页面值为2,继续循环查询.同时将待查询的资源数量减page_size.

            page_num += 1
            instances_mount -= page_size #待查询的资源数量
            continue

        else: #查询完毕,则跳出循环
            break


    #循环实例信息列表.计算running状态的实例总数
    running_count = 0
    for instance_detail in instances_list:

        if instance_detail.get('Status') == "Running":
            running_count += 1
            print("running_count:",running_count)

    return running_count

def Handle_Resource_Check(client,log):

    '''
    检查某个可用区下某个实例规格的库存检查工作.接收一个client对象.
    向阿里云接口进行库存查询工作.查询要创建的ECS的库存状态
    :param client:
    :return: 返回库存状态. 有三种状态:
    1.WithStock 库存充足
    2.ClosedWithStock: 库存有,但是保障不足
    3.WithoutStock: 库存告罄
    '''
    #调用Check_Rec_Request方法初始化request参数
    request = set_request.Set_Resource_Request()

    #调用Handle_Send_Request方法发起request请求.查询库存状态.接收到一个返回的详细信息
    response = Handle_Send_Request(request,client,log)


    #获取到各ECS实例的库存信息列表.但是如果配置文件中指定了一个明确的实例规格族,则这里的列表只有一个实例规格.
    #如果配置文件中没有明确指定实例规格,而是指定CPU和内存的配置.那么这个列表就有许多可选实例规格.有可能是独享型,有可能是共享型.
    Ecs_Stock_List = response["AvailableZones"]["AvailableZone"][0]["AvailableResources"]["AvailableResource"][0]["SupportedResources"]["SupportedResource"]
    log.info("当前可用区下的相关资源库存情况:{}".format(Ecs_Stock_List))

    for ecs_stock in Ecs_Stock_List: #遍历列表.

        if ecs_stock["Value"] == config.set_InstanceType: #查找配置文件中指定的规格族的库存状态

            stock_status = ecs_stock["StatusCategory"]

        else:
            stock_status = None

    return stock_status


