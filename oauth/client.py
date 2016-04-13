#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


def get_class(cls):
    parts = cls.split('.')
    module = ".".join(parts[:-1])
    m = __import__(module)
    for comp in parts[1:]:
        m = getattr(m, comp)
    return m


def get_configs():
    with open('config.json') as data:
        return json.load(data)


class OauthClient(object):
    __configs = get_configs()

    def __init__(self):
        super(OauthClient, self).__init__()

    @classmethod
    def get_client(cls, name):
        module = get_class("oauth.{0}.{1}".format(
            name.lower(), name.lower().capitalize()))
        client = module()

        cfg = next(
            (c for c in cls.__configs
                if c["name"].lower() == name.lower()), None)
        if cfg:
            client.init(cfg)

        return client
