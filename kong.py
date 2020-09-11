#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 下午2:16
# @Author  : jesse
# @File    : kong.py

import requests,json

url = 'http://10.0.0.101:8001/'

data = {'name':'betaapi',"protocol":"http",'host':'m.devapi.haoshiqi.net'}

#提交
server_url = url + 'services'
r = requests.post(server_url,data=data)
response = json.loads(r.text)
print(type(r.text))
print(r.text)
print(response)
print(response.get("id"))