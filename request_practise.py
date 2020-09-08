# -*- coding: utf-8 -*-
# @Time    : 2020-09-07 21:56
# @Author  : jesse
# @File    : request_practise.py

import requests
from lxml import etree
from requests.auth import HTTPBasicAuth

# url = 'http://172.16.20.101:9200/_cat/health'
# r=requests.get(url,auth=HTTPBasicAuth('elastic','Ld73vPze2c'))
# print(r.status_code)
# print(r.text)
#
# print(r.text.split())


url = 'https://accounts.douban.com/j/mobile/login/basic'

#
# r = requests.get(url,auth=HTTPBasicAuth('7865227@qq.com','xxxx'))
#
# print(r.status_code)
# print(r.text)

data = {
            "ck": "",
            "name": '7865227@qq.com',
            "password": 'hyliqin1987',
            "remember": "false"
        }

headers = {
            "Host": "accounts.douban.com",
            "Origin": "https://accounts.douban.com",
            "Referer": "https://accounts.douban.com/passport/login",
            "Upgrade-Insecure-Requests": "1",
            "User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'

}

proxies = {
            "http": "http://127.0.0.1:8080",
            "https": "https://127.0.0.1:8080"
        }

session = requests.session()
session.headers = headers
# session.proxies = proxies

r = session.post(url,data=data,headers=headers)

print(r.status_code)
response = session.get('https://accounts.douban.com/passport/setting',headers=headers)
print(response.text)

html = etree.HTML(response.text)
print(html.xpath('//div[@class="account-form-field"]/input/@value')[0])