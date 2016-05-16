#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
from oauth2 import Oauth2


class Qq(Oauth2):

    NAME = 'QQ'
    AUTHORIZATION_URL = 'https://graph.qq.com/oauth2.0/authorize'
    ACCESS_TOKEN_URL = 'https://graph.qq.com/oauth2.0/token'
    GET_USERINFO_URL = 'https://graph.qq.com/oauth2.0/me'

    def __init__(self):
        super(Qq, self).__init__()

    def parse_token_response(self, response):
        d = self._query_to_dict(response)
        self._access_token = d.get('access_token', '')
        self._expires_in = d.get('expires_in', '')
        self._refresh_token = d.get('refresh_token', '')

    def parse_user_info(self, response):
        r = response[response.index('(') + 1: response.rindex(')')]
        d = json.loads(r)
        uid = d.get('openid', '')
        detail = self.access_resource(
            'GET',
            'https://graph.qq.com/user/get_user_info',
            params={
                'oauth_consumer_key': self._config['client_id'],
                'openid': uid
            })
        return {
            'uid': uid,
            'name': detail.get('nickname'),
            'avatar': detail.get('figureurl_qq_1'),
            'raw': detail
        }
