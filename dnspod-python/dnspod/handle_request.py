#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 下午5:02
# @Author  : jesse
# @File    : handle_request.py

import auth
import json
import requests

class DNSPodApiException(Exception):
    pass


def submit(path,**kwargs):
    login_token = auth.login_token
    base_url = "dnsapi.cn/"
    data_dict = kwargs
    data_dict.update(dict(login_token=login_token,format="json"))
    headers = {
        "Content-type": "application/x-www-form-urlencoded",
        "Accept": "text/json",
        "User-Agent": "dnspod-python/0.01 (jessehuang; DNSPod.CN API v2.8)"
    }
    url = "https://" + base_url + path
    response = requests.post(url, data=data_dict, headers=headers)
    data = response.text
    ret = json.loads(data)
    if ret.get("status", {}).get("code") == "1":
        return ret
    else:
        raise DNSPodApiException(ret)