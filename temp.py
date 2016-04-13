#!/usr/bin/env python
# -*- coding: utf-8 -*-

from oauth.client import OauthClient

if __name__ == '__main__':
    c = OauthClient.get_client("facebook")
    print c.get_login_url()

    print c.get_user_info("code=AQA4vlHU6ArE7VcMUffZftUxqYfyvWoEXsMf0IhlAzqRbeE06pVc0LxBI3EzmoRcdro9mIaSY2KxRyjtAGGrFRJRkt9JJceM15gXs6MGmVz77hsvhRm2RrOL3DVySZmmQl_7sS58t2sXhAY7eElz9AadZ-b0GAI6KyZfvrhufxStxCchqenABbtOcPL7dgn4BrXfHM14ht41bC9cwgSVLqKkIfP4UVjCEeG8vBi7TExocO7fR6Vdos5bdysN7hPyWeK7KaaswgRcElIFLRRJnyka1T0e4oS3lu97Us2_yv3kGiCSXgOzSKaKkqIrAQdPQAiHkIFhZQTfwMRcxxPjdQS5#_=_")
