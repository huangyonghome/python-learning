# -*- coding: utf-8 -*-
# @Time    : 2020-06-14 10:28
# @Author  : jesse
# @File    : practise1.py

# class Foo:
#     @property
#     def AAA(self):
#         print("执行了get方法")
#
#     @AAA.setter
#     def AAA(self,value):
#         print("执行了set方法")
#
#     @AAA.deleter
#     def AAA(self):
#         print("执行了delete方法")
#
#
# f = Foo()
#
# f.AAA
# f.AAA = 'jesse'
# del f.AAA
#
# class Goods:
#     def __init__(self):
#         self.original_price = 100
#         self.discount = 0.8
#
#     @property
#     def price(self):
#         prices = self.original_price * self.discount
#         return prices
#
#     # def get_price(self):
#     #     print(self.prices)
#
#     @price.setter
#     def price(self,original_price):
#         self.original_price = original_price
#
#     @price.deleter
#     def price(self):
#         del self.original_price
#
#
# p = Goods()
# # p.price
# # print(p.prices)
# p.price = 200
# p.price
# print(p.price)
# del p.price
# p.price

# p.get_price()


#静态方法

# class Person:
#     country = 'china'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @staticmethod
#     def search(self):
#         print("我是静态方法")
#         print(self)
#         print(self.name,self.age)
#
# p = Person('jesse','22')
# print(p)
# p.search(p)
# Person.search(p)

# class Foo:
#     def __new__(cls):
#         pass
#
# a = Foo()
#
# class A:
#     def __str__(self):
#         return "i am str"
#
# a = A()
# print(str(a))
# print(repr(a))



