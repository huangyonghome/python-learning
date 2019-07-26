#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 上午10:02
# @Author  : jesse
# @File    : config.py



access_key = "xxxxx"
key_secret = "xxxxxxxx"
region_id = "cn-hangzhou"

'''
配置文件格式要求:
1.格式要求为set_xxx.后面命名规范遵守驼峰命名,如果命名格式错误,则不生效
2.部分值为整数型,布尔型,列表.注意要和字符串类型区分
3.配置参数要符合阿里云OpenAPI规范.否则不被支持
4.注意配置参数的互相依赖性,和矛盾性.例如如果设置了使用自定义镜像中的密码,就不要再去设置passwd密码
'''

#ECS实例相关参数.以下参数定义了实例启动中的必要信息.

#指定创建ECS实例的数量。取值范围：1~100 .默认值：1.
set_Amount = 5

#指定ECS实例最小购买数量。取值范围：1~100.可选参数
#当ECS库存数量小于最小购买数量，会创建失败。
#当ECS库存数量大于等于最小购买数量，按照库存数量创建。

#MinAmount=1

'''
设置镜像ID.如果是自定义镜像则输入自定义镜像ID号.否则输入公共镜像ID号.下面这个例子的镜像是hsq-api-lvm500-20190625.必选参数

以下是镜像ID和镜像名,以及镜像用途的对应关系.注意不同的镜像对应的主机名也不一样
镜像ID                    镜像名                     实例主机名                     镜像用途
m-bp12jrdsuyuy2vu51nbg hsq-api-rpc-lvm500-20190625  hsq-rpc-api-temp    好食期RPC服务器镜像.磁盘500G的LVM格式分区
m-bp1htc4i0js5ddns89zn hsq-api-lvm500-20190625      hsq-api-temp        好食期api服务器镜像.磁盘500G的LVM格式分区


'''
set_ImageId = "m-bp12jrdsuyuy2vu51nbg"

#设置实例的规格族.下面列出一些经常使用到的规格族: 必选参数
# - 4核8G  共享实例: 	ecs.n4.xlarge
# - 8核16G.共享实例: ecs.n4.2xlarge  独享实例:  ecs.sn1.xlarge
# - 16核32G. 共享实例: ecs.n4.4xlarge  独享实例: 	ecs.sn1.3xlarge
# - 32核64G. 共享实例: ecs.n4.8xlarge  独享实例: 无
#
set_InstanceType = "ecs.n4.8xlarge"

#设置实例规格的CPU核数和内存.这是
#可用区,如果是华东1B区,就是cn-hangzhou-b .同理,如果是F区,就是cn-hangzhou-f.如果未指定可用区,则随机选择
set_ZoneId = "cn-hangzhou-b"

#安全组ID.比如好食期安全组ID是sg-bp11h64dz1tlkgla5344. 必选参数
set_SecurityGroupId = "sg-bp11h64dz1tlkgla5344"

#实例标签.可用添加多个标签
set_Tags = [{ "Key":"hsq","Value":"hsq"}]

#实例名称. 必选参数
set_InstanceName = "hsq-rpc-api-temp"




#主机相关参数.以下参数定义了主机名,密码等参数


#主机hostname.必选参数
set_HostName = "hsq-rpc-api-temp"


#是否为HostName和InstanceName添加有序后缀，有序后缀从001开始递增，最大不能超过999。
#例如：LocalHost001，LocalHost002和MyInstance001，MyInstance002。默认值：false

set_UniqueSuffix = True

#为实例创建个root密码
#Password=

#是否使用镜像预设的密码。使用该参数时，Password参数必须为空，同时您需要确保使用的镜像已经设置了密码。必选参数
set_PasswordInherit = True



#网络相关参数.以下参数定义了内网IP网段.公网IP.网络计费类型等

#虚拟交换机ID.比如好食期的交换机ID是vsw-bp188m3tbdypjmsi4qhtt.必选参数
set_VSwitchId = "vsw-bp188m3tbdypjmsi4qhtt"

#公网IP出口带宽.公网出带宽最大值，单位为Mbit/s。取值范围：0~100.如果值为0,则表示不分配公网IP.默认为0
#set_InternetMaxBandwidthOut=0

#网络计费类型。取值范围：
#PayByBandwidth：按固定带宽计费
#set_PayByTraffic（默认）：按使用流量计费

#set_InternetChargeType=PayByTraffic



#磁盘相关参数.如果是使用自定义镜像的话,数据磁盘可用不需要定义.以下参数默认即可

#已停售的实例规格且非I/O优化实例默认值为cloud，否则默认值为cloud_efficiency。取值范围：

#cloud：普通云盘
#cloud_efficiency：高效云盘
#cloud_ssd：SSD 云盘
#ephemeral_ssd：本地 SSD 盘
#cloud_essd：ESSD 云盘

#1.系统磁盘类型.默认为高效云盘.默认大小为镜像(无论是公共镜像还是自定义镜像的大小)
#set_SystemDisk.Category=cloud_efficiency


#2.数据磁盘: 数据磁盘是一个包含字典的列表,如果是有多个数据磁盘,就定义多个字典

#数据磁盘 主要有2个参数: Size和Category

#Size: 数据磁盘容量.单位BiG取值范围：

#cloud：5~2000
#cloud_efficiency：20~32768
#cloud_ssd：20~32768
#cloud_essd：20~32768
#ephemeral_ssd：5~800

#Category: 磁盘类型.参考系统磁盘类型

#例如下面定义了2个数据磁盘,容量分别是1024和2048
#set_DataDisk=[{"Size":"1024","Category":"cloud_efficiency"},{"Size":"2048","Category":"cloud_efficiency"}]




#计费相关.如果是按量计费.则以下参数默认即可

#1.实例的付费方式。取值范围：

#PrePaid：预付费，包年包月。 选择预付费时，您必须确认自己的账号支持余额支付或者信用支付，否则将返回 InvalidPayMethod 的错误提示。
#PostPaid（默认）：按量付费。选择预付费时，您必须确认自己的账号支持信用支付，否则将返回 InvalidPayMethod 的错误提示。

#set_InstanceChargeType = "PostPaid"


#2.购买资源的时长。可选值：
#Week
#Month（默认)

#set_PeriodUnit=Month


#3.购买资源的时长，单位为：月。当参数 InstanceChargeType 取值为 PrePaid 时才生效且为必选值。一旦指定了 DedicatedHostId，则取值范围不能超过专有宿主机的订阅时长。取值范围：

#PeriodUnit=Week时，Period取值：{“1”, “2”, “3”, “4”}
#PeriodUnit=Month时，Period取值：{ “1”, “2”, “3”, “4”, “5”, “6”, “7”, “8”, “9”, “12”, “24”, “36”,”48”,”60”}

#set_Period=


#4.是否要自动续费。当参数 InstanceChargeType 取值 PrePaid 时才生效。取值范围：

#True：自动续费。
#False（默认）：不自动续费。

#set_AutoRenew=False


#5.单次自动续费的续费时长。取值范围：

#PeriodUnit=Week 时：{“1”, “2”, “3”}
#PeriodUnit=Month 时：{“1”, “2”, “3”, “6”, “12”}
#默认值：1

#set_AutoRenewPeriod=1