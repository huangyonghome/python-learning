#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 下午5:02
# @Author  : jesse
# @File    : hello.py

from flask import Flask,render_template,session,redirect,url_for,flash
from flask_mail import Mail
from flask_script import Manager
from flask_mail import Message
import os

app = Flask(__name__)

mail = Mail(app)
manager = Manager(app)

app.config['MAIL_SERVER'] = 'smtphz.qiye.163.com'
app.config['MAIL_PORT'] = 25
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'devops@doweidu.com'
app.config['MAIL_PASSWORD'] = 'DWDduoweidu@2018'
app.config['MAIL_DEFAULT_SENDER'] = 'devops@doweidu.com'




@app.route('/')
def index():
    return '<a href="{}">发送邮件<a/>'.format(url_for('send_mail'))


@app.route('/send_mail')
def send_mail():
    message = Message('我是邮件的主题', ['devops@doweidu.com'])
    # message.body = '我是内容'
    message.html = '<h1>我也是内容<h1/>'
    mail.send(message)
    return '邮件发送中......'


if __name__ == '__main__':
    app.run(debug=True)