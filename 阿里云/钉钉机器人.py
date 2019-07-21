#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/10 下午4:12
# @Author  : jesse
# @File    : 钉钉机器人.py


import requests
import json

class DingTalk:

    def __init__(self):
        self.header = {'Content-Type': 'application/json;charset=utf-8'}
        self.url = "https://oapi.dingtalk.com/robot/send?access_token=f064adad17bc66ad30d94c7c9c5393c8489cc94c8b4b2e866ffe70045bbee0bd"

    def send_msg(self,text):

        json_text = {
            "msgtype": "text",
            "text": {
                "content": text
            },
            "at": {
                "atMobiles": ["17749739691"],
                "isAtAll": False
            }
        }

        requests.post(self.url, data=json.dumps(json_text), headers=self.header)


if __name__ == "__main__":
    dingding = DingTalk()
    dingding.send_msg('SSL证书:{}将在{}天后到期,\n详细请查看:{}'.format("m.dev.haoshiqi.net",7,"https://m.dev.haoshiqi.net"))

