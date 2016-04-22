#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from oauth2py.client import OauthClient


class TestTwitter(unittest.TestCase):

    def setUp(self):
        self.config = {
            'name': 'twitter',
            'client_id': '1234567',
            'client_secret': 'secret_abcefg',
            'redirect_uri': 'http://127.0.0.1/oauth/twitter/callback',
            'scope': ''
        }
        self.request_oauth_token = 'Z6eEdO8MOmk394WozF5oKyuAv855l4Mlqo7hhlSLik'
        self.request_oauth_token_secret = 'Kd75W4OQfb2oJTV0vzGzeXftVAwgMnEK9MumzYcM'
        self.request_token_resp = 'oauth_token={0}&oauth_token_secret={1}&oauth_callback_confirmed=true'.format(
            self.request_oauth_token, self.request_oauth_token_secret)

        self.access_oauth_token = '6253282-eWudHldSbIaelX7swmsiHImEL4KinwaGloHANdrY'
        self.access_oauth_token_secret = '2EEfA6BG3ly3sR3RjE0IBSnlQu4ZrUzPiYKmrkVU'
        self.access_token_resp = 'oauth_token={0}&oauth_token_secret={1}&user_id=6253282&screen_name=twitterapi'.format(
            self.access_oauth_token, self.access_oauth_token_secret)

        self.user_info_resp = {
            u'follow_request_sent': False,
            u'has_extended_profile': False,
            u'profile_use_background_image': False,
            u'default_profile_image': False,
            u'id': 40811770,
            u'profile_background_image_url_https': u'https://abs.twimg.com/images/themes/theme1/bg.png',
            u'verified': False,
            u'profile_text_color': u'000000',
            u'profile_image_url_https': u'https://pbs.twimg.com/profile_images/3120262977/0822b66c760560bbc1b08490993314a5_normal.png',
            u'profile_sidebar_fill_color': u'000000',
            u'entities': {
                u'description': {u'urls': []}
            },
            u'followers_count': 75,
            u'profile_sidebar_border_color': u'000000',
            u'id_str': u'40811770',
            u'profile_background_color': u'000000',
            u'listed_count': 13,
            u'status': {
                u'contributors': None,
                u'truncated': False,
                u'text': u'\u5f53\u5e74\u5077\u5077\u770b\u738b\u5c0f\u6ce2\uff0c\u81ea\u79f0\u300c\u95e8\u4e0b\u8d70\u72d7\u300d\u7684\u5c0f\u4f19\u4f34\u4eec\uff0c\u5df2\u7ecf\u5fd8\u4e86\u8fd9\u56de\u4e8b\u4e86\u5427 \uff1d\u30fc\uff1d',
                u'is_quote_status': False,
                u'in_reply_to_status_id': None,
                u'id': 719515686796529664L,
                u'favorite_count': 0,
                u'source': u'<a href="http://caoyue.me" rel="nofollow">\u4e14\u542c\u75af\u541f</a>',
                u'retweeted': False,
                u'coordinates': None,
                u'entities': {},
                u'in_reply_to_screen_name': None,
                u'in_reply_to_user_id': None,
                u'retweet_count': 0,
                u'id_str': u'719515686796529664',
                u'favorited': False,
                u'geo': None,
                u'in_reply_to_user_id_str': None,
                u'lang': u'ja',
                u'created_at': u'Mon Apr 11 13:21:22 +0000 2016',
                u'in_reply_to_status_id_str': None,
                u'place': None
            },
            u'is_translation_enabled': False,
            u'utc_offset': 28800,
            u'statuses_count': 1493,
            u'description': u'\u4ed6\u6559\u6211\u6536\u4f59\u6068\u3001\u514d\u5a07\u55d4\u3001 \u4e14\u81ea\u65b0\u3001\u6539\u6027\u60c5\u3001\u4f11\u604b\u901d\u6c34\u3001\u82e6\u6d77\u56de\u8eab\u3001\u65e9\u609f\u5170\u56e0',
            u'friends_count': 134,
            u'location': u'China',
            u'profile_link_color': u'3B94D9',
            u'profile_image_url': u'http://pbs.twimg.com/profile_images/3120262977/0822b66c760560bbc1b08490993314a5_normal.png',
            u'following': False,
            u'geo_enabled': False,
            u'profile_background_image_url': u'http://abs.twimg.com/images/themes/theme1/bg.png',
            u'screen_name': u'caoyue',
            u'lang': u'en',
            u'profile_background_tile': False,
            u'favourites_count': 1,
            u'name': u'caoyue',
            u'notifications': False,
            u'url': None,
            u'created_at': u'Mon May 18 04:17:29 +0000 2009',
            u'contributors_enabled': False,
            u'time_zone': u'Beijing',
            u'protected': False,
            u'default_profile': False,
            u'is_translator': False
        }
        self.update_status_resp = {
            u'contributors': None,
            u'truncated': False,
            u'text': u'test from oauth2py!',
            u'is_quote_status': False,
            u'in_reply_to_status_id': None,
            u'id': 723005550229745665L,
            u'favorite_count': 0,
            u'source': u'<a href="http://l.caoyue.me" rel="nofollow">EsportsTest</a>',
            u'retweeted': False,
            u'coordinates': None,
            u'entities': {},
            u'in_reply_to_screen_name': None,
            u'in_reply_to_user_id': None,
            u'retweet_count': 0,
            u'id_str': u'723005550229745665',
            u'favorited': False,
            u'user': {},
            u'geo': None,
            u'in_reply_to_user_id_str': None,
            u'lang': u'en',
            u'created_at': u'Thu Apr 21 04:28:50 +0000 2016',
            u'in_reply_to_status_id_str': None,
            u'place': None
        }

        self.twitter = OauthClient.load('twitter')
        self.twitter.init(self.config)

    @mock.patch('oauth2py.base.requests.post')
    def test_get_login_url(self, mock_post):
        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.content = self.request_token_resp
        mock_post_response.json.side_effect = ValueError('Not valid json')

        mock_post.return_value = mock_post_response

        self.assertEqual(
            self.twitter.get_login_url(),
            'https://api.twitter.com/oauth/authenticate?oauth_token={0}'.format(
                self.request_oauth_token)
        )

        self.assertEqual(mock_post.call_count, 1)

    @mock.patch('oauth2py.base.requests.post')
    @mock.patch('oauth2py.base.requests.get')
    def test_get_user_info(self, mock_get, mock_post):
        mock_get_response = mock.Mock()
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = self.user_info_resp
        mock_get.return_value = mock_get_response

        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.content = self.access_token_resp
        mock_post_response.json.side_effect = ValueError('Not valid json')
        mock_post.return_value = mock_post_response

        login_url_query = 'oauth_token={0}&oauth_verifier=4TzL9SH0oZdsxvkHnbGrwiMzJS4EmjY6'.format(
            self.request_oauth_token)
        user = self.twitter.get_user_info(
            login_url_query, {
                'oauth_token': self.request_oauth_token,
                'oauth_token_secret': self.request_oauth_token_secret
            }
        )

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_post.call_count, 1)

        # assert access token
        token = self.twitter.get_access_token()
        self.assertEqual(
            token.get('access_token'),
            self.access_oauth_token
        )
        self.assertEqual(
            token.get('access_token_secret'),
            self.access_oauth_token_secret
        )

        # assert response uid
        self.assertEqual(user['uid'], self.user_info_resp['id_str'])

    @mock.patch('oauth2py.base.requests.post')
    def test_access_resource(self, mock_post):
        mock_post_response = mock.Mock()
        mock_post_response.status_code = 200
        mock_post_response.json.return_value = self.update_status_resp
        mock_post.return_value = mock_post_response

        self.twitter.set_access_token({
            'access_token': self.access_oauth_token,
            'access_token_secret': self.access_oauth_token_secret
        })

        token = self.twitter.get_access_token()
        self.assertEqual(
            token['access_token'],
            self.access_oauth_token
        )

        r = self.twitter.access_resource(
            'POST',
            url='https://api.twitter.com/1.1/statuses/update.json',
            data={
                'status': 'test from oauth2py!'
            })

        self.assertEqual(mock_post.call_count, 1)
        self.assertEqual(r['text'], self.update_status_resp['text'])
