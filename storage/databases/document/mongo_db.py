# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from helpers.trials import run_trials
from helpers.trials import _test_speed
from datetime import datetime as dt
from pprint import pprint as ppr
from faker import Factory
from pymongo import MongoClient


DEBUG = True if __name__ == '__main__' else False

_count = 0
_testdata = []
faker = Factory.create()
client = MongoClient()
db = client['local']
collection = db['people']


def make_person():
    return {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address(),
        'url': faker.url(),
        'created': dt.now()
    }


@_test_speed
def insert_all(max_records):
    global _count
    global _testdata
    for n in range(max_records):
        _count += 1
        data = make_person()
        _testdata.append(data['name'])
        collection.insert(data)

if DEBUG:
    with Section('MongoDB (via pymongo)'):
        # Clean up stale collection beforehand, if it exists.
        collection.remove()
        print(collection.count())
        run_trials(insert_all, trials=10)
        res = collection.find({})
        # Assert all names are correct
        mongo_res = []
        for k, item in enumerate(res):
            mongo_res.append(item['name'])
        prnt('Result from MongoDB execution, names only: ', mongo_res, func=ppr)
        # Check database count vs. local increment
        assert sorted(mongo_res) == sorted(_testdata)
        assert _count == collection.count()
