"""HTTP/2 Testing."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
import requests


if DEBUG:
    with Section('HTTP/2'):
        res = requests.get('https://127.0.0.1:8001', verify=False)
        print('<Response: {}>: {}'.format(res.status_code, res.content))
        assert res.content == "Hello, here's some lovely Http/2!"
