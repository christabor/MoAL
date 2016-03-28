"""A vanilla app for interacting with POST requests as hooks."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import json

from flask import (
    Flask,
    request,
)
from MOAL.helpers.display import Section
from MOAL.helpers.text import random_binary


app = Flask('webhook-app2')
app.debug = True


@app.route('/hook', methods=['GET', 'POST'])
def index():
    """Hook index."""
    if request.method == 'GET':
        return 'hello, I am app2 - please send me a webhook.'
    else:
        return json.dumps(dict(
            message='App 2 - Message received, sending hook data',
            status=200,
            data=random_binary(12)))


if DEBUG:
    with Section('Webhooks - app2'):
        app.run(host='0.0.0.0', port=5001)
