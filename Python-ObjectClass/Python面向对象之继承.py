# -*- coding: utf-8 -*-
# @Time    : 2019-06-01 23:35
# @Author  : jesse
# @File    : Python面向对象之继承.py

#继承就是该类是基于父类(也称基类,超类)而来,继承的类通常称为子类或者派生类

#继承类的格式: class 类名(父类):

#下面是个例子

# class Animal:
#
#     #eat
#     def eat(self):
#         print("I am eating")
#
#     def sleep(self):
#         print("I am sleeping")
#
#
#
# #猫类继承动物类
#
# class Cat(Animal):
#     def catch_mouse(self):
#         print("I am catching")
#
#
# #狗继承动物类
#
# class Dog(Animal):
#     def jump_wall(self):
#         print("I am jumping")
#
#
#
#
# cat1 = Cat()
# dog1 = Dog()
# #实例都可以访问父类中的方法
#
# cat1.sleep()
# dog1.sleep()
#
# #但是不能访问其他实例对象的自己方法


#多继承
#
# class A:
#     def __init__(self):
#         pass
#
#     def display(self):
#         print("this is from A")
#
#
# class B(A):
#
#     def __init__(self):
#         pass
#
# class C(A):
#     def __init__(self):
#         pass
#
#     def display(self):
#         print("this is from C")
#
#
# #D类继承B和C2个父类
# class D(B,C):
#     def __init__(self):
#         pass
#
# #在python3中,默认是新类...当继承多个类的时候,默认会先从第一个类(B)查找相应方法或者属性..如果没有则去第二个类找(C)
# #在python2中,默认的是经典类.当继承多个类的时候,默认会先从第一个类(B)查找相应方法或者属性..如果没有则去B类的父类(A)查找
# obj = D()
# obj.display()

#派生

#继承是站在子类角度看的.,那么派生就是站在父类角度,下面的例子演示了父类和子类没有重复的属性和方法,以及如果有重复时的情况


#下面的例子中属性和方法都不发生冲突

# class Person:
#     country = 'China'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def work(self):
#         print("I am working....")
#
#
# #派生一个子类
#
# class Men(Person):
#     #子类属性
#     male = 'men'
#
#     #新增子类方法
#     def sleep(self):
#         print("I am sleeping")
#
# #实例化子类.注意要传递参数给父类的构造函数,
#
# man = Men('jesse',20)
#
# #调用父类的work方法和name属性.和country属性
#
# man.work()
# print(man.name)
# print(man.country)



#下面的例子属性和方法有冲突
#
# class Person:
#     country = 'China'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def work(self):
#         print("I am working....")
#
#
# #派生一个子类
#
# class Men(Person):
#
#     def __init__(self,male,country):
#         #子类属性
#         self.male = male
#         self.country = country
#
#     def work(self):
#         print("I don't like working.....")
#
#     #新增子类方法
#     def sleep(self):
#         print("I am sleeping")
#
#
# #man = Men('male','America')
# man = Men('jesse',23)
# man.work()
# print(man.male)
# print(man.country)
# print(man.age) #无法访问父类的age属性,因为被子类的__init__方法覆盖

#如果需要访问父类的age属性,
#
#当子类父类都有构造方法时 , 如果子类需要父类构造方法中的实例属性怎么办 ?
#当子类父类都有同名方法时 , 如果子类需要用父类中的方法怎么办?

#解决问题1.子类和父类构造方法中实例属性集合

# class Person:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# #派生一个子类
#
# class Men(Person):
#
#     def __init__(self,name,age,male):
#         #子类属性
#         self.male = male
#         #子类调用Person父类的__init__方法,也就是将父类的__init__方法拿过来用一遍
#         Person.__init__(self,name,age)
#
#
# #实例化Men类
#
# man = Men('jesse',23,'male')
#
# #访问man属性
# print(man.name)
# print(man.age)
# print(man.male)

#解决问题2 : 使用父类中的重名方法


# class Person:
#
#     def work(self):
#         print("I am working....")
#
# #派生一个子类
#
# class Men(Person):
#
#     def work(self):
#         print("I don't like working....")
#
#
# #实例化Men类
# man = Men()
#
# #将实例man作为self参数传入Person中的work方法
#
# Person.work(man)

#两个问题解决了 , 但是我们发现通过这两种方式来解决会对后期修改造成非常大的麻烦.所以就有了super

#super只能用在新式类

#上述问题1:
#
# class Person:
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
# #派生一个子类
#
# class Men(Person):
#
#     def __init__(self,name,age,male):
#         #子类属性
#         self.male = male
#         #子类调用super方法.__init__方法后直接跟参数,不需要指定self关键字
#         super().__init__(name,age)
#
#
# #实例化Men类
#
# man = Men('jesse',23,'male')
#
# #访问man属性
# print(man.name)
# print(man.age)
# print(man.male)

#问题2

# class Person:
#
#     def work(self):
#         print("I am working....")
#
# #派生一个子类
#
# class Men(Person):
#
#     def work(self):
#         print("I don't like working....")
#
#
# #实例化Men类
# man = Men()
#
# # super的第一个参数是要找父类的那个类
#
# super(Men,man).work()



# class A(object):
#     def __init__(self):
#         print("This is from A")
# class B(A):
#     def __init__(self):
#         print("This is from B")
#         super().__init__()
#         print("This is from B")
# class C(A):
#     def __init__(self):
#         print("This is from C")
#         super().__init__()
#         print("This is from C")
# class D(B,C):
#     def __init__(self):
#         print("This is from D")
#         super().__init__()
#         print("This is from D")
# d = D()

#类的限制访问, __双划线开头的变量表示这个变量是私有变量,不允许从外部访问.要想访问可以定义一个方法来获取

# class Person():
#     def __init__(self,name):
#         self.__name = name
#
#     def get_name(self):
#         self.__name = self.__name+'hello'
#         return self.__name
#
# p1 = Person('jesse')
# print(p1.get_name())
# print(p1._Person__name)

#使用私有方法,可以实现子类不会继承父类方法

class A:
    def __func(self):
        print("From A")

    def test1(self):
        self.__func()


class B(A):
    def __func(self):
        print("From B")

    def test2(self):
        self.__func()


b = B()

b.test1()
b.test2()
