#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 下午7:17
# @Author  : jesse
# @File    : 01-helloworld.py

from flask import Flask,escape
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hello,world!'

@app.route('/hello')
def hello():
    return "hello hello"

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return 'Subpath %s' % escape(subpath)

if __name__ == "__main__":
     app.run()