#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

from base import Base
from exceptions import OauthException


class Oauth2(Base):

    def __init__(self):
        super(Oauth2, self).__init__()

    def get_login_url(self, state=''):
        self._check_config()

        payload = {
            'client_id': self._config['client_id'],
            'redirect_uri': self._config['redirect_uri'],
            'response_type': 'code'
        }

        if self._config['scope']:
            payload['scope'] = self._config['scope']

        if state:
            payload['state'] = state

        return self.build_request_uri({
            'url': self.AUTHORIZATION_URL,
            'params': payload
        })

    def get_access_token(self, refresh_token=''):
        '''get access_token, or use refresh_token update access_token'''
        self._check_config()

        if refresh_token:
            self._refresh_token = refresh_token
            self._get_access_token({}, 'refresh_token')

        return {
            'access_token': self._access_token,
            'expires_in': self._expires_in,
            'refresh_token': self._refresh_token
        }

    def get_user_info(self, query):
        self._check_config()
        
        params = query        
        if not type(query) is dict:
            params = self._query_to_dict(query)

        self._check_response(params)
        self._get_access_token(params)
        response = self._get_user_info()
        return self.parse_user_info(response)

    def parse_user_info(self, response):
        raise NotImplementedError('Must implement in subclass')

    def _check_response(self, params):
        if params.get('error'):
            raise OauthException(
                'Authorization failed: {0}'.format(params['error']))

        self.state = params.get('state', '')

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

    def _get_user_info(self):
        payload = {
            'access_token': self._access_token
        }
        return self.get({
            'url': self.GET_USERINFO_URL,
            'params': payload
        })
