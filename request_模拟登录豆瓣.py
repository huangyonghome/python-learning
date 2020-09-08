# -*- coding: utf-8 -*-
# @Time    : 2020-09-07 21:56
# @Author  : jesse
# @File    : request_practise.py

import requests
from lxml import etree
from requests.auth import HTTPBasicAuth

'''
博客:
https://www.pianshen.com/article/3077218787/
'''


url = 'https://accounts.douban.com/j/mobile/login/basic'

data = {
            "ck": "",
            "name": '7865227@qq.com',
            "password": '',
            "remember": "false"
        }

headers = {
            "Host": "accounts.douban.com",
            "Origin": "https://accounts.douban.com",
            "Referer": "https://accounts.douban.com/passport/login",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

}


session = requests.session()
session.headers = headers


r = session.post(url,data=data,headers=headers)

print(r.status_code)
response = session.get('https://accounts.douban.com/passport/setting',headers=headers)
print(response.text)

html = etree.HTML(response.text)
print(html.xpath('//div[@class="account-form-field"]/input/@value')[0])