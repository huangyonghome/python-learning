#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/4/27 下午4:55
# @Author  : jesse
# @File    : python函数练习.py


# 实参角度

    #1.位置参数: 位置参数要求从前至后一一对应
    #2.关键字传参: 形参和实参的参数名要求一致,但是顺序不做要求..但是实参和形参的数量也必须要一一对应
    #3.混合传参: 既有位置参数,又有关键字参数.但是关键字参数必须要在位置参数后面

''''''
#练习:返回数字较大的参数
#
# def func1(a,b):
#     if a >  b:
#         return a
#     else:
#         return b
#
# # print(func1(3,4))
#
# ## 三元运算..对于简单的if ... else...语句,可以用一行代码实现,,也就是3元运算
# # a = 3
# # b = 20
# # ret = a if a > b else  b
# #
# # print(ret)
#
# # 所以上面的函数可以简化成
#
# def func2(a,b):
#     return a if a > b else  b
#
# print(func2(20,5))
''''''

#2.关键字传参.

# def func3(name,age):
#     return name,age
#
# print(func3(age=34,name="jesse"))
#
# #如果数量不能一一对应,则报错
#
# print(func3(age=34,name='jesse',job='it'))

''''''
#3.混合参数

# def func4(a,b,c,name):
#     print(a,b,c,name)
#
# func4(1,2,3,name='jesse')
#
# #如果关键字参数在前面,则报错
#
# func4(name='jesse',1,2,3)
''''''

# 形参角度
    #1.位置桉树: 和实参一样
    #2.默认参数: 函数定义时,就先已经定义了参数的值
    #3.动态参数,万能参数.表示法: *args, **kwargs


'''
默认参数
'''

# def func5(name,age,sex='male'):
#     print(name,age,sex)
#
# #如果函数调用没有传入这个参数,则参数的值为默认值
# func5('jesse',22)
#
# #如果函数调用有传入这个参数,而且值不一样,则函数的默认参数值会被覆盖
# func5('jesse',22,'female')
#
# #或者用关键字参数定义也一样
# func5('jesse',22,sex='female')


# 练习

# 设计一个函数,功能是编辑一个登记表的文档.让用户输入姓名,年龄和性别,然后记录到这个文档中.如果性别未输入,则默认为男

# def w_file(name,age,sex='男'):
#     with open('register.txt',mode='a') as f:
#         f.write("%s \t %d \t %s \n" %(name,age,sex))
#
#
# while 1:
#     name = input("姓名:(按Q,q退出程序)")
#     if name.upper() == "Q": break
#     age = int(input("年龄:"))
#     sex = input("性别:(如果是男,则直接回车)")
#     if sex:
#        w_file(name.strip(),age,sex)
#     else:
#         w_file(name.strip(), age)


'''
动态参数
'''

# 动态参数用*args和**kwargs来定义形参.*表示聚合.将函数调用者传递的所有位置参数聚合在一起,赋值给args.将函数调用者传递的所有关键字参数聚合在一起,赋值给kwargs

# def func6(*args,**kwargs):
#     print(args)
#     print(kwargs)
#
# func6(1,2,3,4,name='jesse',age=22,sex='male')
#
# func6([1,2,3,4],[2,3,4,5],name='jesse',age=22,sex='male')

# 练习:

# #将下列数据传入函数args参数,并且最终打印出来的是一个元祖.效果如下(1,2,3,4,11,22,33,44......555)
#
# l1 = [1,2,3,4]
# l2 = [11,22,33,44]
# l3 = (111,222,333,444,555)
#
#
# # def func7(*args):
# #    t1 = ()
# #    for i in args:
# #        t1 = t1 + tuple(i)
# #    print(t1)
# #
# # func7(l1,l2,l3)
#
# #有个更简单的用法
#
# def func8(*args):
#     print(args)
# func8(*l1,*l2,*l3)
#
# ## 形参中的*和** 表示聚合,将聚合后的值赋值给args和kwargs
# ## 实参中的*和** 表示打散,其中*表示将多个可迭代的对象拆分(l1,l2,l3),然后依次传递个形参的args
# ##                     其中**表示将多个可迭代的字典拆分,然后依次传递给形参的**kwargs
#
# # 例如:
#
# dic1 = {'name':'jesse',"age":22}
# dic2 = {'job':'it',"company":'dwd'}
#
# def func9(**kwargs):
#     print(kwargs) #kwargs并非将2个字典作为2个独立元素打印,而是将2个字典所有元素合并在一起打印
#
# func9(**dic1,**dic2)
#
#
# # def main(*args, **kwargs):  # 参数状态:(1,2,3,4,5){'n1':1,'n2':2,'n3'=3}
# #     # 进行解包
# #     return (*args), {**kwargs}  # 参数状态:1,2,3,4,5,n1=1,n2=2,n3=3
# #
# #
# # result = main(1, 2, 3, 4, 5, n1=1, n2=2, n3=3)
# # print(result)
#
#
# mytuple = (1,2,3,4,5,6,7)
#   # _为占位符,*c打包成列表
#
# mytuple = (1,2,3,4,5,6,7)
#   # _为占位符,*c打包成列表
# a,_,b,*c,d = mytuple
# print(a)
# print(b)
# print(c)
# print(d)
# ##
#
# '''
# 参数顺序
# '''
#
# ## 顺序依次如下:位置参数,*args,关键字参数,**args
#
#
# def func9(a,b,*args,sex='male',**kwargs):
#     print(a,b)
#     print(args)
#     print(sex)
#     print(kwargs)
#
# func9(1,2,3,4,5,6,sex='female',name='jesse',age=24)
#
# func9(1,2,3,4,5,6,name='jesse',age=24,sex='female')

# def func(*args):
#     print(args)
#
#
# def func1(*args):
#     func(*args)
#
# func1("hello,world","jesse")

