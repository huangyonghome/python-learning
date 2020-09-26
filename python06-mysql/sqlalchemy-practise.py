# -*- coding: utf-8 -*-
# @Time    : 2020-09-26 9:32
# @Author  : jesse
# @File    : sqlalchemy-practise.py

# coding:utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DATE, ForeignKey  # 导入外键
from sqlalchemy.orm import relationship,sessionmaker # 创建关系

engine = create_engine("mysql+pymysql://root:Iamyourdaddy@172.16.20.1:3306/test",
                       encoding="utf-8")

Base = declarative_base()  # 生成orm基类


class Company(Base):
    __tablename__ = "company"

    name = Column(String(20), primary_key=True)
    location = Column(String(20))

    def __repr__(self):
        return "name:{0} location:{1}".format(self.name, self.location)


class Phone(Base):
    __tablename__ = "phone"

    id = Column(Integer, primary_key=True)
    model = Column(String(32))
    price = Column(String(32))
    company_name = Column(String(32), ForeignKey("company.name"))
    company = relationship("Company", backref="phone_of_company")

    def __repr__(self):
        return "{0} model:{1},price:{2}".format(self.id, self.model, self.price)


Base.metadata.create_all(engine)  # 创建表

Base = declarative_base()

DBSession = sessionmaker(bind=engine)
session = DBSession()





# companys = {
#     "Apple": "Amercian",
#     "Xiaomi": "China",
#     "Huawei": "China",
#     "Sungsum": "Korea",
#     "Nokia": "Finland"
# }
# phones = (
#     [1, "iphoneX", "Apple", 8400],
#     [2, "xiaomi2s", "Xiaomi", 3299],
#     [3, "Huaweimate10", "Huawei", 3399],
#     [4, "SungsumS8", "SungSum", 4099],
#     [5, "NokiaLumia", "Nokia", 2399],
#     [6, "iphone4s", "Apple", 3800]
# )
#
# for key in companys:
#     new_company = Company(name=key, location=companys[key])
#     session.add(new_company)
#     session.commit()
#
# for phone in phones:
#     id = phone[0]
#     model = phone[1]
#     company_name = phone[2]
#     price = phone[3]
#
#     new_phone = Phone(id=id, model=model, company_name=company_name, price=price)
#     session.add(new_phone)
#     session.commit()
#
# session.close()

phone_obj = session.query(Phone).filter_by(id = 1).first()
print(phone_obj)
print(phone_obj.company.name)


#查询company表
company_obj = session.query(Company).filter_by(name = "Nokia").first()

#通过phone表关联的relationship的字段"backref="phone_of_company"",查询phone表数据
print(company_obj.phone_of_company)
print(company_obj.phone_of_company[0].id)
