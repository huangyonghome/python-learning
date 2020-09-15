#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 下午5:04
# @Author  : jesse
# @File    : prictise.py

import configparser,json,requests,sys

config = configparser.ConfigParser()
config.read('config.ini')


def connect_kong(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise ConnectionError('连接Kong网关错误')




def post_kong(data):
    res = requests.post(url + 'services',data=data)
    if res.status_code == 201:
        error = None
    else:
        error = res.text
    return error

def get_service(host):
    res = requests.get(url + 'services')
    response = json.loads(res.text)
    data = response.get('data')
    for item in data:
        # print(item)
        if item.get('name') == host:
            return item.get('id')
    else:
        return None


def post_routes(data):
    res = requests.post(url + 'routes',data=data)

    if res.status_code == 201:
        error = None
    else:
        error = res.text
    return error


if __name__ == "__main__":
    # env = input("请输入你要配置的Kong的环境名称,例如:dev,beta,prod:>>>").strip()
    env = 'dev'
    base = config['default']
    url = base.get(env +'_url')
    if not url: print("请输出正确的环境名称")
    connect_kong(url)

    service = config['service']
    if service:
        for key in service:
            service_dic = json.loads(config['service'].get(key))
            # print(type(service_dic))
            # print(service_dic)
            # # print(service_dic)
            # # print(json.loads(service_dic))
            service_name = service_dic.get('name')
            if not service_name:
                raise KeyError("service配置项{}不存在name属性".format(key))
            service_id = get_service(service_name)
            if not service_id:
                print("正在创建service:{}".format(service_name))
                res = post_kong(service_dic)
                if not res:
                    print("service:{}创建成功".format(service_name))
                else:
                    print("service:{}创建失败:{}".format(service_name, res))

            else:
                print("当前已经存在一个同名的service:{}".format(service_name))

                while True:
                    info = input("是否确认将routes添加到这个Service?.yes/no:>>>").strip()
                    if info == "no" or info == "NO":
                        print("程序退出")
                        sys.exit()

                    elif info == "yes" or info == "YES":
                        print("Continue")
                        break
                    else:
                        print("输入错误,请重新输入!")


    routes = config['routes']
    print(routes)
    if routes:
        for key in routes:

            route_dic = json.loads(config['routes'].get(key))

            service_name = route_dic.get('service_name')
            routes_name = route_dic.get('name')
            if not service_name:
                raise KeyError("routes配置项{}service_name属性".format(key))
            service_id = get_service(service_name)
            if not service_id:
                print("没有找到service:{}服务,路由{}添加失败,程序退出".format(service_name,routes_name))
                sys.exit()
            del route_dic['service_name']
            route_dic['service.id'] = service_id
            print("开始创建routes:{}".format(routes_name))
            res = post_routes(route_dic)
            if not res:
                print("routes路由{}创建成功".format(routes_name))
            else:
                print("routes路由{}创建失败:{}".format(routes_name,res))



    # print(service)
    # for section in topsecret:
    #     if section == 'default':continue
    #     for item in config[section]:print(item)
            # for
            # service = config[section].get('service')
            # service_name = json.loads(service).get('name')
            # service_id = get_service(service_name)
            # if not service_id:
            #     print("正在创建service:{}".format(service_name))
            # else:
            #     print("当前已经存在一个同名的service:{}".format(service_name))
            #     info = input("是否确认将routes添加到这个Service?.yes/no:>>>").strip()
            #     if info == "yes" or info =="YES":


    # print(get_service('betaapi'))betaapi