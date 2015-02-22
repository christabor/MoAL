# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.text import gibberish
from helpers.display import Section
from random import randrange as rr
from pprint import pprint as ppr


class NaiveHashTable:

    def __init__(self):
        self.max = 50
        self.items = [[] for x in range(self.max)]

    def hash(self, key):
        return key % self.max

    def insert(self, key, value):
        print('Inserting {} = {} under key {}'.format(
            key, value, self.hash(key)))
        self.items[self.hash(key)].append(value)


def fill_blocks_to(x):
    for _ in range(x):
        nht.insert(rr(0, x), gibberish(length=6))


if __name__ == '__main__':
    with Section('Naive hash tables'):
        nht = NaiveHashTable()
        keys = [rr(0, 30) for k in range(5)]
        print(keys)

        for k in keys:
            fill_blocks_to(40)

        for k in keys:
            print('Reading... {}'.format(nht.items[k]))

        ppr(nht.items)
