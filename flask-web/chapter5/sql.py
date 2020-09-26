# -*- coding: utf-8 -*-
# @Time    : 2020-09-26 17:28
# @Author  : jesse
# @File    : sql.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint
from sqlalchemy.orm import sessionmaker

#创建引擎
engine = create_engine('mysql+pymysql://root:Iamyourdaddy@172.16.20.1:3306/test',
                        encoding='utf-8')

#声明基类

Base = declarative_base()

Session_class = sessionmaker(bind=sql.engine) #绑定数据库引擎

Session = Session_class() #实例化数据库会话



class Role(Base):
    __tablename__ = 'roles'
    id = Column(Integer,primary_key=True)
    name = Column(String(64),unique=True)

    def __repr__(self):
        return '<Role %r>' %self.name


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer,primary_key=True)
    username = Column(String(64),unique=True,index=True)
    role_id = Column(Integer)

    def __repr__(self):
        return '<User %r>' %self.username




if __name__ == '__main__':
    Base.metadata.create_all(engine)  # 创建表结构