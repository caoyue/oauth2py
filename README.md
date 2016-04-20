
### oauth2py
[![PyPI version]][PyPI]
[![Build Status]][Travis CI]

a simple, lightweight oauth client

### require

python 2.7

### supported
- [x] Weibo
- [ ] QQ
- [x] Facebook
- [x] Github
- [x] Twitter
- [ ] Other...

### useage
1. create client
    - put `oauth2py.config.json` in your app folder

    ```python
    from oauth2py.client import OauthClient as oauth

    github = oauth.load('github')
    ```
    - or set config in code

    ```python
    github.init({
        'client_id': '',
        'client_secret': '',
        'redirect_uri': '',
        'scope': ''
    })
    ```

2. get login url

    ```python
    url = github.get_login_url(state='abc')
    ```

3. get user info

    ```python
    user = github.get_user_info('code=12345&state=abc')
    # or
    user = github.get_user_info({'code': '12345', 'state': 'abc'})
    ```

4. get access token

    ```python
    token = github.get_access_token()
    ```

### add providers
- inherit `oauth2py.Oauth2` and set oauth urls

    ```python
    class Github(Oauth2):

        NAME = 'Github'
        AUTHORIZATION_URL = 'https://github.com/login/oauth/authorize'
        ACCESS_TOKEN_URL = 'https://github.com/login/oauth/access_token'
        GET_USERINFO_URL = 'https://api.github.com/user'

        def __init__(self):
            super(Github, self).__init__()

    ```

- parse user info from response

    ```python
    def parse_user_info(self, response):
        return {
            'uid': response['id'],
            'name': response['name'],
            'avatar': response['avatar_url'],
            'raw': response
        }
    ```


[PyPI]:              https://pypi.python.org/pypi/oauth2py
[PyPI version]:      https://img.shields.io/pypi/v/oauth2py.svg?style=flat
[Build Status]:      https://img.shields.io/travis/shadowsocks/shadowsocks/master.svg?style=flat
[Travis CI]:         https://travis-ci.org/caoyue/oauth2py
