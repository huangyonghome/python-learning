#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/24 上午10:02
# @Author  : jesse
# @File    : config.py

access_key = ""
key_secret = ""
region_id = "cn-hangzhou"

'''
配置文件格式要求:

配置文件包含两大块: 1.ECS相关 2.SLB相关
1.格式要求为set_xxx.后面命名规范遵守驼峰命名,如果命名格式错误,则不生效
2.部分值为整数型,布尔型,列表.注意要和字符串类型区分
3.配置参数要符合阿里云OpenAPI规范.否则不被支持
4.注意配置参数的互相依赖性,和矛盾性.例如如果设置了使用自定义镜像中的密码,就不要再去设置passwd密码
'''

#ECS实例相关参数.以下参数定义了实例启动中的必要信息.

#指定创建ECS实例的数量。取值范围：1~100 .默认值：1.
set_Amount = 20

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
'''
实例名称。长度为2~128个字符，必须以大小字母或中文开头，不能以http://和https://开头。可以包含中文、英文、数字、半角冒号（:）、下划线（_）、点号（.）或者连字符（-）。默认值为实例的InstanceId。

说明 创建多台ECS实例时，您可以使用UniqueSuffix为这些实例设置不同的实例名称。您也可以使用name_prefix[begin_number,bits]name_suffix的命名格式设置有序的实例名称，例如，设置InstanceName取值为k8s-node-[1,4]-alibabacloud，则第一台ECS实例的实例名称为k8s-node-0001-alibabacloud 。详情请参见API FAQ。
当实例名称或主机名称不设置命名后缀name_suffix，即命名格式为name_prefix[begin_number,bits]时，UniqueSuffix不生效。例如，当InstanceName取值为instance-[99,3]，UniqueSuffix取值为true时，生效的实例名称为instance099，而不是instance099001。
'''
set_InstanceName = "hsq-api-temp"




#主机相关参数.以下参数定义了主机名,密码等参数


#主机hostname.必选参数
set_HostName = "hsq-apitest-temp"


#是否为HostName和InstanceName添加有序后缀，有序后缀从001开始递增，最大不能超过999。
#例如：LocalHost001，LocalHost002和MyInstance001，MyInstance002。默认值：false

#set_UniqueSuffix = True

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


'''
###############################################################################################################################################
#####                                                   2.  SLB相关                                                                       ######
#####                                                                                                                                    ######
#####                                                                                                                                    ######
#####                                                                                                                                    ######
###############################################################################################################################################
'''

#slb_list的列表有2个功能:
#1.创建SLB实例
#2.创建侦听器

#这个配置不在API请求中,但是SLB的API不支持批量创建.所以只能通过循环调用API的方式去创建.把要创建的通用性参数定义成一个列表,从列表中循环读取配置.对于通用性的公共配置(比如可用区,按量计费等)直接读取配置文件

#代码只读取以下2个列表和一些公共的配置参数,所以对于部分配置和一些少数不常用的配置,如果想要配置生效,需要加入到以下这个列表,代码不会再去遍历配置文件的所有参数

#定义一个SLB的通用性配置.列表中的2个元素表示公网和私网SLB的两种配置,列表中的字典可以直接注释.但是字典中的KEY不能修改.

#以下是列表中key的意义:
        # Amount表示创建的数量,
        #set_AddressType:公网或者私网SLB类型
        #LoadBalanceName:slb实例名称.必须是列表类型
        #set_LoadBalancerSpec表示SLB实例的规格.如果是要创建共享型的实例规格,则删掉"set_LoadBalancerSpec"项.
        #listener:侦听器类型,有三种可选,https,http,tcp
        #backends: SLB的后端真实服务器,支持通配符正则.记住,要加入SLB的服务器必须在running状态
        #如果是通用配置,代码会自动读取文件,不需要配置,但是如果是自定义配置,需要写入到这个列表里.

slb_list = [
    {"Amount": 1, "set_AddressType": "internet", "LoadBalanceName" : ["hsq-openapi-temp7","hsq-openapi-temp2","hsq-openapi-temp3"],"set_LoadBalancerSpec" : "slb.s1.small",
     "listener" : ["https","http"],"backends":["hsq-openapi-temp","hsq-api5"]},
    {"Amount": 1, "set_AddressType": "intranet", "LoadBalanceName" : ["hsq-user-temp7","hsq-message-temp","hsq-trade-temp"], "set_LoadBalancerSpec" : "slb.s1.small",
     "listener" : ["http"],"set_HealthCheckDomain" : "user.center.haoshiqi.net","backends": [ "hsq-openapi-temp", "hsq-api5"]}
 ]



#一.重要,常用的配置参数:

'''
1.负载均衡实例的网络类型。取值：

internet：创建公网负载均衡实例后，系统会分配一个公网IP地址，可以转发公网请求。
intranet：创建内网负载均衡实例后，系统会分配一个内网IP地址，仅可转发内网请求。
参数值为字符串类型.
'''

set_AddressType="intranet"


'''
2.字符串类型.公网类型实例的付费方式。取值：

paybybandwidth：按带宽计费。
paybytraffic：按流量计费（默认值）。
参数值为字符串类型.
'''

set_InternetChargeType="paybytraffic"


'''
3.SLB实例名称.长度为2-128个英文或中文字符，必须以大小字母或中文开头，可包含数字，点号（.），下划线（_）和短横线（-）
不指定该参数时，默认由系统分配一个实例名称。
参数值为字符串类型.
'''

set_LoadBalancerName="hsq-openapi-temp"


'''
4.负载均衡实例的规格。取值：

slb.s1.small
slb.s2.small
slb.s2.medium
slb.s3.small
slb.s3.medium
slb.s3.large
若不指定规格，则创建性能共享型实例。
参数值为字符串类型.
'''

#set_LoadBalancerSpec=


'''
5.负载均衡实例的主可用区ID。
参数值为字符串类型.
'''
set_MasterZoneId="cn-hangzhou-b"

'''
6.负载均衡实例的备可用区ID。
参数值为字符串类型.
'''
set_SlaveZoneId="cn-hangzhou-d"


'''
7.实例的计费类型，取值：

PayOnDemand：按量付费。
PrePay：预付费。
参数值为字符串类型.
'''

set_PayType="PayOnDemand"


'''
8.专有网络实例的所属交换机ID。

创建专有网络类型的负载均衡实例，必须指定该参数。如果指定了该参数，AddessType参数的值会默认被设置为intranet。
'''

set_VSwitchId="vsw-bp188m3tbdypjmsi4qhtt"

#9.负载均衡实例的所属的VPC ID。
set_VpcId="vpc-bp11mmoyrvgbqzt1q2gb4"



#10.字符串类型. 指定负载均衡实例的私网IP地址，该地址必须包含在交换机的目标网段下.
#set_Address="xx.xx.xx.xx"

#slb标签
SlbTags = [{ "Key":"hsq","Value":"hsq"}]


#以下是一些不常用的参数,如果要使用这些参数,需要加入到配置文件开头的列表中

'''
预付费公网实例的购买时长，取值：

如果PricingCycle为month，取值为1~9。
如果PricingCycle为year，取值为1~3。
'''
#set_Duration

'''
预付费公网实例的计费周期，取值：month|year

'''
#set_PricingCycle="month"

#整数类型. 监听的带宽峰值。
#set_Bandwidth=




'''
###############################################################################################################################################
#####                                                   3.  SLB侦听器配置相关                                                                       ######
#####                                                                                                                                    ######       
#####                                                                                                                                    ######       
#####                                                                                                                                    ######   
###############################################################################################################################################
'''




#是否开启健康检查。取值：on | off。
set_HealthCheck="on"

#负载均衡实例http侦听器前端使用的端口。取值：1-65535 .整数类型变量.一般https规定为443,http的值可以自定义,但是一般是80,除非很有必要,否则不要修改
set_ListenerPort=80

#负载均衡实例后端使用的端口，取值：1-65535.除非很有必要,否则不要修改
set_BackendServerPort=80

#负载均衡实例的ID。
#set_LoadBalancerId

#是否开启会话保持。取值：on | off。
set_StickySession="off"

#服务器证书的ID。就是ssl证书的ID
set_ServerCertificateId="1930648065870840_1697bae2890_-959453864_1832952232"

#是否开启HTTP/2特性。取值：on（默认值）|off。
set_EnableHttp2="on"

#是否开启Gzip压缩，对特定文件类型进行压缩,默认on。
#set_Gzip="on"



'''
用于健康检查的域名。取值：

$_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。

domain：域名长度为1~80，只能包含字母、数字、点号（.）和连字符（-）。
'''

set_HealthCheckDomain="m.testapi.haoshiqi.net"

'''
健康检查正常的HTTP状态码，多个状态码用逗号（,）分割。默认值为http_2xx。

取值：http_2xx | http_3xx | http_4xx | http_5xx。
默认值:"http_2xx,http_3xx"

'''
#set_HealthCheckHttpCode = "http_2xx,http_3xx"

'''
健康检查的时间间隔。

取值：1-50（秒）。整数值,默认5秒

'''
set_HealthCheckInterval=50

#用于健康检查的URI

set_HealthCheckURI="/"



#以下参数和健康检查相关,保持默认即可

'''
#健康检查使用的端口。整数值
'''

set_HealthCheckConnectPort = 80


'''
接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。

取值：1-300（秒）。

说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
整数值,默认3秒
'''
set_HealthCheckTimeout = 50

'''
健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。

取值：2~10
'''
set_HealthyThreshold = 2

'''
健康检查连续失败多少次后，将后端服务器的健康检查状态由success判定为fail。

取值：2~10。
'''
set_UnhealthyThreshold = 2




'''
指定连接空闲超时时间，取值范围为1-60秒，默认值为15秒。

在超时时间内一直没有访问请求，负载均衡会暂时中断当前连接，直到一下次请求来临时重新建立新的连接。
'''
#set_IdleTimeout=

'''
调度算法。取值：

wrr（默认值）：权重值越高的后端服务器，被轮询到的次数（概率）也越高。
wlc：除了根据每台后端服务器设定的权重值来进行轮询，同时还考虑后端服务器的实际负载（即连接数）。当权重值相同时，当前连接数越小的后端服务器被轮询到的次数（概率）也越高。
rr：按照访问顺序依次将外部请求依序分发到后端服务器。
'''
#set_Scheduler


'''
只有性能保障型实例才可以指定TLSCipherPolicy参数，每种policy定义了一种安全策略，安全策略包含HTTPS可选的TLS协议版本和配套的加密算法套件。默认:tls_cipher_policy_1_1
'''

#set_TLSCipherPolicy






