#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/7 下午7:53
# @Author  : jesse
# @File    : 02-url_for.py

from flask import Flask, escape, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return 'index'

@app.route('/login')
def login():
    return 'login'

@app.route('/user/<username>')
def profile(username):
    return '{}\'s profile'.format(escape(username))

with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John'))


if __name__ == "__main__":
     app.run()