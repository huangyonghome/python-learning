#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 下午3:02
# @Author  : jesse
# @File    : create_db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint
from sqlalchemy.orm import sessionmaker


def get_conn(**kwargs):
    username = kwargs.get('username')
    password = kwargs.get('password')
    host = kwargs.get('host')
    port = kwargs.get('port','3306')
    database = kwargs.get('database')

    #创建引擎
    engine = create_engine('mysql+pymysql://{0}:{1}@{2}:{3}/{4}'
                           .format(username,password,host,port,database),encoding='utf-8')

    # 声明基类
    Base = declarative_base()

    DBSession = sessionmaker(bind=engine)
    session = DBSession()

    return engine,session,Base


def create_table(Base,engine):

    class Employee(Base):
        #表名
        __tablename__ = 'employee'

        #设置列
        id = Column(Integer,primary_key=True,autoincrement=True) #id列 int类型
        username = Column(String(32))  #用户名列,char类型
        age = Column(Integer) #年龄列
        deptname = Column(String(32)) #部门列

        #表参数,一般是设置为索引
        __table_args__ = (

            #创建一个所需,名字是ix_name
            Index('ix_name','username'),
        )

        #类返回格式
        def __repr__(self):
            return "<User(id='%s',username='%s')>" %(self.id,self.username)
    #创建表
    Base.metadata.create_all(engine)
    return Employee


def insert(class_name,engine,session,data):
    # print(**data)
    insert_data = class_name(**data)
    session.add(insert_data)
    session.commit()
    session.close()


