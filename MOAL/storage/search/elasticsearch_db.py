# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from MOAL.helpers.trials import test_speed
from faker import Factory
from datetime import datetime as dt
from elasticsearch import Elasticsearch

DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()
es = Elasticsearch()


def get_name():
    return {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address(),
        'timestamp': dt.now(),
    }


@test_speed
def insert_all(max_records):
    for n in range(max_records):
        res = es.index(
            index='testing_index', doc_type='test',
            id=n, body=get_name())
        print(res)

if DEBUG:
    with Section('ElasticSearch (via ElasticSearch-py)'):
        insert_all(10)
        res = es.get(index='testing_index', doc_type='test', id=1)
        prnt('ES Results:', res)
