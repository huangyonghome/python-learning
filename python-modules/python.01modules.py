# -*- coding: utf-8 -*-
# @Time    : 2019-06-08 8:52
# @Author  : jesse
# @File    : python.01modules.py

#导入模块,模块名是以py后缀结尾的文件名.
# import my_module

#调用模块中的方法格式为:模块名.方法
# my_module.read()


#from格式:

#from 模块名 import 方法. 这种格式导入模块,就可以直接使用方法,而不需要指定模块名.方法
# from my_module import read
#
# read()

#给模块名取名
# import my_module as m1
#
# m1.read()
#
# from my_module import read as r
# r()

#__name__属性

#执行下面代码.my_module模块执行了print(__name__)语句..从外部执行模块的__name__属性为模块名.也就是my_module.
#如果是从模块文件里面去执行print(__name__).结果是__main__

#所以根据__name__属性可以知道执行当前的代码是直接执行本文件,还是从外部来执行
import my_module



