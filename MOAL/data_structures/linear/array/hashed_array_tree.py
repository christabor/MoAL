# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_simple

DEBUG = True if __name__ == '__main__' else False


class HashedArrayTree:

    # See http://www.drdobbs.com/database/algorithm-alley/184409965?pgno=5
    # for details.

    def __init__(self):
        self.top = []
        self.count = 0

    def add_leaf(self, leaves):
        if len(self.top) + leaves % 2 != 0:
            raise ValueError('Leaf count must be a power of 2!')
        for n in range(leaves):
            self.count += 1
            self.top.append([])

    def add(self, leaf, items):
        if len(self.top[leaf]) + len(items) % 2 != 0:
            raise ValueError('Items count not a power of 2')
        self.top[leaf] += items

    def __str__(self):
        return '[{}]'.format(', '.join(map(str, self.top)))


if DEBUG:
    with Section('Hashed array tree'):
        hat = HashedArrayTree()
        hat.add_leaf(4)
        print_simple('HAT', hat)
        try:
            hat.add(1, ['foo', 'bar', 'bim', 'baz', 'bim'])
        except ValueError:
            print('- Prevented unexpected value.')
            hat.add(1, ['foo', 'bar', 'bim', 'baz'])
        hat.add(2, ['foo', 'baz'])
        print(hat)
