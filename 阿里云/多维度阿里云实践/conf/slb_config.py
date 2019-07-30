#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/30 下午3:08
# @Author  : jesse
# @File    : slb_config.py

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
        #https: 是否需要配置https侦听器
        #set_ListenerPort:前端侦听端口
        #set_BackendServerPort:后端服务器的端口.
        #set_StickySession="off" 是否开启会话保持
        #set_EnableHttp2="on" 是否开启http2特性
        #set_ServerCertificateId="1930648065870840_1697bae2890_-959453864_1832952232" ssl证书ID.在这个例子中的证书是m.testapi.haoshiqi.net
        #set_HealthCheck:是否需要健康检查,如果值为on.则还需要添加健康检查相关的参数
        #set_HealthCheckDomain: 健康检查域名
        #set_HealthCheckInterval: 健康检查时间间隔

slb_list = [
    {"Amount": 3, "set_AddressType": "internet", "LoadBalanceName" : ["hsq-openapi-temp1","hsq-openapi-temp2","hsq-openapi-temp3"],"set_LoadBalancerSpec" : "slb.s3.large",
     "https" : "true","set_ListenerPort" : 443,"set_BackendServerPort" : 9229,"set_StickySession" : "off","set_EnableHttp2" : "on","set_ServerCertificateId" : "1930648065870840_1697bae2890_-959453864_1832952232",
     "set_HealthCheck" : "on","set_HealthCheckDomain" : "m.testapi.haoshiqi.net", "set_HealthCheckInterval" : 50},
    {"Amount": 3, "set_AddressType": "intranet", "LoadBalanceName" : ["hsq-user-temp","hsq-message-temp","hsq-trade-temp"], "set_LoadBalancerSpec" : "slb.s2.small","https" : "false",}
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
#set_HealthCheck="off"

#负载均衡实例前端使用的端口。取值：1-65535 .整数类型变量
#set_ListenerPort=443

#负载均衡实例后端使用的端口，取值：1-65535
#set_BackendServerPort=80

#负载均衡实例的ID。
#set_LoadBalancerId

#是否开启会话保持。取值：on | off。
#StickySession="off"

#服务器证书的ID。就是ssl证书的ID
#set_ServerCertificateId="1930648065870840_1697bae2890_-959453864_1832952232"

#是否开启HTTP/2特性。取值：on（默认值）|off。
#set_EnableHttp2="on"

#是否开启Gzip压缩，对特定文件类型进行压缩。
#set_Gzip="on"

#健康检查使用的端口。整数值
#set_HealthCheckConnectPort=


'''
用于健康检查的域名。取值：

$_ip： 后端服务器的私网IP。当指定了IP或该参数未指定时，负载均衡会使用各后端服务器的私网IP当做健康检查使用的域名。

domain：域名长度为1~80，只能包含字母、数字、点号（.）和连字符（-）。
'''

#set_HealthCheckDomain

'''
健康检查正常的HTTP状态码，多个状态码用逗号（,）分割。默认值为http_2xx。

取值：http_2xx | http_3xx | http_4xx | http_5xx。
默认值:"http_2xx,http_3xx"

'''
#set_HealthCheckHttpCode

'''
健康检查的时间间隔。

取值：1-50（秒）。整数值,默认5秒

'''
#set_HealthCheckInterval




#以下参数和健康检查相关,保持默认注释即可

'''
接收来自运行状况检查的响应需要等待的时间。如果后端ECS在指定的时间内没有正确响应，则判定为健康检查失败。

取值：1-300（秒）。

说明 如果HealthCHeckTimeout的值小于HealthCheckInterval的值，则HealthCHeckTimeout无效，超时时间为HealthCheckInterval的值。
整数值,默认3秒
'''
#set_HealthCheckTimeout

#用于健康检查的URI

#set_HealthCheckURI

'''
健康检查连续成功多少次后，将后端服务器的健康检查状态由fail判定为success。

取值：2-10。默认4
'''
#set_HealthyThreshold


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