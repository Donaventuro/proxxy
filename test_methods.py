#! /usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def test():
    print("Проверка метода get " + str(requests.get('http://localhost:9000/')))
    print("Проверка метода post " + str(requests.post('http://localhost:9000/post', data={'key': 'value'})))
    print("Проверка метода put " + str(requests.put('http://localhost:9000/put', data={'key': 'value'})))
    print("Проверка метода delete " + str(requests.delete('http://localhost:9000/delete')))
    print("Проверка метода head " + str(requests.head('http://localhost:9000/get')))
    print("Проверка метода patch " + str(requests.patch('http://localhost:9000/patch', data={'key': 'value'})))
    print("Проверка метода options " + str(requests.options('http://localhost:9000/get')))



test()
