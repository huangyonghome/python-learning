# -*- coding: utf-8 -*-
# @Time    : 2020-09-18 23:49
# @Author  : jesse
# @File    : test_factory.py

from flaskr import create_app

def test_config():
    assert not create_app().testing
    assert create_app({'TESTING': True}).testing


def test_hello(client):
    response = client.get('/hello')
    assert response.data == b'Hello, World!'