#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth import Oauth


class Twitter(Oauth):

    NAME = 'Twitter'
    REQUEST_TOKEN_URL = 'https://api.twitter.com/oauth/request_token'
    AUTHENTICATE_URL = 'https://api.twitter.com/oauth/authenticate'
    ACCESS_TOKEN_URL = 'https://api.twitter.com/oauth/access_token'
    GET_USERINFO_URL = 'https://api.twitter.com/1.1/account/verify_credentials.json'

    def __init__(self):
        super(Twitter, self).__init__()

    def parse_user_info(self, response):
        return {
            'uid': response.get('id_str'),
            'name': response.get('name'),
            'avatar': response.get('profile_image_url_https'),
            'raw': response
        }
