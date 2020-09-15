#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 下午7:17
# @Author  : jesse
# @File    : 01-helloworld.py

from flask import Flask,escape
app = Flask(__name__)

#装饰器,装饰器内的URL关联一个视图函数,表示访问哪个URL就使用哪个视图函数处理访问请求
@app.route('/') #访问根目录,就使用Hello_world函数处理请求
def hello_world():
    return 'hello,world!' #响应值,浏览器响应给用户的页面

@app.route('/hello')
def hello():
    return "hello hello"

@app.route('/user/<username>')  #<>表示一个变量参数 username数据类型代表一个字符串
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>') #<>里面还可以使用数据类型:变量格式.,int表示一个整数数据类型,并且将整数赋值给post_id变量
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>') #path数据类型也是字符串,但是可以包括URL的斜杠符号
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

if __name__ == "__main__":
     app.run()