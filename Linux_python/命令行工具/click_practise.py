#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/10/1 上午8:40
# @Author  : jesse
# @File    : click_practise.py
import click

@click.command()
# @click.option('--count', default=1, help='number of greetings')
# @click.option('--name', prompt='Your name', help='the person to greet')
# @click.option('--pos', nargs=2, type=float)
#
# def hello(count,name):
#     for x in range(count):
#         click.echo('hello %s!' %name)
#         print('%d' %x)

# def haha(pos):
#     print(pos)


@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)

def encrypt(password):
    print(password)
    print('Encrypting password to %s' %password.encode('utf-8'))

# if __name__ == '__main__':
#     hello()

encrypt()