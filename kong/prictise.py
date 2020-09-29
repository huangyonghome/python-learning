#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 下午5:04
# @Author  : jesse
# @File    : prictise.py

import configparser
import json
import requests
import sys

config = configparser.ConfigParser()
config.read('config.ini')


# 测试kong集群的链接是否正常
def connect_kong(url):
    res = requests.get(url)
    if res.status_code != 200:
        raise ConnectionError('连接Kong网关错误')

# 查找某个service的id


def get_service(name):
    '''
    :param name: 一个service名称
    :return: 如果有该service则返回service的id,否则返回None
    '''
    res = requests.get(url + 'services')
    response = json.loads(res.text)
    data = response.get('data')
    for item in data:
        # print(item)
        if item.get('name') == name:
            return item.get('id')
    else:
        return None

# 查找某个route路由的id


def get_route(route_name):
    '''
    :param route_name: route路由名称
    :return: 如果存在该route路由,则返回路由的id,否则返回None
    '''
    res = requests.get(url + 'routes')
    response = json.loads(res.text)
    data = response.get('data')
    for item in data:
        if item.get('name') == route_name:
            return item.get('id')
    else:
        return None


# 配置Kong的Service
def post_kong(data):
    '''

    :param data: data参数是一个字典格式的数据
    :return: 如果提交成功返回的代码是201,否则会返回具体错误,比如400,字段错误 409,有重复的Service等
    '''
    res = requests.post(url + 'services', data=data)
    if res.status_code == 201:
        error = None
    else:
        error = res.text
    return error

# 配置Kong的routes路由


def post_routes(data):
    '''
    :param data: data参数是一个字典格式的数据
    :return: 如果提交成功返回的代码是201,否则会返回具体错误,比如400,字段错误 409,有重复的routes等
    '''
    res = requests.post(url + 'routes', data=data)

    if res.status_code == 201:
        error = None
    else:
        error = res.text
    return error

# 配置Kong的插件


def post_plugins(plugins_url, data):
    '''

    :param plugins_url: 插件URL,因为插件可能配置在routes或者配置在Service中,所以提交URL地址还不一样
    :param data:  data参数是一个字典格式的数据
    :return:  如果提交成功返回的代码是201,否则会返回具体错误,比如400,字段错误 409等
    '''
    res = requests.post(plugins_url, data=data)
    if res.status_code == 201:
        error = None
    else:
        error = res.text
    return error


if __name__ == "__main__":
    env = input("请输入你要配置的Kong的环境名称,例如:dev,beta,prod:>>>").strip()
    base = config['default']
    url = base.get(env + '_url')  # 拼接Kong不同环境的url地址
    if not url:
        print("请输出正确的环境名称")

    # 测试是否正常连接kongx
    connect_kong(url)

    # 检查是否定义了service配置项
    service = config['service']
    if service:
        # 迭代service配置项中的每个key
        for key in service:
            # 获取key中的字典,由于配置文件中提取出来的是字符串形式,所以需要用json转换成字典格式
            service_dic = json.loads(config['service'].get(key))

            # 获取service名
            service_name = service_dic.get('name')
            if not service_name:
                raise KeyError("service配置项{}不存在name属性".format(key))

            # 检查是否已经配置了该service.如果service不存在,则直接创建,否则提示是否配置有误.
            service_id = get_service(service_name)
            if not service_id:
                print("正在创建service:{}".format(service_name))
                res = post_kong(service_dic)  # 调用post_kong函数创建service
                if not res:
                    print("service:{}创建成功".format(service_name))
                else:
                    print("service:{}创建失败:{}".format(service_name, res))

            # 如果service已经存在,并且用户确认无误,则继续创建后面的routes路由,否则终止程序
            else:
                print("当前已经存在一个同名的service:{}".format(service_name))

                while True:
                    info = input("是否确认将routes添加到这个Service?.yes/no:>>>").strip()
                    if info == "no" or info == "NO":
                        print("程序退出")
                        sys.exit()

                    elif info == "yes" or info == "YES":
                        print("service:{}已经存在,不再创建该service".format(service_name))
                        break
                    else:
                        print("输入错误,请重新输入!")

    # 检查是否存在routes配置项
    routes = config['routes']
    if routes:
        # 迭代routes配置项下的每个key
        for key in routes:

            # 获取key的内容,configparse模块提取出来的是字符串形式,使用json转换成字典格式
            route_dic = json.loads(config['routes'].get(key))

            # 获取data数据(稍后需要将data数据通过Post提交给Kong)
            route_data = route_dic.get('data')

            # 获取service名
            service_name = route_dic.get('service_name')

            if not service_name:
                raise KeyError("routes配置项{},缺少service_name属性".format(key))

            # 获取routes路由名
            routes_name = route_data.get('name')

            # 获取service的id,由于routes路由需要绑定到service下,所以需要检查该service是否已经存在
            service_id = get_service(service_name)
            if not service_id:
                print("没有找到service:{}服务,路由{}添加失败,程序退出".format(
                    service_name, routes_name))
                sys.exit()

            # 在data数据中添加service.id,在配置routes路由时,需要绑定具体service的id
            route_data['service.id'] = service_id
            print("开始创建routes:{}".format(routes_name))

            # 调用post_routes函数,传入route_data字典,配置routes
            res = post_routes(route_data)
            if not res:
                print("routes路由{}创建成功".format(routes_name))
            else:
                print("routes路由{}创建失败:{}".format(routes_name, res))

    # 检查是否存在plugins配置项
    plugins = config['plugins']
    if plugins:

        # 迭代plugins配置项下的key
        for key in plugins:
            plugins_dic = json.loads(config['plugins'].get(key))
            plugins_data = plugins_dic.get('data')

            # 由于plugins插件可以关联到一个route路由,或者关联到整个service.所以plugin配置文件中可能同时存在service或者routes名
            service_name = plugins_dic.get('service_name')
            route_name = plugins_dic.get('route_name')

            # 检查配置文件,确定是否定义需要配置的插件名称
            plugins_name = plugins_data.get('name')
            if not plugins_name:
                raise AttributeError("plugins必须指定插件名")

            # 如果没有配置service名称或者routes名称,那么Plugin插件无法绑定到对象中
            if not route_name and not service_name:
                raise AttributeError(
                    "plugin插件:{},必须指定配置在某个Service或者routes下".format(plugins_name))

            # 如果有配置routes路由名,则关联到routes路由中
            elif route_name:

                # 判断该routes路由是否存在
                route_name_id = get_route(route_name)
                if not route_name_id:
                    raise NameError("plugins插件:{},配置的route路由:{}不存在!".format(
                        plugins_name, route_name))
                else:
                    # 拼接插件的url.
                    plugins_url = url + 'routes/' + route_name_id + '/plugins'

                    # 调用post_plugins函数,配置Kong插件,关联到routes中
                    res = post_plugins(plugins_url, plugins_data)
                    if not res:
                        print("plugins:{}创建成功.绑定在route路由:{}中".format(
                            plugins_name, route_name))
                    else:
                        print("plugins:{}创建失败:{}".format(plugins_name, res))

            # 如果只配置了service名称,则将插件配置到service下
            else:

                # 查看service是否存在
                service_id = get_service(service_name)
                if not service_id:
                    raise NameError("plugins插件:{},配置的Service:{}不存在!".format(
                        plugins_name, service_name))
                else:

                    # 拼接插件url
                    plugins_url = url + 'services/' + service_id + '/plugins'

                    # 调用post_plugins函数,配置Kong插件,关联到service中
                    res = post_plugins(plugins_url, plugins_data)
                    if not res:
                        print("plugins:{}创建成功.绑定在service:{}中".format(
                            plugins_name, service_name))
                    else:
                        print("plugins:{}创建失败:{}".format(plugins_name, res))
