#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'an simple, lightweight oauth client',
    'author': 'caoyue',
    'url': '',
    'download_url': 'Wher',
    'author_email': 'i@caoyue.me',
    'version': '0.1.1',
    'install_requires': ['nose'],
    'packages': ['oauth2client'],
    'scripts': [],
    'name': 'oauth2client'
}

setup(**config)
