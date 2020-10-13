#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 下午2:49
# @Author  : jesse
# @File    : csv_import_mysql.py


import csv
from collections import namedtuple
from sqlalchemy.ext.declarative import declarative_base

import create_db

# 每行读取csv文件.使用yield生成器每次返回一行数据.
def get_data(file_name):
    #读取csv文件
    with open(file_name,encoding='utf-8-sig') as f:
        f_csv = csv.reader(f)

        #先读取csv文件的一行标题
        headers = next(f_csv)

        # #定义一个命名元祖
        # Row = namedtuple('Row', headers)

        for line in f_csv:
            #以元祖形式生成csv文件内容的每行数据
            # yield Row(*line)
            t = {header: data for header,data in zip(headers,line)}
            # print(type(t))
            # print(t)
            yield  t




if __name__ == '__main__':
    # 创建引擎
    engine, session, Base = create_db.get_conn(username='root', password='Iamyourdaddy', host='172.16.20.1',
                                               port='3306', database='csvdb')

    # 创建数据库
    table_name = create_db.create_table(Base, engine)

    # 从csv文件拿数据

    for t in get_data('sql.csv'):
        # print(**t)
        # pass
        # 从csv文件中读取每行,并且插入数据
        # 插入表数据..传入数据表类名,engine,session,以及插入的数据.由于csv文件的每行数据是一个命名元祖,
        # 所以可以用命名元祖的静态方法取值
        # create_db.insert(table_name,engine,session,name=t.username,age=t.age,deptname=t.deptname)
        create_db.insert(table_name,engine,session,t)



