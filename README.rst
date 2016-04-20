oauth2py
~~~~~~~~

|PyPI version| |Build Status|

a simple, lightweight oauth client

require
~~~~~~~

python 2.7

supported
~~~~~~~~~

-  [x] Weibo
-  [ ] QQ
-  [x] Facebook
-  [x] Github
-  [ ] Twitter
-  [ ] Other…

useage
~~~~~~

#. create client

    -  put ``config.json`` in your app folder

    .. code:: python

        from oauth2py.client import OauthClient as oauth

        github = oauth.load('github')

    -  or set config in code

    .. code:: python

        github.init({
            'client_id': '',
            'client_secret': '',
            'redirect_uri': '',
            'scope': ''
        })

#. get login url

    .. code:: python

        url = github.get_login_url(state='abc')

#. get user info

    .. code:: python

        user = github.get_user_info('code=12345&state=abc')
        # or
        user = github.get_user_info({'code': '12345', 'state': 'abc'})

#. get access token

    .. code:: python

        token = github.get_access_token()

add providers
~~~~~~~~~~~~~

-  inherit ``oauth2py.Oauth2`` and set oauth urls

    .. code:: python

        class Github(Oauth2):

            NAME = 'Github'
            AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
            ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
            GET_USERINFO_URL = 'https://api.github.com/user'

            def __init__(self):
                super(Github, self).__init__()

-  parse user info from response

    .. code:: python

        def parse_user_info(self, response):
            return {
                'uid': response['id'],
                'name': response['name'],
                'avatar': response['avatar_url'],
                'raw': response
            }

.. |PyPI version| image:: https://img.shields.io/pypi/v/oauth2py.svg?style=flat
   :target: https://pypi.python.org/pypi/oauth2py
.. |Build Status| image:: https://img.shields.io/travis/shadowsocks/shadowsocks/master.svg?style=flat
   :target: https://travis-ci.org/caoyue/oauth2py