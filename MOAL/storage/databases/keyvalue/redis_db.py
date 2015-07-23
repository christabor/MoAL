# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_success
from MOAL.helpers.display import prnt
from MOAL.helpers.trials import run_trials
from MOAL.helpers.trials import _test_speed
from faker import Factory
from redis import Redis

DEBUG = True if __name__ == '__main__' else False

faker = Factory.create()
redis_conn = Redis(host='localhost', port=6379, db=0)
pipe = redis_conn.pipeline()

testing = {}


def insert_name(*args, **kwargs):
    key = faker.name()
    val = faker.email()
    testing[key] = val
    pipe.set(key, val)
    pipe.get(key)


@_test_speed
def insert_all(max_records):
    for n in range(max_records):
        insert_name()

if DEBUG:
    with Section('Redis (via Redis-py)'):
        run_trials(insert_all, trials=10)
        print_success('This is **too** easy!')
        # Use single pipeline for speed.
        res = pipe.execute()
        prnt('Result from Redis store pipeline execution: ', res)
