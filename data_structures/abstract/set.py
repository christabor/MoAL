# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import _print
from helpers.text import randchars
from pprint import pprint as ppr
from random import randrange as rr
from random import choice


class ImmutableSetError(Exception):
    pass


class SetADT(object):
    """
    From wikipedia.org/wiki/Set_%28abstract_data_type%29

    "The data may be booleans, numbers, characters, or other data structures.
    If one considers the structure yielded by packaging or
    indexing, there are four basic data structures:

        * unpackaged, unindexed: bunch
        * packaged, unindexed: set
        * unpackaged, indexed: string (sequence)
        * packaged, indexed: list (array)

    In this view, the contents of a set are a bunch,
    and isolated data items are elementary bunches (elements).
    Whereas sets contain elements, bunches consist of elements.
    """

    def __init__(self, items=[]):
        self.items = items
        print('<Constructor for set>')

    def __contains__(self, value):
        return value in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def __str__(self):
        for k, item in enumerate(self.items):
            print('item', item)
        return ''

    def __setitem__(self, _, value):
        if value not in self.items:
            self.items.append(value)
        else:
            print('Value already exists! {}'.format(value))


class FrozenSetADT(SetADT):

    def __init__(self, items):
        self.items = items

    def __setitem__(self, *args):
        raise ImmutableSetError


# Set types
# wikipedia.org/wiki/Set_%28abstract_data_type%29#Operations


class StaticSet(SetADT):

    def is_element_of(self, value):
        return super(StaticSet, self).__contains__(value)

    def is_empty(self, value):
        return len(self.items) == 0

    def cardinality(self):
        return super(StaticSet, self).__len__()

    def size(self):
        return super(StaticSet, self).__len__()

    def enumerate(self):
        return super(StaticSet, self).__iter__()

    @staticmethod
    def build(self, *args, **kwargs):
        return StaticSet(*args, **kwargs)

    @staticmethod
    def create_from(self, collection):
        if hasattr('__iter__', collection):
            return StaticSet(collection.values())
        return StaticSet(collection)


class DynamicSet(SetADT):

    @staticmethod
    def create(args, capacity=100):
        ds = DynamicSet(args)
        ds.capacity = capacity
        return ds

    def set_capacity(self, capacity):
        self.capacity = capacity

    def add(self, value):
        if self.room_left() == 0:
            print('No more room left!')
            return
        super(DynamicSet, self).__setitem__('', value)

    def remove(self, value):
        super(DynamicSet, self).__delitem__(value)

    def capacity(self):
        return self.capacity

    def room_left(self):
        return abs(len(self) - self.capacity)


if __name__ == '__main__':
    with Section('Set Abstract Data Type'):
        set_adt = SetADT()
        frozen_set_adt = FrozenSetADT([1, 2, 3, 4, True, False, 'A', 'B', 'C'])

        for n in range(6):
            set_adt[n] = rr(0, 10)
            set_adt[n] = ''.join(randchars(1))
            set_adt[n] = choice([True, False])
            try:
                frozen_set_adt[n] = rr(0, 10)
            except ImmutableSetError:
                print('Frozen set cannot be modified after creation.')

        _print('Set/Frozen set items', '')
        ppr(set_adt.items)
        ppr(frozen_set_adt.items)

        dynam_set = DynamicSet.create([1, 2, 3, 4], capacity=4)
        print('Capacity', dynam_set.set_capacity(4))
        print('Room left', dynam_set.room_left())
        dynam_set.add(range(100))
