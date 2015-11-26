# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import divider
from MOAL.helpers.trials import run_trials
from MOAL.helpers.trials import test_speed
from datetime import datetime as dt
from faker import Factory
import couchdb
from pprint import pprint as ppr


DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()
couch = couchdb.Server()

try:
    test_db = couch.create('test_db')
except couchdb.http.PreconditionFailed:
    couch.delete('test_db')
    test_db = couch.create('test_db')


def make_person():
    return {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address(),
        'url': faker.url(),
        'created': str(dt.now())
    }


@test_speed
def insert_all(max_records):
    for n in range(max_records):
        test_db.save(make_person())


if DEBUG:
    with Section('CouchDB (via python-couchdb)'):
        run_trials(insert_all, trials=10)
        print_h2('Result from CouchDB execution: ')
        for res in test_db:
            divider()
            ppr(test_db[res])
