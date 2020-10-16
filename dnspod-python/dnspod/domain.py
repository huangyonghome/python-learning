#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/14 下午4:40
# @Author  : jesse
# @File    : domain.py


from handle_request import submit

class DNSPodApiException(Exception):
    pass


# dnspod域名相关
class Domain():
    def __init__(self,domain=None,domain_id=None,domain_status=None,):
        self.domain = domain
        self.domain_id = domain_id
        self.domain_status = domain_status


    # 获取所有域名列表信息. 暂时还没使用该方法
    def domain_list(self):
        response = submit("Domain.List")
        domain_info = response.get('domains')
        for item in domain_info:
            if item.get("name") == self.domain:
                self.domain_id = item.get("id")
                break
        else:
            self.domain_id = None

    # 查看单个域名信息
    def domain_info(self):
        '''
        域名信息中包含很多信息.本方法只获取2个关键域名信息:域名状态,域名id.
        :return:
        '''

        response = submit("Domain.Info",domain = self.domain)
        print(response)
        self.domain_id = response.get('domain').get('id')
        self.domain_status = response.get('domain').get('status')

    # 创建个域名绑定
    def domain_create(self):
        '''
        参数: domain域名
        :return:
        '''
        # 先判断域名是否已经创建
        self.domain_list()
        if not self.domain_id:
            response = submit("Domain.Create",domain = self.domain)
            print("域名:{}.已成功创建".format(self.domain))
        else:
            print("域名:{}.已经存在".format(self.domain))


    # 修改域名状态:
    def domain_status(self):
        '''
        需要2个参数
        domain或者domain_id: 域名或者域名id
        status: 状态
        :return:
        '''
        response = submit("Domain.Status", domain=self.domain,status=self.domain_status)
        print("域名:{}状态已经变更.当前状态为:{}.".format(self.domain,self.domain_status))



if __name__ == '__main__':

    domain = Domain(domain="haoshiqi.net")
    # domain.domain_list()
    # print(domain.domain_id)
    # domain.domain_create()
    # domain.domain_info()
    # print(domain.domain_id)
    domain.domain_info()
