#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth2 import Oauth2


class Facebook(Oauth2):

    NAME = 'Facebook'
    AUTHORIZATION_URL = 'https://www.facebook.com/dialog/oauth'
    ACCESS_TOKEN_URL = 'https://graph.facebook.com/oauth/access_token'
    GET_USERINFO_URL = 'https://graph.facebook.com/me?fields=id,name,email,picture'

    def __init__(self):
        super(Facebook, self).__init__()

    def parse_token_response(self, response):
        r = self._query_to_dict(response)
        self._access_token = r.get('access_token', '')
        self._expires_in = r.get('expires', '')

    def parse_user_info(self, response):
        return {
            'uid': response.get('id'),
            'name': response.get('name'),
            'avatar': response.get('picture', {}).get('data', {}).get('url'),
            'raw': response
        }
