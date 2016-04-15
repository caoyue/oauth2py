#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth2 import Oauth2


class Weibo(Oauth2):

    NAME = 'Weibo'
    AUTHORIZATION_URL = 'https://api.weibo.com/oauth2/authorize'
    ACCESS_TOKEN_URL = 'https://api.weibo.com/oauth2/access_token'
    GET_USERINFO_URL = 'https://api.weibo.com/2/account/get_uid.json'

    def __init__(self):
        super(Weibo, self).__init__()

    def parse_user_info(self, response):
        return {
            'uid': response['uid']
        }
