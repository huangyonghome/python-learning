#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/30 下午5:19
# @Author  : jesse
# @File    : argparse_mysql.py

import argparse

def _argparse():
    parser = argparse.ArgumentParser(description='A python-Mysql client')
    parser.add_argument('--host', action='store', dest='host', required=True, help='connect to host')
    parser.add_argument('-u', '--user', action='store', dest='user', required=True, help='user for login')
    parser.add_argument('-p', '--password', action='store', dest='password', required=True, help='password for login')
    parser.add_argument('-P', '--port', action='store', dest='port', default=3306, type=int, help='port number to user for connection.default is 3306')
    parser.add_argument('-v', '--version', action='version', version='%(prog)s 0.1')
    return parser.parse_args()

def start():
    print('continue')

def main():
    parser = _argparse()
    conn_args = dict(host=parser.host, user=parser.user, password=parser.password,port=parser.port)
    print(conn_args)
    start()


if __name__ == '__main__':
    main()