#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base
from exceptions import OauthException


class Oauth2(Base):

    def __init__(self):
        super(Oauth2, self).__init__()

    def get_login_url(self, state=''):
        self._check_config()

        params = {
            'client_id': self._config['client_id'],
            'redirect_uri': self._config['redirect_uri'],
            'response_type': 'code'
        }

        if self._config['scope']:
            params['scope'] = self._config['scope']

        if state:
            params['state'] = state

        return self._build_request_uri({
            'url': self.AUTHORIZATION_URL,
            'params': params
        })

    def get_access_token(self, refresh_token=''):
        """access_token, or use refresh_token update access_token."""
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

    def parse_token_response(self, response):
        self._access_token = response.get('access_token', '')
        self._expires_in = response.get('expires_in', '')
        self._refresh_token = response.get('refresh_token', '')

    def get_user_info_params(self):
        return {
            'access_token': self._access_token
        }

    def parse_user_info(self, response):
        raise NotImplementedError('Must implement in subclass')

    def set_access_token(self, access_token):
        self._access_token = access_token['access_token']
        self._expires_in = access_token.get('expires_in')

    def access_resource(self, method, url, params={}, data={}):
        self._check_config()

        params['access_token'] = self._access_token

        r = None
        if method.lower() == 'get':
            r = self._get({
                'url': url,
                'params': params
            })
        elif method.lower() == 'post':
            r = self._post({
                'url': url,
                'params': params,
                'data': data
            })
        else:
            r = self._request({
                'method': method,
                'url': url,
                'params': params,
                'data': data
            })

        return r

    def _check_response(self, params):
        if params.get('error', ''):
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

        r = self._post({
            'url': self.ACCESS_TOKEN_URL,
            'data': params
        })

        self.parse_token_response(r)

    def _get_user_info(self):
        params = self.get_user_info_params()
        return self._get({
            'url': self.GET_USERINFO_URL,
            'params': params
        })
