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
        self.access_token_resp = {
            'access_token': 'abcdefg',
            'expires_in': '1234567',
            'uid': '12345'
        }
        self.user_info_resp = {
            u'status': {
                u'reposts_count': 0,
                u'mlevel': 0,
                u'truncated': False,
                u'text': u'\u60f3\u8d77\u7a0b\u5e8f\u5f00\u53d1\u4e2d\u7684\u6700\u5927\u6d41\u6d3e\u4e4b\u4e00 DDD (Deadline-Driven Development) [doge] //@tombkeeper:\u4e94\u5473\u6742\u9648\u2026\u2026',
                u'visible': {
                    u'type': 0,
                    u'list_id': 0
                },
                u'in_reply_to_status_id': u'',
                u'id': 3965220369495401,
                u'mid': u'3965220369495401',
                u'source': u'<a href="http://weibo.com/" rel="nofollow">\u5fae\u535a weibo.com</a>',
                u'attitudes_count': 0,
                u'in_reply_to_screen_name': u'',
                u'in_reply_to_user_id': u'',
                u'pic_urls': [],
                u'darwin_tags': [],
                u'favorited': False,
                u'text_tag_tips': [],
                u'source_allowclick': 0,
                u'idstr': u'3965220369495401',
                u'source_type': 1,
                u'hot_weibo_tags': [],
                u'geo': None,
                u'isLongText': False,
                u'userType': 0,
                u'created_at':      u'Sun Apr 17 12:01:09      +0800 2016',
                u'biz_feature': 0,
                u'comments_count': 0
            },
            u'domain': u'c4oyu3',
            u'avatar_large': u'http://tp1.sinaimg.cn/1047113932/180/22833261666/1',
            u'bi_followers_count': 3,
            u'verified_source': u'',
            u'ptype': 0,
            u'block_word': 0,
            u'star': 0,
            u'id': 1047113932,
            u'verified_reason_url': u'',
            u'urank': 9,
            u'city': u'3',
            u'verified': False,
            u'credit_score': 80,
            u'block_app': 0,
            u'follow_me': False,
            u'verified_reason': u'',
            u'followers_count': 85,
            u'location': u'\u5e7f\u4e1c \u6df1\u5733',
            u'verified_trade': u'',
            u'mbtype': 0,
            u'verified_source_url': u'',
            u'profile_url': u'c4oyu3',
            u'province': u'44',
            u'avatar_hd':   u'http://tva1.sinaimg.cn/crop.0.0.180.180.1024/3e69b0ccjw1e8qgp5bmzyj2050050aa8.jpg',
            u'statuses_count': 501,
            u'description': u'\u4ed6\u6559\u6211\u6536\u4f59\u6068\u3001\u514d\u5a07\u55d4\u3001 \u4e14\u81ea\u65b0\u3001\u6539\u6027\u60c5\u3001\u4f11\u604b\u901d\u6c34\u3001\u82e6\u6d77\u56de\u8eab\u3001\u65e9\u609f\u5170\u56e0',
            u'friends_count': 112,
            u'online_status': 0,
            u'mbrank': 0,
            u'idstr': u'1047113932',
            u'profile_image_url':   u'http://tp1.sinaimg.cn/1047113932/50/22833261666/1',
            u'allow_all_act_msg': True,
            u'allow_all_comment': True,
            u'geo_enabled': False,
            u'class': 1,
            u'name': u'c4oyu3',
            u'lang': u'zh-cn',
            u'weihao': u'',
            u'remark': u'',
            u'favourites_count': 4,
            u'screen_name': u'c4oyu3',
            u'url': u'',
            u'gender': u'm',
            u'created_at':   u'Wed Dec 16 22:18:14 +0800 2009',
            u'verified_type': -1,
            u'following': False,
            u'pagefriends_count': 0,
            u'user_ability': 0
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
        # query = {
        #     'code': '12345',
        #     'state':'abc'
        # }

        mock_get_response = mock.Mock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = self.user_info_resp

        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.json.return_value = self.access_token_resp

        mock_get.return_value = mock_get_response
        mock_post.return_value = mock_post_response

        user = self.weibo.get_user_info(query)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_post.call_count, 1)

        # assert state
        self.assertEqual(self.weibo.state, 'abc')

        # assert access token
        token = self.weibo.get_access_token()
        self.assertEqual(
            token['access_token'],
            self.access_token_resp['access_token']
        )

        # assert response uid
        self.assertEqual(user['uid'], self.user_info_resp['id'])
