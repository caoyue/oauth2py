#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
from setuptools import setup


def long_description():
    with codecs.open('README.rst', encoding='utf-8') as f:
        long_description = f.read()

config = {
    'name': 'oauth2py',
    'version': '1.1.5',
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
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
    'long_description': long_description(),
}

setup(**config)
