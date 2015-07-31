# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.text import gibberish
from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class NaiveHashTable(object):

    def __init__(self):
        self.count = 1
        self.max_capacity = 100
        self.items = []

    def _naive_hash_value(self, val):
        """Compute an integer signature relative to the value given. This
        is very naive and will result in collisions in a short matter of time.
        Only here for demo purposes, as this data structure is not performant
        for production use."""
        val = str(val)
        _key = ''
        for v in list(val):
            _key += str(ord(v))
        return int(_key)

    def hash(self, key):
        """Super naive hashing function - collisions are highly probable."""
        return self._naive_hash_value(key) % self.max_capacity

    def __iter__(self):
        return iter(self.items)

    def __getitem__(self, key):
        return self.items[self.hash(key)]

    def __setitem__(self, key, value):
        hashkey = self.hash(key)
        if DEBUG:
            print('Inserting `{}` under hash key {} with value: {}'.format(
                key, hashkey, value))
        # Expand the list into a sparse array to store keys.
        if hashkey > len(self.items):
            self.items += range(len(self.items), hashkey)
        # Insert the value at the right key location.
        self.items.insert(hashkey, value)

    def __delitem__(self, key):
        del self.items[key]

    def fill_to(self, x):
        for _ in range(x):
            self.__setitem__(gibberish(length=3), gibberish(length=6))


if DEBUG:
    with Section('Naive hash tables'):
        nht = NaiveHashTable()
        nht.fill_to(4)

        nht['Foo'] = 'TEST'
        nht['Bar'] = 'TEST'
        nht['TEST'] = 'Bar'

        # Test strings
        assert nht['Foo'] == 'TEST'
        assert nht['Bar'] == 'TEST'
        assert nht['TEST'] == 'Bar'

        # Test integers
        nht[12] = 'Testnum'
        assert nht[12] == 'Testnum'
