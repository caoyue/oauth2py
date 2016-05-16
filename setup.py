#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup


def long_description():
    try:
        return open('README.rst').read()
    except IOError:
        return 'a simple, lightweight oauth client'

config = {
    'name': 'oauth2py',
    'version': '1.1.4',
    'description': 'a simple, lightweight oauth client',
    'author': 'caoyue',
    'author_email': 'i@caoyue.me',
    'url': 'https://github.com/caoyue/oauth2py',
    'download_url': 'https://github.com/caoyue/oauth2py',
    'license': 'http://www.apache.org/licenses/LICENSE-2.0',
    'install_requires': [''],
    'packages': ['oauth2py'],
    'classifiers': [
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    'long_description': long_description(),
}

setup(**config)
