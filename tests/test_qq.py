#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from oauth2py.client import OauthClient


class TestQQ(unittest.TestCase):

    def setUp(self):
        self.config = {
            'name': 'qq',
            'client_id': '1234567',
            'client_secret': 'secret_abcefg',
            'redirect_uri': 'http://127.0.0.1/oauth/qq/callback',
            'scope': ''
        }
        self.access_token = 'access_token123'
        self.access_token_resp = 'access_token={0}&expires_in=7776000&refresh_token=88E4BE14'.format(
            self.access_token)
        self.user_id_resp = 'callback( {"client_id":"1234567","openid":"abcde"} );'
        self.user_info_resp = {
            u'ret': '0',
            u'msg': '',
            u'is_lost': '0',
            u'nickname': 'caoyue',
            u'gender': '男',
            u'province': '',
            u'city': '',
            u'year': '1234',
            u'figureurl': 'http://qzapp.qlogo.cn/qzapp/100330589/46D42C580040C4AA42FD15141CF7DCC7/30',
            u'figureurl_1': 'http://qzapp.qlogo.cn/qzapp/100330589/46D42C580040C4AA42FD15141CF7DCC7/50',
            u'figureurl_2': 'http://qzapp.qlogo.cn/qzapp/100330589/46D42C580040C4AA42FD15141CF7DCC7/100',
            u'figureurl_qq_1': 'http://q.qlogo.cn/qqapp/100330589/46D42C580040C4AA42FD15141CF7DCC7/40',
            u'figureurl_qq_2': 'http://q.qlogo.cn/qqapp/100330589/46D42C580040C4AA42FD15141CF7DCC7/100',
            u'is_yellow_vip': '0',
            u'vip': '0',
            u'yellow_vip_level': '0',
            u'level': '0',
            u'is_yellow_year_vip': '0'
        }

        self.qq = OauthClient.load('qq')
        self.qq.init(self.config)

    def test_get_login_url(self):
        self.assertEqual(
            self.qq.get_login_url(),
            'https://graph.qq.com/oauth2.0/authorize?client_id={0}&redirect_uri={1}&response_type=code'.format(
                self.config['client_id'], self.config['redirect_uri'])
        )

        self.assertEqual(
            self.qq.get_login_url(state='abc'),
            'https://graph.qq.com/oauth2.0/authorize?client_id={0}&redirect_uri={1}&response_type=code&state=abc'.format(
                self.config['client_id'], self.config['redirect_uri'])
        )

    @mock.patch('oauth2py.base.requests.post')
    @mock.patch('oauth2py.base.requests.get')
    def test_get_user_info(self, mock_get, mock_post):
        query = 'code=12345&state=abc'
        # query = {
        #     'code': '12345',
        #     'state':'abc'
        # }

        mock_get.side_effect = self._mocked_requests_get

        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.content = self.access_token_resp
        mock_post_response.json.side_effect = ValueError('Not valid json')
        mock_post.return_value = mock_post_response

        user = self.qq.get_user_info(query)

        self.assertEqual(mock_get.call_count, 2)
        self.assertEqual(mock_post.call_count, 1)

        # assert state
        self.assertEqual(self.qq.state, 'abc')

        # assert access token
        token = self.qq.get_access_token()
        self.assertEqual(
            token['access_token'],
            self.access_token
        )

        # assert response uid
        self.assertEqual(user['name'], self.user_info_resp['nickname'])

    def _mocked_requests_get(self, *args, **kwargs):
        class MockResponse:

            def __init__(self, json_data, content, status_code):
                self.json_data = json_data
                self.content = content
                self.status_code = status_code

            def json(self):
                if not self.json_data:
                    raise ValueError('not valid json')
                return self.json_data

        if args[0] == 'https://graph.qq.com/oauth2.0/me':
            return MockResponse(None, self.user_id_resp, 200)
        else:
            return MockResponse(self.user_info_resp, '', 200)

        return MockResponse({}, '', 404)
