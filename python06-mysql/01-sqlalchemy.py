# -*- coding: utf-8 -*-
# @Time    : 2020-07-11 17:22
# @Author  : jesse
# @File    : 01-sqlalchemy.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint
from sqlalchemy.orm import sessionmaker


#创建引擎
engine = create_engine('mysql+pymysql://root:Iamyourdaddy@172.16.20.1:3306/db1',encoding='utf-8'
                       )

#声明基类

Base = declarative_base()

#创建数据表的类,tablename是表名.所有类都基于Base类

class Interests(Base):
    #表名
    __tablename__ = 'interests'

    #设置列
    id = Column(Integer,primary_key=True,autoincrement=True) #id列 int类型
    name = Column(String(32))  #用户名列,char类型
    interest = Column(String(128)) #兴趣列,char类型

    #表参数,一般是设置为索引
    __table_args__ = (

        #创建一个所需,名字是ix_name
        Index('ix_name','name'),
    )

    #类返回格式

    # def __repr__(self):
    #     return "<User(id='%s',name='%s')>" %(self.id,self.name)


#创建表
# Base.metadata.create_all(engin)
DBSession = sessionmaker(bind=engine)
session = DBSession()


# run_interest = Interests(name="jesse",interest="run")
# session.add(run_interest)
# session.commit()
# session.close()

inte = session.query(Interests).filter(Interests.id==1).one()
print(type(inte))
print(inte.name,inte.interest)
session.close()
