# -*- coding: utf-8 -*-
# @Time    : 2019-06-07 10:29
# @Author  : jesse
# @File    : 练习题.py

# class StarkConfig:
#     def __init__(self, num):
#         self.num = num
#
#     def run(self):
#         self()
#
#     def __call__(self, *args, **kwargs):
#         print(self.num)
#
#
# class RoleConfig(StarkConfig):
#     def __call__(self, *args, **kwargs):
#         print(345)
#
#     def __getitem__(self, item):
#         return self.__dict__[item]
#
# v1 = RoleConfig('alex')
# v2 = StarkConfig('太白金星')
# # print(v1[1])
# # print(v2[2])
# v1.run()
# print(v1.num)
# print(v1['num'])

#-------


# class UserInfo:
#     pass
#
#
# class Department:
#     pass
#
#
# class StarkConfig:
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite:
#
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v
#
#
# site = AdminSite()
# site.register(UserInfo, StarkConfig)
# # 1
# # obj = site._registry[UserInfo]()
#
# # 2
# obj = site._registry[UserInfo](100)
# obj.run()
#
# -------
#
#
# class UserInfo:
#     pass
#
#
# class Department:
#     pass
#
#
# class StarkConfig:
#     def __init__(self, num):
#         self.num = num
#
#     def changelist(self, request):
#         print(self.num, request)
#
#     def run(self):
#         self.changelist(999)
#
#
# class RoleConfig(StarkConfig):
#     def changelist(self, request):
#         print(666, self.num)
#
#
# class AdminSite:
#
#     def __init__(self):
#         self._registry = {}
#
#     def register(self, k, v):
#         self._registry[k] = v(k)
#
#
# site = AdminSite()
# site.register(UserInfo, StarkConfig)
# site.register(Department, RoleConfig)
#
# for k, row in site._registry.items():
#     print(k,row)
#     row.run()



#-------

#
# class A:
#     list_display = []
#
#     def get_list(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
# s1 = A()
# print(s1.get_list())

# -------
#
#
# class A:
#     list_display = [1, 2, 3]
#
#     def __init__(self):
#         self.list_display = []
#
#     def get_list(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
# s1 = A()
# print(s1.get_list())
#
# ------
#

# class A:
#     list_display = []
#
#     def get_list(self):
#         self.list_display.insert(0, 33)
#         return self.list_display
#
#
# class B(A):
#     list_display = [11, 22]
#
#
# s1 = A()
# s2 = B()
# print(s1.get_list())
# print(s2.get_list())