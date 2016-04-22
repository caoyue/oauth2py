#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth2 import Oauth2


class Weibo(Oauth2):

    NAME = 'Weibo'
    AUTHORIZATION_URL = 'https://api.weibo.com/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://api.weibo.com/oauth2/access_token'
    GET_USERINFO_URL = 'https://api.weibo.com/2/users/show.json'

    def __init__(self):
        super(Weibo, self).__init__()

    def parse_token_response(self, response):
        self._access_token = response.get('access_token', '')
        self._expires_in = response.get('expires_in', '')
        self._uid = response.get('uid', '')

    def get_user_info_params(self):
        return {
            'access_token': self._access_token,
            'uid': self._uid
        }

    def parse_user_info(self, response):
        return {
            'uid': response.get('idstr'),
            'name': response.get('name'),
            'avatar': response.get('profile_image_url'),
            'raw': response
        }
