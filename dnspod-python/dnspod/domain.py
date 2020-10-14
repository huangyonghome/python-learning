#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 下午4:40
# @Author  : jesse
# @File    : domain.py


from apicn import ApiCn
from handle_request import submit


class Domain(ApiCn):
    def __init__(self,domain=None,url=None,domain_id=None,domain_status=None):
        self.domain = domain
        self.url = url
        self.domain_id = domain_id
        self.domain_status = domain_status
        # super


    def DomainList(self):
        response = submit("Domain.List")
        domain_info = response.get('domains')
        for item in domain_info:
            if item.get("name") == self.domain:
                self.domain_id = item.get("id")
                break
        else:
            self.domain_id = None


    def DomainInfo(self):
        response = submit("Domain.Info",domain = self.domain)
        self.domain_id = response.get('domain').get('id')
        self.domain_status = response.get('domain').get('status')


    def DomainCreate(self):
        self.DomainList()
        if not self.domain_id:
            response = submit("Domain.Create",domain = self.domain)
            print("domain:{}.已经存在".format(self.domain))
        else:
            print("domain:{}.已经存在".format(self.domain))


    def DomainStatus(self):




domain = Domain(domain="iqg.net")
# domain.DomainList()
# print(domain.domain_id)
# domain.DomainCreate()
domain.DomainInfo()
print(domain.domain_id)

