#!/usr/bin/env python
# -*- coding: utf-8 -*-

from base import Base


class Oauth(Base):

    def __init__(self):
        super(Oauth, self).__init__()

    def get_login_url(self):
        payload = {
            "client_id": config.client_id,
            "redirect_uri": config.redirect_uri,
            "scope": config.scope
        }
        if state:
            payload["state"] = state

        return self.self.build_request_uri({
            url: self.ACCESS_TOKEN_URL,
            params: payload
        })
