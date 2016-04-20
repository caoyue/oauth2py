#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from oauth2py.client import OauthClient


class TestFacebook(unittest.TestCase):

    def setUp(self):
        self.config = {
            'name': 'facebook',
            'client_id': '1234567',
            'client_secret': 'secret_abcefg',
            'redirect_uri': 'http://127.0.0.1/oauth/facebook/callback',
            'scope': ''
        }
        self.access_token_resp = "access_token=CAAC5oaHfBC8BABEaVGQGJtt1iBqwVeGZBVScuJfhxkd5LTxZAbEVN1NAUv89JtIYBYiG7ZARfJ5VnZBVHwS3Tdnus6fuQnJLzXZAoBbbwZCCBnVpKCyEXbwV79CZAUIlRQGmR8zb602bL3GpRSQcf6qbGRZArH115prFWciZBwu9mcmRgn5lPOZBKotpSVt3WcH6kZD&expires=5172977"
        self.user_info_resp = {
            u'email': u'****',
            u'picture': {
                u'data': {
                    u'url': u'https://scontent.xx.fbcdn.net/hprofile-xaf1/v/t1.0-1/c37.31.385.385/s50x50/549771_545991638744577_556687133_n.jpg?oh=799d5131f320b6457c24bae93e3e5a84&oe=57ABCA68',
                    u'is_silhouette': False
                }
            },
            u'id': u'1111862645490804',
            u'name': u'Yue Cao'
        }
        self.facebook = OauthClient.load('facebook')
        self.facebook.init(self.config)

    def test_get_login_url(self):
        self.assertEqual(
            self.facebook.get_login_url(),
            'https://www.facebook.com/dialog/oauth?redirect_uri=http://127.0.0.1/oauth/facebook/callback&response_type=code&client_id=1234567'
        )

        self.assertEqual(
            self.facebook.get_login_url(state='abc'),
            'https://www.facebook.com/dialog/oauth?state=abc&redirect_uri=http://127.0.0.1/oauth/facebook/callback&response_type=code&client_id=1234567'
        )

    @mock.patch('oauth2py.base.requests.post')
    @mock.patch('oauth2py.base.requests.get')
    def test_get_user_info(self, mock_get, mock_post):
        query = 'code=12345&state=abc'
        # query = {
        #     'code': '12345',
        #     'state':'abc'
        # }

        mock_get_response = mock.Mock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = self.user_info_resp

        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.content = self.access_token_resp
        mock_post_response.json.side_effect = ValueError("Not valid json")

        mock_get.return_value = mock_get_response
        mock_post.return_value = mock_post_response

        user = self.facebook.get_user_info(query)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_post.call_count, 1)

        # assert state
        self.assertEqual(self.facebook.state, 'abc')

        # assert access token
        token = self.facebook.get_access_token()
        self.assertEqual(
            token['access_token'],
            'CAAC5oaHfBC8BABEaVGQGJtt1iBqwVeGZBVScuJfhxkd5LTxZAbEVN1NAUv89JtIYBYiG7ZARfJ5VnZBVHwS3Tdnus6fuQnJLzXZAoBbbwZCCBnVpKCyEXbwV79CZAUIlRQGmR8zb602bL3GpRSQcf6qbGRZArH115prFWciZBwu9mcmRgn5lPOZBKotpSVt3WcH6kZD'
        )

        # assert response uid
        self.assertEqual(user['uid'], self.user_info_resp['id'])
