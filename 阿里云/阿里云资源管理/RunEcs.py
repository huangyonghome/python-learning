#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午3:50
# @Author  : jesse
# @File    : RunEcs.py

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
import uuid
import json

client = AcsClient('LTAIdL4dFHXnznpn', 'QdlXmv881cbUs2pWlJZkbWE78vFZvF', 'cn-hangzhou')

request = RunInstancesRequest()
request.set_accept_format('json')

# request.set_InternetMaxBandwidthOut(5)
# request.set_InstanceChargeType("PostPaid")
# request.set_AutoRenew(False)
# request.set_ClientToken(str(uuid.uuid4()))
# request.set_SecurityEnhancementStrategy("Active")
# request.set_MinAmount(1)
# request.set_Amount(2)
# request.set_SystemDiskCategory("cloud_efficiency")
# request.set_InternetChargeType("PayByTraffic")
# request.set_PasswordInherit(True)
# request.set_UniqueSuffix(True)
# request.set_HostName("hsq-testapi")
# request.set_Description("hsq")
# request.set_InstanceName("hsq-testapi")
# request.set_VSwitchId("vsw-bp188m3tbdypjmsi4qhtt")
# request.set_SecurityGroupId("sg-bp109ml84d3zd9sp2ald")
# request.set_InstanceType("ecs.n4.2xlarge")
# request.set_ImageId("m-bp1htc4i0js5ddns89zn")
# request.set_Tags([
#   {
#     "Key": "hsq",
#     "Value": "hsq"
#   }
# ])

print(request.__dict__)

# response = client.do_action_with_exception(request)
# # python2:  print(response)
# print(str(response, encoding='utf-8'))
