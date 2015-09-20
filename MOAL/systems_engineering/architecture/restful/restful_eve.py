# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.datamaker import random_person
from random import choice
from string import uppercase as uc
from random import randrange as rr
from eve import Eve
import sys
import os
import json

DEBUG = True if __name__ == '__main__' else False

app = Eve()


"""
See settings.py in this folder for the brunt of the code
-- most everything is done via configuration!"""


def _random_person():
    person = random_person()
    return {'name': person['name']}


def _random_robot():
    return {'model': '{}{}-{}'.format(choice(uc), choice(uc), rr(0, 9999))}


def _curl_post(endpoint, data):
    os.system("curl -d '{}' -H 'Content-Type: application/json' "
              "localhost:5000/{}".format(json.dumps(data), endpoint))


def setup_fixtures(max=10):
    """Use the super simple Eve api to generate fixtures via curl"""
    for _ in range(max):
        _curl_post('person', _random_person())
        _curl_post('robot', _random_robot())
        _curl_post('cyborg', _random_person())


if DEBUG:
    with Section('RESTful API - using Eve'):
        # Run app or load data
        if '--data' in sys.argv:
            setup_fixtures()
        else:
            app.run()
