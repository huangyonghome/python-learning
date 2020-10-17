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
    def __init__(self,domain=None,domain_id=None,status=None,grade_title=None):
        self.domain = domain                  #域名
        self.domain_id = domain_id            #域名id
        self.status = status                  #域名状态
        self.grade_title = grade_title        #域名解析套餐规格

        #提交参数字典
        self.params = {}


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
        查看一个域名是否存在
        域名信息中包含很多信息.本方法只获取2个关键域名信息:域名状态,域名id.
        :return:
        '''

        response = submit("Domain.Info",domain = self.domain)
        if response:
            response = response.get('domain')
            self.grade_title = response.get('grade_title')
            self.domain_id = response.get('id')
            self.status = response.get('status')
        else:
            response = None

        return response

    # 创建个域名绑定
    def domain_create(self):
        '''
        参数: domain域名
        :return:
        '''
        response = submit("Domain.Create",domain = self.domain)
        print(response)

    # 修改域名状态:
    def domain_status(self):
        '''
        需要2个参数
        domain或者domain_id: 域名或者域名id
        status: 状态
        :return:
        '''
        response = submit("Domain.Status",**self.params)




if __name__ == '__main__':

    domain = Domain(domain="haoshiqi.haha")
    # domain.domain_list()
    # print(domain.domain_id)
    # domain.domain_create()
    # domain.domain_info()
    # print(domain.domain_id)
    domain.domain_info()
