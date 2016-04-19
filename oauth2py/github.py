#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth2 import Oauth2


class Github(Oauth2):

    NAME = 'Github'
    AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
    ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
    GET_USERINFO_URL = 'https://api.github.com/user'

    def __init__(self):
        super(Github, self).__init__()

    def parse_user_info(self, response):
        return {
            'uid': response['id'],
            'name': response['name'],
            'avatar': response['avatar_url'],
            'raw': response
        }
