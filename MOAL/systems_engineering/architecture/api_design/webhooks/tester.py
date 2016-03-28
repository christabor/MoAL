"""A test script for POSTing data to various webhook services."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


import time

from MOAL.helpers.display import Section
from MOAL.helpers.text import random_binary
import requests


if DEBUG:
    with Section('Webhooks - tester'):
        while True:
            time.sleep(2)
            data = random_binary(64)
            print('Posting data to :5000 ...')
            r = requests.post('http://localhost:5000/hook', data=data)
            print(r.text, r.status_code)
            print('Posting data to :5001 ...')
            r = requests.post('http://localhost:5001/hook', data=data)
            print(r.text, r.status_code)
