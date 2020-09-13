#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/9 下午10:42
# @Author  : jesse
# @File    : 04-重定向和错误页面.py

from flask import Flask
from flask import abort,redirect,url_for,render_template

app = Flask(__name__)


@app.route('/')
def index():
    #redirect函数可以重定向
    return redirect(url_for('login')) ##访问根目录,重定向到login视图函数去处理


@app.route('/login')
def login():
    abort(401)  #abort函数提出一个异常错误码
    this_is_never_executed()


#错误页面处理装饰器
@app.errorhandler(404)
def page_not_found(error):
    #render_template表示使用templates下面的模板页面,404参数表示状态码是404
    return render_template('page_not_found.html'),404


if __name__ == "__main__":
     app.run()