#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/22 下午2:37
# @Author  : jesse
# @File    : createECS.py

#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.RunInstancesRequest import RunInstancesRequest
import uuid

client = AcsClient('LTAIFl3FW7np6VQ3', 'PQHQp0Hcx99YCEmgp1WLLv8a0VTZJ5', 'cn-hangzhou')

request = RunInstancesRequest()
request.set_accept_format('json')

request.set_InstanceChargeType("PostPaid")
request.set_AutoRenew(False)
request.set_ClientToken(str(uuid.uuid4()))
request.set_SecurityEnhancementStrategy("Active")
request.set_MinAmount(1)
request.set_Amount(2)
request.set_SystemDiskCategory("cloud_efficiency")
request.set_InternetChargeType("PayByTraffic")
request.set_PasswordInherit(False)
request.set_Password("Abc12345!")
request.set_UniqueSuffix(True)
request.set_HostName("hsq")
request.set_Description("hsq")
request.set_InstanceName("hsq")
request.set_SecurityGroupId("sg-bp1560yas86r5hl2nh5x")
request.set_InstanceType("ecs.n4.small")
request.set_ImageId("centos_7_03_64_20G_alibase_20170818.vhd")
request.set_DataDisks([
  {
    "Size": "100"
  }
])
request.set_Tags([
  {
    "Key": "hsq",
    "Value": "hsq"
  }
])

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))
