
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
    - put `oauth2py.json` in your app root folder

    ```json
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
    ```

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
2. oauth
    1. get login url

    ```python
    url = github.get_login_url(state='abc')
    ```

    2. get user info

    ```python
    user = github.get_user_info('code=12345&state=abc')
    # or
    user = github.get_user_info({'code': '12345', 'state': 'abc'})
    ```

    3. save access token

    ```python
    token = github.get_access_token()
    # save token ...
    ```

3. access resource
    - get github repo list
    ```python
    github.set_access_token({
        'access_token': '...'
    })
    github.access_resource(
            'GET', 'https://api.github.com/user/repos')
    ```

    - another example: post status to twitter

    ```python
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
    ```

### implement new providers
- inherit `oauth2py.Oauth2` or `oauth2py.Oauth` and set oauth urls

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
