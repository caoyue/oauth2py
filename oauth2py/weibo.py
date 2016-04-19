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

    def parse_user_info(self, response):
        return {
            'uid': response['id'],
            'name': response['name'],
            'avatar': response['profile_image_url'],
            'raw': response
        }

    def _get_access_token(self, params, grant_type='authorization_code'):
        params['client_id'] = self._config['client_id']
        params['client_secret'] = self._config['client_secret']
        params['redirect_uri'] = self._config['redirect_uri']
        params['grant_type'] = grant_type

        if grant_type != 'authorization_code':
            params['refresh_token'] = self._refresh_token

        r = self.post({
            'url': self.ACCESS_TOKEN_URL,
            'params': params
        })

        self._access_token = r.get('access_token', '')
        self._expires_in = r.get('expires_in', '')
        self._refresh_token = r.get('refresh_token', '')
        self._uid = r.get('uid', '')

    def _get_user_info(self):
        payload = {
            'access_token': self._access_token,
            'uid': self._uid
        }
        return self.get({
            'url': self.GET_USERINFO_URL,
            'params': payload
        })
