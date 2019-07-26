
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest
import json

client = AcsClient('LTAIdL4dFHXnznpn', 'QdlXmv881cbUs2pWlJZkbWE78vFZvF', 'cn-hangzhou')

request = DescribeInstancesRequest()
request.set_accept_format('json')

request.set_PageSize(100)
request.set_Tags([
  {
    "value": "hsq",
    "key": "hsq"
  }
])

response = client.do_action_with_exception(request)
# python2:  print(response)
print(str(response, encoding='utf-8'))

response = response.decode("utf-8")
response = json.loads(response)

response_detail = (response.get("Instances").get("Instance"))
instance_list = []

for instance in response_detail:

    instance_list.append(instance.get('InstanceName'))

print(instance_list)