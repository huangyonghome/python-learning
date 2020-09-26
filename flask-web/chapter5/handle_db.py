# -*- coding: utf-8 -*-
# @Time    : 2020-09-26 17:45
# @Author  : jesse
# @File    : handle_db.py

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Index, UniqueConstraint
from sqlalchemy.orm import sessionmaker

import sql

Session_class = sessionmaker(bind=sql.engine) #绑定数据库引擎

Session = Session_class() #实例化数据库会话

def Insert(data):

    Session.add(data)
    Session.commit()
    Session.close()

