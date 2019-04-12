#!/usr/bin/env python
#-*- coding: utf-8 -*-

import pymysql

configs = {
    'debug': True,
    'db': {
        'host': '127.0.0.1',
        'port': 3306,
        'user': 'root',
        'password': '888',
        'db': 'awesome',
        'cursorclass': pymysql.cursors.DictCursor
    },
    'session': {
        'secret': 'Awesome'
    }
}