#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/27 上午11:45
# @Author  : jesse
# @File    : python.01类的初识.py


#类的格式


#class 类名:
#    pass

#举个例子

# #创建一个类
# class Person():
#     #构造函数,初始化属性.__init__方法的代码会在实例化对象的时候自动执行
#     def __init__(self,name):
#         print("i am init attribution")
#         self.name = name
#
#     #动态方法
#
#     def eat(self):
#         print("I am eating")
#
#
# #实例化一个对象
# p = Person('jesse')
# #查看对象的静态属性
# print(p.name)
#
# #执行对象的动态方法.
# p.eat()
#
# #查看类或对象成员,返回一个字典
# print(Person.__dict__)
# print(p.__dict__)


#__init__构造函数

# class Foo():
#     def __init__(self,name):
#         self.name = name
#
#     def func(self):
#         print(id(self))
#
#
# a = Foo('jesse')
# print(id(a))
# a.func()
#
# #不同的对象,内存地址不同
# b = Foo('jerry')
# print(id(b))
# b.func()

#属性的继承

# class A():
#     '''
#     这是一个类,这个注释通过__doc__属性可以查看到
#     '''
#     pass
#
# a = A()
#
# #a这个对象并没有__doc__属性的,他继承了A类的属性.
# print(a.__doc__)

# class Foo:
#     name = ['jesse']
#
# a = Foo()
# b = Foo()
#
# #查看实例属性
# print('实例a的name:',a.name)
# print('实例b的name:',b.name)
#
# #查看内存地址
# print(id(a.name))
# print(id(b.name))
# print(id(Foo.name))
#
# Foo.name = 'Lyon'
#
# #再次查看属性
# print('实例a的name:',a.name)
# print('实例b的name:',b.name)
#
# a.name = ['Jesse']
#
# print('实例a的name:',a.name)
# print('实例b的name:',b.name)
#
# #再次查看内存地址
# print(id(a.name))
# print(id(b.name))
# print(id(Foo.name))


#类的方法是所有实例共享的

# class Foo:
# #     def func(self):
# #         pass
# #
# # a = Foo()
# # b = Foo()
# #
# # print(a.func)
# # print(b.func)
# #
# # print(hex(id(a))) #a.func和a对象本身的内存地址一样.说明func绑定到了a
# # print(hex(id(b))) #a.func和b.func内存地址不一样.不同的实例,有不同的内存空间

# #对象交互
#
# class Foo:
#     def __init__(self,name):
#         self.name = name
#
#     def attack(self,per):
#         print("{} attack {}".format(self.name,per.name))
#
#
# jesse = Foo('jesse')
# Jerry = Foo('jerry')
#
# jesse.attack(Jerry)

#类的组合

#传参组合

# class Birthday:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# class Person:
#     def __init__(self,name,birthdate):
#         self.name = name
#         self.birthdate = birthdate
#
#
# p = Person('jesse',Birthday('1985','5','01'))
#
# print (p.name)
# print(p.birthdate.year)
#
# #定义组合
#
# class Birthday:
#     def __init__(self,year,month,day):
#         self.year = year
#         self.month = month
#         self.day = day
#
# class Person:
#     def __init__(self,name,year,month,day):
#         self.name = name
#         self.birthdate = Birthday(year,month,day)
#
#
# p = Person('jesse','1985','5','01')
#
# print (p.name)
# print(p.birthdate.year)

# class Game_role:
#     def __init__(self,name,sex,attack,hp):
#         self.name = name
#         self.sex = sex
#         self.attack = attack
#         self.hp = hp
#
#     def fight(self,role):
#         rest = role.hp - self.attack
#         print("{} attack {}, 伤害{},对方还剩余{}血量".format(self.name,role.name,self.attack,rest))
#
#
# p1 = Game_role('jesse','male',20,500)
# p2 = Game_role('jerry','male',10,500)
#
# p1.fight(p2)


# class Person():
#     name = 'Lyon'
#     def __init__(self,name1):
#         self.name = name1
#
#     def eat(self):
#         print("%s is eatting" %self.name)
#
#
# p = Person('jesse')
#
# print(p.name)
# print(Person.name)
# print(Person.__dict__)
# print(Person.__name__)
# print(p.__dict__)
#
# class Foo():
#     name = ['lyon']
#
# a = Foo()
# b = Foo()
#
# print("实例a中的name属性:",a.name)
# print("实例b中的name属性:",b.name)
#
# print(id(a.name))
# print(id(b.name))
# print(id(Foo.name))
#
# Foo.name = ['jesse']
#
# print("实例a中的name属性:",a.name)
# print("实例b中的name属性:",b.name)
#
# print(id(a.name))
# print(id(b.name))
# print(id(Foo.name))
#
# a.name = ['jerry']
#
# print("实例a中的name属性:",a.name)
# print("实例b中的name属性:",b.name)
#
# print(id(a.name))
# print(id(b.name))
# print(id(Foo.name))

class Animal():
    def eat(self):
        print("eating")


class cat():
    def eat1(animal):
        print("%s is eating" % animal)

    def eat(self):
        print("cat is eating")


def eat(obj):
    obj.eat()

Animal.eat(Animal)
cat.eat1(Animal.__name__)
eat(Animal())
eat(cat())