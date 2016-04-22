#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base
from requests_oauthlib import OAuth1
from exceptions import AuthorizeException


class Oauth(Base):

    def __init__(self):
        super(Oauth, self).__init__()

    def get_login_url(self):
        self._check_config()
        self._request_token = self._get_request_token()
        return '{0}?oauth_token={1}'.format(
            self.AUTHENTICATE_URL,
            self._request_token['oauth_token']
        )

    def get_request_token(self):
        return self._request_token

    def get_access_token(self, verifier=''):
        if verifier:
            oauth = OAuth1(
                client_key=self._config['client_id'],
                client_secret=self._config['client_secret'],
                callback_uri=self._config['redirect_uri'],
                resource_owner_key=self._request_token['oauth_token'],
                resource_owner_secret=self._request_token[
                    'oauth_token_secret'],
                verifier=verifier
            )

            r = self._post({
                'url': self.ACCESS_TOKEN_URL,
                'auth': oauth
            })
            q = self._query_to_dict(r)
            self._access_token = q['oauth_token']
            self._access_token_secret = q['oauth_token_secret']

        return {
            'access_token': self._access_token,
            'access_token_secret': self._access_token_secret
        }

    def get_user_info(self, query, request_token={}):
        params = query
        if not type(query) is dict:
            params = self._query_to_dict(query)

        if request_token:
            self._request_token = request_token

        self._check_response(params)
        self._get_access_token(params)

        oauth = OAuth1(
            client_key=self._config['client_id'],
            client_secret=self._config['client_secret'],
            callback_uri=self._config['redirect_uri'],
            resource_owner_key=self._access_token,
            resource_owner_secret=self._access_token_secret
        )

        r = self._get({
            'url': self.GET_USERINFO_URL,
            'auth': oauth
        })
        return self.parse_user_info(r)

    def parse_user_info(self, response):
        raise NotImplementedError('Must implement in subclass')

    def set_access_token(self, access_token):
        self._access_token = access_token['access_token']
        self._access_token_secret = access_token['access_token_secret']

    def access_resource(self, method, url, params={}, data={}):
        self._check_config()

        oauth = OAuth1(
            client_key=self._config['client_id'],
            client_secret=self._config['client_secret'],
            callback_uri=self._config['redirect_uri'],
            resource_owner_key=self._access_token,
            resource_owner_secret=self._access_token_secret
        )

        r = None
        if method.lower() == 'get':
            r = self._get({
                'url': url,
                'params': params,
                'auth': oauth
            })
        elif method.lower() == 'post':
            r = self._post({
                'url': url,
                'params': params,
                'data': data,
                'auth': oauth
            })
        else:
            r = self._request({
                'method': method,
                'url': url,
                'params': params,
                'data': data,
                'auth': oauth
            })

        return r

    def _check_response(self, params):
        if params.get('error', ''):
            raise AuthorizeException(
                'Authorization failed: {0}'.format(params['error']))

    def _get_request_token(self):
        oauth = OAuth1(
            client_key=self._config['client_id'],
            client_secret=self._config['client_secret'],
            callback_uri=self._config['redirect_uri'],
        )
        r = self._post({
            'url': self.REQUEST_TOKEN_URL,
            'auth': oauth
        })
        return self._query_to_dict(r)

    def _get_access_token(self, params):
        return self.get_access_token(params['oauth_verifier'])
