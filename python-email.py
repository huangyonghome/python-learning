#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/27 下午6:12
# @Author  : jesse
# @File    : python-email.py

#
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
# # 第三方 SMTP 服务
# mail_host = "smtphz.qiye.163.com"  # 设置服务器
# mail_user = "devops@doweidu.com"  # 用户名
# mail_pass = "DWDduoweidu@2018"  # 口令
#
# sender = 'devops@doweidu.com'
# receivers = ['mailhuangyong@163.com']  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
#
# message = MIMEText('Python 邮件发送测试...', 'plain', 'utf-8')
# message['From'] = Header("devops@doweidu.com", 'utf-8')
# message['To'] = Header("测试", 'utf-8')
#
# subject = 'Python SMTP 邮件测试'
# message['Subject'] = Header(subject, 'utf-8')
#
# try:
#     smtpObj = smtplib.SMTP()
#     smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
#     smtpObj.login(mail_user, mail_pass)
#     smtpObj.sendmail(sender, receivers, message.as_string())
#     print("邮件发送成功")
# except smtplib.SMTPException:
#     print("Error: 无法发送邮件")

import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = 'devops@doweidu.com'  # 发件人邮箱账号
my_pass = 'xxxxxx'  # 发件人邮箱密码
my_user = 'mailhuangyong@163.com'  # 收件人邮箱账号，我这边发送给自己


def mail():
    ret = True
    try:
        msg = MIMEText('填写邮件内容', 'plain', 'utf-8')
        msg['From'] = my_sender  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] =  my_user  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "菜鸟教程发送邮件测试"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtphz.qiye.163.com", 465)  # 发件人邮箱中的SMTP服务器，端口是25
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        ret = False
    return ret


ret = mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")