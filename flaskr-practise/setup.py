#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/9/17 下午7:34
# @Author  : jesse
# @File    : setup.py

from setuptools import find_packages,setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)