oauth2py
~~~~~~~~

| |PyPI version|
| |Build Status|
| |Coverage Status|

a simple, lightweight oauth client

require
~~~~~~~

python 2.7

supported
~~~~~~~~~

-  [x] Weibo
-  [x] QQ
-  [x] Facebook
-  [x] Github
-  [x] Twitter
-  [ ] Other…

useage
~~~~~~

#. create client

   -  put ``oauth2py.json`` in your app root folder

   .. code:: json

       [{
           "name": "github",
           "client_id": "",
           "client_secret": "",
           "redirect_uri": "",
           "scope": ""
       },
       {
           "name": "twitter",
           "client_id": "",
           "client_secret": "",
           "redirect_uri": "",
           "scope": ""
       }]

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

#. oauth

   #. get login url

   .. code:: python

       url = github.get_login_url(state='abc')

   #. get user info

   .. code:: python

       user = github.get_user_info('code=12345&state=abc')
       # or
       user = github.get_user_info({'code': '12345', 'state': 'abc'})

   #. save access token

   .. code:: python

       token = github.get_access_token()
       # save token ...

#. access resource

   -  get github repo list

   .. code:: python

       github.set_access_token({
           'access_token': '...'
       })
       github.access_resource(
               'GET', 'https://api.github.com/user/repos')

   -  another example: post status to twitter

   .. code:: python

       twitter.set_access_token({
               'access_token': '...',
               'access_token_secret': '...'
           }
       )
       twitter.access_resource(
           'POST',
           url='https://api.twitter.com/1.1/statuses/update.json',
           data={
               'status': 'test from oauth2py!'
           }
       )

implement new providers
~~~~~~~~~~~~~~~~~~~~~~~

-  inherit ``oauth2py.Oauth2`` or ``oauth2py.Oauth`` and set oauth urls

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
               'uid': str(response.get('id')),
               'name': response.get('name'),
               'avatar': response.get('avatar_url'),
               'raw': response
           }


.. |PyPI version| image:: https://img.shields.io/pypi/v/oauth2py.svg?style=flat
   :target: https://pypi.python.org/pypi/oauth2py
.. |Build Status| image:: https://img.shields.io/travis/shadowsocks/shadowsocks/master.svg?style=flat
   :target: https://travis-ci.org/caoyue/oauth2py
.. |Coverage Status| image:: https://coveralls.io/repos/github/caoyue/oauth2py/badge.svg?branch=master
   :target: https://coveralls.io/github/caoyue/oauth2py?branch=master
