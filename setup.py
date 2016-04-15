#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'name': 'oauth2py',
    'version': '0.1.0',
    'description': 'an simple, lightweight oauth client',
    'author': 'caoyue',
    'author_email': 'i@caoyue.me',
    'url': '',
    'download_url': '',
    'license':  'http://www.apache.org/licenses/LICENSE-2.0',
    'install_requires': [''],
    'packages': ['oauth2py'],
    'classifiers': [
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ]
}

setup(**config)
