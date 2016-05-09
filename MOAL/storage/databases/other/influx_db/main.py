"""InfluxDb tester."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

IS_MAIN = True if __name__ == '__main__' else False

if IS_MAIN:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from datetime import datetime as dt
from random import random, choice

from influxdb import InfluxDBClient
from MOAL.helpers.display import Section


def make_data(client):
    i = 0
    while True:
        json_body = [
            {
                'measurement': 'cpu_load_short',
                'tags': {
                    'host': 'server-{}'.format(i),
                    'region': 'us-{}'.format(
                        choice(['east', 'west', 'north', 'south']))
                },
                'time': dt.now(),
                'fields': {
                    'value': random(),
                    'value2': random(),
                }
            },
            {
                'measurement': 'hdd_load_short',
                'tags': {
                    'host': 'server-{}'.format(i),
                    'region': 'us-{}'.format(
                        choice(['east', 'west', 'north', 'south']))
                },
                'time': dt.now(),
                'fields': {
                    'size': choice(['1TB', '4TB', '8TB', '16TB', '32TB']),
                    'value': random(),
                    'value2': random(),
                }
            }
        ]
        i += 1
        yield client.write_points(json_body)


if IS_MAIN:
    with Section(__doc__):
        client = InfluxDBClient('localhost', 8086, 'root', 'root', 'moaltest')
        client.create_database('moaltest')
        d = make_data(client)
        for _ in range(100):
            next(d)

        result = client.query('select * from cpu_load_short;')
        print('Result: {0}'.format(result))

        result = client.query('select * from hdd_load_short;')
        print('Result: {0}'.format(result))
