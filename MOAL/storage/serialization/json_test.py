# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.data_structures.hashes import hash_list as hl
from faker import Factory
from datetime import datetime as dt
from pprint import pprint as ppr
from random import randrange as rr
from random import choice
import json
import umsgpack

DEBUG = True if __name__ == '__main__' else False


def make_person(omit=[]):
    val = {
        'name': faker.name(),
        'address': faker.address(),
        'url': faker.url(),
        'is_married': choice([True, False]),
        'created': '{}'.format(dt.now()),
        'age': rr(1, 99)
    }
    for _val in omit:
        if _val in val:
            val.pop(_val)
    return val


def test_pack2unpack(start):
    packed = umsgpack.packb(start)
    print('===>  Packed: {}\n===>  Unpacked: {}\n'.format(
        packed,
        umsgpack.unpackb(packed)))


faker = Factory.create()


if DEBUG:
    with Section('Data Serialization - JSON'):
        dumped = json.dumps({faker.email(): make_person() for _ in range(10)})
        print(dumped)
        ppr(json.loads(dumped))

    with Section('Data Serialization - MessagePack'):
        dumped = json.dumps([{
            faker.email(): make_person(
                omit=['created', 'url', 'address']) for _ in range(4)
        }])

        fakefile = hl.MockFile()
        hashlist = hl.HashList(fakefile.data, chunk_size=12)
        print(hashlist)

        testers = [
            {"foo": True, "bar": [True, False]},
            dumped,
            [chr(n) for n in range(10)],
            [[chr(n), n, n * n, n ** n] for n in range(10)],
        ]

        for tester in testers:
            test_pack2unpack(tester)

        for k in range(10):
            _k = k ** k
            orig = str(_k).encode('utf-8')
            packed = umsgpack.packb(orig)
            test_pack2unpack(packed)
            unpacked = umsgpack.unpackb(packed)
            assert orig == unpacked
            print(orig, umsgpack.packb(orig),
                  umsgpack.unpackb(umsgpack.packb(orig)))
