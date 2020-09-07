# -*- coding: utf-8 -*-
# @Time    : 2020-09-07 21:56
# @Author  : jesse
# @File    : request_practise.py

import requests
from requests.auth import HTTPBasicAuth

url = 'http://172.16.20.101:9200/_cat/health'
r=requests.get(url,auth=HTTPBasicAuth('elastic','Ld73vPze2c'))
print(r.status_code)
print(r.text)

print(r.text.split())

