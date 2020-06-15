# -*- coding: utf-8 -*-
# @Time    : 2019-07-31 23:57
# @Author  : jesse
# @File    : python08.gevent使用案例.py

#
# from urllib.request import urlopen
# import requests

# url = 'https://www.baidu.com'
#
# res = urlopen(url)
# res1 = res.read().decode("utf-8")
#
# # print(res1)
#
# res2 = requests.get(url)
# res_2 = res2.content.decode("utf-8")
#
# # print(res_2)
#
# print(len(res_2))


import requests
from gevent import monkey;monkey.patch_all()
import gevent

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf-8")
    return len(content)

g1 = gevent.spawn(get_url,'http://www.baidu.com')
g2 = gevent.spawn(get_url,'http://www.163.com')
g3 = gevent.spawn(get_url,'http://www.taobao.com')
g4 = gevent.spawn(get_url,'http://www.jd.com')

# gevent.joinall([g1,g2,g3,g4])
gevent.joinall([g1])
print(g1.value)
# print(g2.value)
# print(g3.value)
# print(g4.value)