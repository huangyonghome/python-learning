#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/11 下午8:17
# @Author  : jesse
# @File    : sqlalchemy.table.py

# -*- coding: utf-8 -*-
# @Time    : 2017-06-09 22:10
# @Author  : jesse
# @File    : sqlalchemy_class.py

'''创建一个创建表的模块.演示多外键关联'''

import sqlalchemy
from sqlalchemy import create_engine,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date

from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("mysql+pymysql://root:Iamyourdaddy@172.16.20.1:3306/db1?charset=utf8") #连接数据库.charset字段表示支持中文

Base = declarative_base()

class Income(Base):
    __tablename__='income' #创建一个customer表
    id=Column(Integer,primary_key=True) #id字段,整形,主键
    incomes=Column(Integer) #name字段


class Address(Base): #定义一个Address类
    __tablename__='address'
    id = Column(Integer,primary_key=True)
    street = Column(String(255)) #街道地址
    city = Column(String(255)) #城市名

    def __repr__(self): #定义一个返回格式.为了将查询的数据打印出来更直观
        return "Address:%s %s" %(self.street,self.city)


if __name__ == '__main__':
    Base.metadata.create_all(engine) #创建表结构

    #创建session实例
    Session = sessionmaker(bind=engine)
    Session = Session()

    # income1 = Income(incomes=3000)
    # address1 = Address(street='QinZhouLu',city='ShangHai')
    # Session.add(income1)
    # Session.add(address1)
    #
    # Session.commit()
    #
    # Session.add_all(
    #     [Income(incomes=4000),
    #     Address(street='LingZhaoLu', city='ShangHai')]
    # )
    #
    # Session.commit()

    #删除数据
    #1.先用query查找类名
    #2.用filter将找到结果过滤,filter(指定where条件,类名.字段名 == 值)
    #3.将找到结果用delete()方法删除
    #4.commit提交
    Session.query(Income).filter(Income.incomes==3000).delete()
    Session.commit()

    