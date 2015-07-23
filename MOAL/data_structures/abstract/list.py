# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.text import randchars


class ListADT(object):
    """
    From wikipedia.org/wiki/List_%28abstract_data_type%29#Operations
    "
    Implementation of the list data structure may
    provide some of the following operations:

        * a constructor for creating an empty list;
        * an operation for testing whether or not a list is empty;
        * an operation for prepending an entity to a list
        * an operation for appending an entity to a list
        * an operation for determining the first component
            (or the "head") of a list
        * an operation for referring to the list consisting of all the
            components of a list except for its first
            (this is called the "tail" of the list.)
    "
    """
    def __init__(self):
        self.items = []
        print('<Constructor for list>')

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        for k, item in enumerate(self.items):
            print('item', item)
        return ''

    @staticmethod
    def create(self, *args, **kwargs):
        self.__init__(self, *args, **kwargs)

    def tail(self):
        return self.items[1:]

    def head(self):
        return self.items[0]

    def empty(self):
        return len(self.items) == 0

    def prepend(self, item):
        self.items.insert(0, item)

    def append(self, item):
        self.items.append(item)


if __name__ == '__main__':
    with Section('List Abstract Data Type'):
        list_adt = ListADT()
        for n in range(4):
            list_adt.prepend(randchars(n))
            list_adt.append(randchars(n))

        print(list_adt)
        print('List ADT head', list_adt.head())
        print('List ADT tail', list_adt.tail())
        print('List ADT empty?', list_adt.empty())
