#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from oauth2py.client import OauthClient


class TestWeibo(unittest.TestCase):

    def setUp(self):
        self.config = {
            'name': 'weibo',
            'client_id': '1234567',
            'client_secret': 'secret_abcefg',
            'redirect_uri': 'http://127.0.0.1/oauth/weibo/callback',
            'scope': ''
        }
        self.weibo = OauthClient.load('weibo')
        self.weibo.init(self.config)

    def test_get_login_url(self):
        self.assertEqual(
            self.weibo.get_login_url(),
            'https://api.weibo.com/oauth2/authorize?redirect_uri=http://127.0.0.1/oauth/weibo/callback&response_type=code&client_id=1234567'
        )

        self.assertEqual(
            self.weibo.get_login_url(state='abc'),
            'https://api.weibo.com/oauth2/authorize?state=abc&redirect_uri=http://127.0.0.1/oauth/weibo/callback&response_type=code&client_id=1234567'
        )

    @mock.patch('oauth2py.base.requests.post')
    @mock.patch('oauth2py.base.requests.get')
    def test_get_user_info(self, mock_get, mock_post):
        query = 'code=12345&state=abc'

        access_token_resp = {
            'access_token': 'abcdefg',
            'expires_in': '1234567'
        }

        uid_resp = {
            'uid': '1234567'
        }

        mock_get_response = mock.Mock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = uid_resp

        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.json.return_value = access_token_resp

        mock_get.return_value = mock_get_response
        mock_post.return_value = mock_post_response

        user = self.weibo.get_user_info(query)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_post.call_count, 1)

        # assert state
        self.assertEqual(self.weibo.state, "abc")

        # assert response uid
        self.assertEqual(user['uid'], uid_resp['uid'])

        # assert access token
        self.assertEqual(
            self.weibo.get_access_token()['access_token'],
            access_token_resp['access_token']
        )
