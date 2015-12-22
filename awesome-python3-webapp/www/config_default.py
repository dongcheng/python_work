#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
Default configurations.
'''

__author__ = 'Michael Liao'

configs = {
    'debug': True,
    'db': {
        'host': '172.30.74.164',
        'port': 3306,
        'user': 'peopledata',
        'password': 'peopledatapassword',
        'db': 'dc_test'
    },
    'session': {
        'secret': 'Awesome'
    }
}