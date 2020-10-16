#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 下午5:21
# @Author  : jesse
# @File    : handle_domain.py

from domain import DNSPodApiException
from domain import Domain

class Handle_Domain(Domain):

    def __init__(self):
        super().__init__()
        if not self.domain:
            self.domain = input("请先指定需要操作的域名").strip()


    def list_info(self):
        '''
        查看域名相关信息
        :return:
        '''



