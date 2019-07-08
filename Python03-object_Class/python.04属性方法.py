# -*- coding: utf-8 -*-
# @Time    : 2019-06-02 21:15
# @Author  : jesse
# @File    : python.04属性方法.py

#私有方法

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
#
# class A:
#     def __func(self):
#         print("From A")
#
#     def test1(self):
#         self.__func()
#
#
# class B(A):
#     def __func(self):
#         print("From B")
#
#     def test2(self):
#         self.__func()
#
#
# b = B()
#
# b.test1()
# b.test2()


#静态方法
#
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


#类方法

#类方法通过@classmethod装饰器实现，类方法和普通方法的区别是， 类方法只能访问类变量，不能访问实例变量

# class Person:
#     country = 'china'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def search(cls):
#        print("i come from {}".format(cls.country))
#         print("{} come from {}".format(self.name,cls.country)) #报错.类方法中不能访问实例变量
#
# p = Person('jesse',22)
# p.search()

#属性方法

#属性方法就是通过使用装饰器 `@property ` , 将一个方法变成一个静态属性 , 于是我们就可以通过访问属性 , 来或得一个方法的返回值


# class Person:
#     country = 'china'
#
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     @property
#     def search(self):
#
#         print("{} come from {}".format(self.name,Person.country))
#
# p = Person('jesse',22)
# p.search  #因为search已经变成了一个属性.所以不能用方法来调用.而是像调用一个静态属性一样调用

#
# from urllib.request import urlopen
#
# class Web_page:
#     def __init__(self,url):
#         self.url = url
#         self.__content = None
#
#     @property
#     def content(self):
#         return self.__content if self.__content else urlopen(self.url).read()
#
#
# con = Web_page('http://www.baidu.com')
# res = con.content
# print(res)


#property静态属性实现了3种方法.get set delete

# class Foo:
#
#     #获取属性
#     @property
#     def AAA(self):
#         print("执行了get方法")
#
#     #设定属性值
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
# f.AAA #获取静态属性
# f.AAA = 'aaa' #给修改属性值
# del f.AAA #删除静态属性


#实际应用

# class Goods:
#     def __init__(self):
#         #原价
#         self.original_price = 100
#         #折扣
#         self.discount = 0.8
#
#     #静态属性.获取price价格
#     @property
#     def price(self):
#         good_price = self.original_price * self.discount
#         return good_price
#
#     #静态属性的修改方法,调整静态属性的值.注意方法名不变仍然为price
#     @price.setter
#     def price(self,value):
#         self.original_price = value
#
#     # 静态属性的删除方法,删除某个静态属性.注意方法名不变仍然为price
#     @price.deleter
#     def price(self):
#         del self.original_price
#
#
# #实例化一个对象
#
# apple = Goods()
#
# #获取价格
# print(apple.price)
#
# #修改原价后,再次获取价格
# apple.price = 200
# print(apple.price)
#
# #删除价格
# # del apple.price
# # print(apple.price) #再次获取价格会报错
#
# class C:
#
#     count = 0
#
#     def __init__(self):
#         self.ou()
#
#
#     def ou(self):
#         C.count += 1
#
# a = C()
# a.ou()
# a.ou()
# a.ou()
# a.ou()
# a.ou()
# a.ou()
# print(a.count)


#属性方法.计算BMI指数


class A:

    def __init__(self,weight,high):
        self.weight = weight
        self.high = high

    @property
    def bmi(self):
        BMI = self.weight / (self.high ** 2)
        print(BMI)
        if  18.5 >= BMI:
            return "体重过轻"
        elif 18.5 < BMI <= 23.9:
            return "体重正常"
        elif 24 < BMI <= 27:
            return "体重过重"
        elif 28 <= BMI <= 32:
            return "肥胖"
        elif 32 <= BMI:
            return "非常肥胖"


a = A(72,1.70)
print(a.bmi)
