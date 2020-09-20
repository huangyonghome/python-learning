# -*- coding: utf-8 -*-
# @Time    : 2020-09-20 22:19
# @Author  : jesse
# @File    : hello.py

from flask import Flask,render_template
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)

#运行方式:
'''
进入当前目录
1. set/export FLASK_APP=hello.py
2. set/export FLASK_ENV=development
3. flask run
'''

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/user/<name>')
def user(name):
    return render_template('user.html',name=name)

#自定义错误页面
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500