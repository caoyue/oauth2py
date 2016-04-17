#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from exceptions import AuthorizeException


class Base(object):
    NAME = ''
    AUTHORIZATION_URL = ''
    ACCESS_TOKEN_URL = ''
    GET_USERINFO_URL = ''

    _config = {}

    _access_token = ''
    _expires_in = ''
    _refresh_token = ''

    state = ''

    def init(self, config):
        self._config = config

    def get_config(self):
        return self._config

    def get_login_url(self):
        raise NotImplementedError('Must implement in subclass')

    def get_user_info(self):
        raise NotImplementedError('Must implement in subclass')

    def build_request_uri(self, request):
        params = '&'.join(
            ['{0}={1}'.format(x, y)
             for x, y in request['params'].iteritems()])
        return '{0}?{1}'.format(request['url'], params)

    def get(self, request):
        r = None
        try:
            r = requests.get(request['url'],
                             params=request['params'],
                             headers={'Accept': 'application/json'})
        except requests.ConnectionError, e:
            raise AuthorizeException('Connection error: {0}'.format(e))
        else:
            if r.status_code != 200:
                raise AuthorizeException(
                    'Authorization failed: {0}'.format(r.json()))

        return r.json()

    def post(self, request):
        r = None
        try:
            r = requests.post(request['url'],
                              data=request['params'],
                              headers={'Accept': 'application/json'})
        except requests.ConnectionError, e:
            raise AuthorizeException('Connection error: {0}'.format(e))
        else:
            if r.status_code != 200:
                raise AuthorizeException(
                    'Authorization failed: {0}'.format(r.json()))

        return r.json()

    def _query_to_dict(self, query):
        return {x.split('=')[0]: x.split('=')[1]
                for x in query.split('&')}

    def _check_config(self):
        if not self._config:
            raise AuthorizeException('Oauth client config not set')
