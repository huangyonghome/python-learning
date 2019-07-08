#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/5 下午6:09
# @Author  : jesse
# @File    : python.06特殊成员方法.py

# ########## __doc__方法查看描述信息
#
# class Foo:
#     '''
#     这是一个类,里面什么都没有
#     '''
#     def __init__(self):
#         pass
#
# print(Foo.__doc__)
#
#
#
# ########__module__查看当前操作对象位于哪个模块
#
# from my_module import Foo
#
# print(Foo.__module__)
#
#
#
# #######查看对象的类:__class__
#
# class Foo:
#     def __init__(self):
#         pass
#
# a = Foo()
# print(a.__class__)
# print(type(a))
# print(type(Foo))
#
# ######### __dict__ 查看类或对象中的所有成员
#
# class Person:
#     __country = 'China'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def func(self):
#         print('func')
#
# print("打印类成员".center(30,'-'))
# # print(Person.__dict__)
# for i in Person.__dict__:
#     print('{}:{}'.format(i,Person.__dict__[i]))
#
# p = Person('jesse',22)
# print("打印对象成员".center(30,'-'))
# for i in p.__dict__:
#     print('{}:{}'.format(i,p.__dict__[i]))

##__call__
#构造方法的执行是由创建对象触发的 , 而对于\_\_call\_\_ 方法的执行是由对象后加括号触发的

# class A:
#     def __init__(self):
#         print("执行init")
#
#     def __call__(self, *args, **kwargs):
#         print("执行call")
#
# a = A()
# a()

## \_\_str\_\_  \  \_\_repr\_\_  🍀

#改变对象的字符串显示 , 这两个方法都只能返回字符串

class A:
    def __init__(self,name):
        self.name = name
    def __str__(self):
        return self.name
    # def __repr__(self):
    #     return ("I am repr:%s" %self.name)


class B:
    def __init__(self,classA):
        self.name = classA


a = A('jesse')
print(a)
print(a.name)

b = B(a)
print(b.name)




# print(str(a))
# print(repr(a))



#
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def __hash__(self):
#         return hash(self.name)
#     def __eq__(self, other):
#         if self.name == other.name:
#             return True
#
# p_lst = []
# for i in range(84):
#     p_lst.append(Person('Lyon', i))
# print(p_lst)
# print(set(p_lst))


# __new__ __init__

# __new__ 方法负责实例化一个对象. __init__方法负责初始化一个对象

# 例子:

# class A:
#     def __init__(self):
#         self.x = 1
#         print("执行了init方法")
#
#     def __new__(cls, *args, **kwargs):
#         print("执行了new方法")
#
#
# 因为我们重写了__new__方法.所以并没有成功创建a对象
# 虽然A实例化了一个对象a.但是实际上a并没有成功实例化,a的值为None.而且实例化对象的时候也没有执行init初始化方法
# a = A()
# print(a)
# print(a.x) #打印报错,没有x属性
#
#
# #重写__new__方法
#
# class A:
#     def __init__(self):
#         self.x = 1
#         print("执行了init方法")
#
#     def __new__(cls, *args, **kwargs):
#         #return super().__new__(cls)  #调用父类(object类)的__new__方法
#         #也可以写成:
#         return object.__new__(cls)
#         print("执行了new方法")
#
#
# a = A()
# print(a)
# print(a.x)

## item  🍀

# \_\_getitem\_\_ , \_\_setitem\_\_ , \_\_delitem\_\_  用于索引操作 , 如字典 , 以上分别表示获取 , 设置 , 删除数据

# class A:
#     def __init__(self,name):
#         self.name = name
#
#     def __getitem__(self, item): #将'name'作为参数传递给item
#         print("执行了getitem方法")
#         # print(item)
#         # print(self.__dict__[item]) #打印item的值
#         print(getattr(self, item))  # 通过反射也可以获得name的值
#
#     def __setitem__(self, key, value):
#         print("执行了setitem方法")
#         print(key,value)
#         # self.key = value
#         self.__dict__[key] = value
#         print(self[key])
#
#     def __delitem__(self, key):
#         print("执行了delitem方法")
#         self.__dict__.pop(key)
#
#
#
#
# a = A('jesse')
# a['name'] #执行getitem方法
#
# a['name'] = 'lyon' #执行setitem方法.修改name的值
# print(a.name)
#
# a['age'] = 25  #执行setitem方法,添加个age属性
# print(a.__dict__)
#
# del a['name']
# print(a.__dict__) #执行delitem方法.删除name属性


#__getattr__ 和 __getattribute__

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def __getattr__(self, item):
#         return "Attribute %s fetch failure" %item
#
#     def __getattribute__(self, item):
#         if item == 'name':
#             return 'jesse'
#         else:
#             return 'error'
#
# x = Foo('jesse')
# print(x.name)
# print(x.age)


#__setattr__

# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def __setattr__(self, key, value):
#         if key == 'name':
#             self.__dict__[key] = value
#         else:
#             raise AttributeError(key + ' not allowed')
#
# x = Foo('jesse')
# x.name = "Lyon"
# # x.age = 10
# print(x.__dict__)
#

