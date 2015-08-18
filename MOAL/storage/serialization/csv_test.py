# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from faker import Factory
from datetime import datetime as dt
from random import randrange as rr
import csv

DEBUG = True if __name__ == '__main__' else False


def make_person():
    return {
        'name': faker.name(),
        'email': faker.email(),
        'address': faker.address(),
        'url': faker.url(),
        'created': dt.now(),
        'age': rr(1, 99)
    }


faker = Factory.create()


if DEBUG:
    with Section('Data Serialization - CSV'):
        # Write
        with open('fakecsv.csv', 'w') as csvfile:
            fields = make_person().keys()
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            writer.writeheader()

            for _ in range(100):
                writer.writerow(make_person())

        # Then read
        with open('fakecsv.csv', 'rb') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                print('Row: {}'.format(row))
