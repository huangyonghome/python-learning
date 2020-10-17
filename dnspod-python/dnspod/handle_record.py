#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/15 下午4:35
# @Author  : jesse
# @File    : handle_record.py

import re
from record import Record
from domain import DNSPodApiException


#判断一个字符串是否为IP地址
def is_ip_avaliable(ip):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(ip):
        return True
    else:
        return False


class HandleRecord(Record):
    '''
    处理DNS解析记录工作
    '''
    def __init__(self):
        super().__init__()


    def auth_paras(self):
        '''
        验证用户输入的参数是否正确
        :param record_type:
        :param value:
        :param ttl:
        :param mx:
        :return:
        '''
        # 判断解析记录类型
        if not self.record_type:
            # 默认为A记录
            self.record_type = "A"

        elif self.record_type.upper() == "CNAME" or self.record_type.upper() == "TXT":
            self.record_type = self.record_type.upper()

        else:
            raise DNSPodApiException("解析记录输入错误.请重新输入")

        # 判断value
        if not self.value: raise DNSPodApiException("解析值输入有误,必须指定解析值.请重新输入")

        if self.record_type == "A":
            # 如果解析类型为A记录,则值为一个IP地址
            if not is_ip_avaliable(self.value):
                raise DNSPodApiException("解析值输入错误.如果解析为A记录,则值必须为IP地址,请重新输入")
            else:
                self.value = self.value
        else:
            self.value = self.value

        # 判断ttl
        if not self.ttl:
            self.ttl = 600
        elif str(self.ttl).isdigit():
            self.ttl = int(self.ttl)
        else:
            raise DNSPodApiException("ttl输入错误.ttl必须为数字,请重新输入")

        # 判断mx优先级
        if not self.mx:
            self.mx = None

        elif not str(self.mx).isdigit():
            raise DNSPodApiException("mx输入错误.mx必须为1-20范围内数字,请重新输入")

        elif self.mx < 1 or self.mx > 20:
            raise DNSPodApiException("mx输入错误.mx必须为1-20范围内数字,请重新输入")
        else:
            self.mx = int(self.mx)


        # 拼接参数.创建和修改DNS记录解析会用到
        self.params = dict(domain=self.domain,sub_domain=self.sub_domain,record_line=self.record_line,record_type=self.record_type, value=self.value, ttl=self.ttl, mx=self.mx)


    def get_paras(self,paras=None):
        '''
        组装参数
        :return:
        '''
        parameter_info = {}
        # # 获取域名
        # domain = input("请输入要配置的域名:>>>").strip()

        # 获取子域名(sub_domain)
        if not self.sub_domain:
            self.sub_domain = input("请输入DNS解析子域名名称(域名前缀):>>>").strip()

        # 如果不传入参数,说明只需读取列表,此时只需要域名和子域名前缀即可
        if not paras:
            return self.sub_domain
            # parameter_info = dict(domain=domain,sub_domain=sub_domain)

        # 如果是添加或者修改一条记录
        else:
            self.record_type = input("请输入你要配置的解析类型.有A记录,CNAME记录,TXT记录等,回车默认为A记录:>>>").strip()
            self.value = input("请输入DNS解析记录值:>>>").strip()
            self.ttl = input("请输入TTL的缓存时间.要求为数字,免费版最低ttl为600,企业基础版最低为10,回车默认为600:>>>").strip()
            self.mx = input("请输入域名解析的优先级,回车默认为None,如果指定优先级则必须为1-20范围区间:>>>").strip()

            # 验证参数格式
            self.auth_paras()


    def get_record_id(self):
        '''
        获取record_Id
        :return:
        '''
        # 清空sub_domain和self.params的信息
        self.sub_domain = None


        # 检查子域名的解析记录是否已经存在,并且拿到self.sub_domain_record_list
        self.check_record()

        # 判断解析记录条目.
        if not self.sub_domain_record_list:
            # 如果没有个子域名的解析记录,则提醒返回
            print("当前域名下没有改子域名:{}的dns解析记录".format(self.sub_domain))
            return
        elif len(self.sub_domain_record_list) == 1:
            # 如果只有一条记录,则提示是否需要修改
            choise = input("是否确认需要修改? yes or no:>>>").strip()

            if choise.isalpha() and choise.upper() == "YES":
                choise = 0
            else:
                choise = None
                print("修改操作未完成,返回主界面")

        else:
            while True:
                choise = input("请选择需要修改哪条DNS解析记录.按q退出:>>>").strip()

                if choise.upper() == "Q":
                     choise = None
                     break
                elif not choise.isdigit():
                    print("请您输入数字")

                elif int(choise) > len(self.sub_domain_record_list) or int(choise) < 0:
                    print("您的选择超出了范围")

                else:
                    choise = int(choise)
                    break

        # 获取record_id
        if choise is not None:
            self.record_id = self.sub_domain_record_list[choise].get("record_id")
        else:
            self.record_id = None
    
    def check_record(self):

        # 获取用户输入的子域名
        self.sub_domain = self.get_paras()

        # 检查是否存在子域名的解析记录
        self.is_record_exists()
        if self.sub_domain_record_list:
            print("以下是该子域名:{},DNS解析记录部分信息:".format(self.sub_domain), sep="\n")
            for index,item in enumerate(self.sub_domain_record_list):
                print(index,":",item)

    def check_domain(f):
        '''
        检查域名是否存在,以及获取域名id.所有工作的前提准备工作
        :return:
        '''
        def inner(self,*args,**kwargs):
            # 判断是否存在域名,如果不存在,则输入
            if not self.domain:
                # 获取域名
                self.domain = input("请输入要配置的域名:>>>").strip()
                # 检查域名是否存在,如果不存在直接报错,不管后面要进行什么操作.如果存在,则会获取域名的Id:domain_id
                self.is_domain_avaliable()
            f(self,*args,**kwargs)
        return inner
    
    @check_domain
    def list_info(self):
        '''
        获取.并且打印域名下的某个子域名解析记录信息
        :return:
        '''
        # 清空sub_domain的信息
        self.sub_domain = None

        self.check_record()
        if not self.sub_domain_record_list:
            print("当前子域名:{}的DNS解析记录不存在!".format(self.sub_domain))

    @check_domain
    def create(self):
        '''
         创建一条解析记录.有两种情况:
            1.解析记录是否已经存在?
            2.是否添加多条同子域名的解析记录.(免费版最多2个,企业基础版10个)

            提供必要的参数: 域名(或者域名id),解析值,解析类型,解析线路.
            可选参数: 解析记录状态,ttl缓存时间,mx优先级,解析名
        :return:
        '''
        # 清空sub_domain的信息和self.params的信息
        self.sub_domain = None
        self.params = []

        # 检查子域名的解析记录是否已经存在,并且拿到self.sub_domain_record_list
        self.check_record()

        # 如果子域名解析记录存在,则询问是否需要继续添加
        if self.sub_domain_record_list:
            while True:
                ack = input("当前已经存在以上解析记录,是否仍然需要继续添加{}的解析记录.yes or no:>>>".format(self.sub_domain)).strip()
                if ack.upper() == "YES":
                    break
                else:
                    return

        # 如果不存在,直接添加

        # 获取多个参数.
        self.get_paras(paras="create")

        #创建DNS解析记录
        self.record_create()

    @check_domain
    def modify(self):
        '''
        修改一条DNS记录.
        有两种情况:
            1.解析记录是否已经存在?.如果不存在直接返回
            2.是否添加多条同子域名的解析记录.如果存在多个,要修改哪个?

        相比创建DNS记录解析,多了一个必选参数:record_id.当存在多个解析记录时,需要指定要修改的解析记录
            提供必要的参数: 域名(或者域名id),解析记录id,解析值,解析类型,解析线路.
            可选参数: 解析记录状态,ttl缓存时间,mx优先级,解析名
        :return:
        '''
        #获取record_id
        self.get_record_id()

        # 拿到解析记录的record_id
        if self.record_id:
            # 获取多个参数.
            self.params = []
            self.get_paras(paras="modify")
            # 加上record_id参数
            self.params.update(dict(record_id=self.record_id))

            #发起请求
            self.record_modify()
        else:
            print("子域名{}解析记录,并不存在.请您重新检查".format(self.sub_domain))

    @check_domain
    def change_status(self):
        '''
        开启或者关闭一条解析记录
        必选参数:
        domain,record_id,status:{enable|disable}
        :return:
        '''
        # 获取record_id
        self.get_record_id()
        if self.record_id:
            # 获取参数
            status = input("请输入enable或者disable:>>>").strip()
            if status.lower() == "enable" or status.lower() == "disable":
                self.status = status.lower()
            else:
                print("输入错误.DNS解析记录修改失败")
                return
        else:
            print("子域名{}解析记录,并不存在.请您重新检查".format(self.sub_domain))
            return

        # 拼接参数
        self.params = dict(domain=self.domain,record_id=self.record_id,status=self.status)

        #发起调用
        self.record_status()

    @check_domain
    def delete(self):
        '''
        删除一条解析记录,需要先判断该解析记录是否存在,以及是否有多个解析记录存在
        提供必要的参数: 域名(或者域名id),解析记录的Id
        :return:
        '''
        # 获取record_id
        self.get_record_id()

        if self.record_id:
            # 确认是否删除该条记录.!!!
            while True:
                ack = input("确认是否删除该条记录,删除后不可恢复!.yes or no:>>>").strip()
                if ack.upper() == "YES":
                    # 拼接参数
                    self.params = dict(domain=self.domain, record_id=self.record_id)

                    # 发起调用
                    self.record_remove()
                    break

                elif ack.upper() == "NO":
                    print("删除操作终止,返回主菜单")
                    return

                else:
                    print("输入有误,请重新输入")
        else:
            print("子域名{}解析记录,并不存在.请您重新检查".format(self.sub_domain))


    def run(self):
        print("DNS域名解析视图：")
        while True:
            print("=" * 50,sep="\n")
            print("1.创建解析记录\n"
                  "2.修改解析记录的值\n"
                  "3.删除解析记录\n"
                  "4.设置解析记录状态\n"
                  "5.查看DNS解析记录信息\n"
                  "0.退出\n")
            print("=" * 50,sep="\n")

            res = input("输入序号：").strip()

            if res == "1":
                self.create()
            elif res ==  "2":
                self.modify()
            elif res == "3":
                self.delete()
            elif res == "4":
                self.change_status()
            elif res == "5":
                self.list_info()
            elif res == "0":
                print("退出成功！")
                break
            else:
                print("请选择正确的编号")


if __name__ == "__main__":
    dns_record = HandleRecord()
    dns_record.run()