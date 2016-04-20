#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from oauth2py.client import OauthClient as client

import os
import json


class TestClient(unittest.TestCase):

    def setUp(self):
        self.config = {
            'name': 'weibo',
            'client_id': '1234567',
            'client_secret': 'abcdefg',
            'redirect_uri': 'http://127.0.0.1/oauth/weibo/callback',
            'scope': ''
        }

    def test_load_client(self):
        client.load('weibo')

    def test_load_config(self):
        weibo = client.load('weibo')
        weibo.init(self.config)
        self.assertEqual(
            weibo.get_config()['client_id'],
            self.config['client_id']
        )

    def test_load_config_from_file(self):
        with open('oauth2py.config.json', 'w') as f:
            f.write(json.dumps([self.config]))

        client.reload_configs()
        weibo = client.load('weibo')
        self.assertEqual(
            weibo.get_config()['client_id'],
            self.config['client_id']
        )

    def tearDown(self):
        if os.path.isfile('oauth2py.config.json'):
            os.remove('oauth2py.config.json')
