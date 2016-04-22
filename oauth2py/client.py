#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json


def get_configs():
    f = os.path.join(sys.path[0], 'oauth2py.json')
    if os.path.isfile(f):
        try:
            with open(f) as data:
                return json.load(data)
        except Exception, e:
            raise 'could not load configs: {0}!'.format(e)


class OauthClient(object):
    __configs = get_configs()

    def __init__(self):
        super(OauthClient, self).__init__()

    @classmethod
    def load(cls, name):
        module = OauthClient.get_class('oauth2py.{0}.{1}'.format(
            name.lower(), name.lower().capitalize()))
        client = module()

        if cls.__configs:
            cfg = next((c for c in cls.__configs
                        if c['name'].lower() == name.lower()), None)
            if cfg:
                client.init(cfg)

        return client

    @classmethod
    def reload_configs(cls):
        cls.__configs = get_configs()

    @staticmethod
    def get_class(kls):
        parts = kls.split('.')
        module = '.'.join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m
