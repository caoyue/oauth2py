#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import mock

from oauth2py.client import OauthClient


class TestGithub(unittest.TestCase):

    def setUp(self):
        self.config = {
            'name': 'github',
            'client_id': '1234567',
            'client_secret': 'secret_abcefg',
            'redirect_uri': 'http://127.0.0.1/oauth/github/callback',
            'scope': ''
        }
        self.access_token_resp = {
            'access_token': 'abcdefg',
            'expires_in': '1234567',
            'uid': '12345'
        }
        self.user_info_resp = {
            u'public_repos': 22,
            u'site_admin': False,
            u'subscriptions_url': u'https://api.github.com/users/caoyue/subscriptions',
            u'gravatar_id': u'',
            u'hireable': None,
            u'id': 522324,
            u'followers_url': u'https://api.github.com/users/caoyue/followers',
            u'following_url': u'https://api.github.com/users/caoyue/following{/other_user}',
            u'blog': None,
            u'followers': 8,
            u'location': u'Shenzhen, China',
            u'type': u'User',
            u'email': None,
            u'bio': None,
            u'gists_url': u'https://api.github.com/users/caoyue/gists{/gist_id}',
            u'company': None,
            u'events_url': u'https://api.github.com/users/caoyue/events{/privacy}',
            u'html_url': u'https://github.com/caoyue',
            u'updated_at': u'2016-04-14T03:12:26        Z',
            u'received_events_url': u'https://api.github.com/users/caoyue/received_events',
            u'starred_url': u'https://api.github.com/users/caoyue/starred{/owner}{/repo}',
            u'public_gists': 34,
            u'name': u'caoyue',
            u'organizations_url': u'https://api.github.com/users/caoyue/orgs',
            u'url': u'https://api.github.com/users/caoyue',
            u'created_at': u'2010-12-14T08:05:49 Z',
            u'avatar_url': u'https://avatars.githubusercontent.com/u/522324?v=3',
            u'repos_url': u'https://api.github.com/users/caoyue/repos',
            u'following': 1,
            u'login': u'caoyue'
        }
        self.github = OauthClient.load('github')
        self.github.init(self.config)

    def test_get_login_url(self):
        self.assertEqual(
            self.github.get_login_url(),
            'https://github.com/login/oauth/authorize?redirect_uri={0}&response_type=code&client_id={1}'.format(
                self.config['redirect_uri'], self.config['client_id'])
        )

        self.assertEqual(
            self.github.get_login_url(state='abc'),
            'https://github.com/login/oauth/authorize?state=abc&redirect_uri={0}&response_type=code&client_id={1}'.format(
                self.config['redirect_uri'], self.config['client_id'])
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

        user = self.github.get_user_info(query)

        self.assertEqual(mock_get.call_count, 1)
        self.assertEqual(mock_post.call_count, 1)

        # assert state
        self.assertEqual(self.github.state, 'abc')

        # assert access token
        token = self.github.get_access_token()
        self.assertEqual(
            token['access_token'],
            self.access_token_resp['access_token']
        )

        # assert response uid
        self.assertEqual(user['uid'], self.user_info_resp['id'])
