#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/8 下午10:15
# @Author  : jesse
# @File    : 03-jinjia_practise.py

'''
演示jinjia2模板.
1.在根目录下创建一个templates目录,存放html的jinjia2的模板
2.在templates目录下创建一个hello.html网页模板

'''
from flask import Flask,render_template

app = Flask(__name__)

#路由装饰器
@app.route('/hello/')
@app.route('/hello/<name>')

#视图函数,关键字参数
def hello(name=None):
    #模板网页文件名称,以及jinjia2模板的变量,name是变量名,值是视图函数的参数,也就是用户传入的name
    return render_template('hello.html',name=name)


if __name__ == "__main__":
     app.run()