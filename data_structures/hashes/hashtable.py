# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.text import gibberish
from helpers.display import Section
from helpers.display import print_vars
from random import randrange as rr
from pprint import pprint as ppr
from uuid import uuid1

DEBUG = True if __name__ == '__main__' else False


class NaiveHashTable(object):

    def __init__(self):
        self.count = 1
        self.items = []
        # Create a new random seed to draw from when using the hash function.
        # Each one is unique to the instance, so collisions are
        # practically non-existent (though the amount of bits necessary
        # to store it is unnecessarily large.)
        self.random_seed = int(uuid1())
        if DEBUG:
            print('Random big seed for modulo: {}'.format(self.random_seed))

    def hash(self, key):
        return key % self.random_seed

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, key):
        return self.items[key]

    def __setitem__(self, key, value):
        hashkey = self.hash(key)
        if DEBUG:
            print('Inserting `{}` under hash key {}'.format(value, hashkey))
        self.items.append(value)
        self.count += 1

    def __delitem__(self, key):
        del self[key]
        self.count -= 1

    def fill_to(self, x):
        for _ in range(x):
            self.__setitem__(rr(0, 9999), gibberish(length=6))


if DEBUG:
    with Section('Naive hash tables'):
        nht = NaiveHashTable()
        keys = [rr(1, 100) for k in range(5)]
        print_vars(['Keys', keys])

        for k in keys:
            nht.fill_to(6)

        for item in nht:
            print('Reading... {}'.format(item))

        ppr(nht.items)
