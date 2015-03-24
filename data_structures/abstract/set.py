# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h4
from helpers.text import randchars
from pprint import pprint as ppr
from random import randrange as rr
from random import choice

DEBUG = True if __name__ == '__main__' else False


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
    Whereas sets contain elements, bunches consist of elements."""

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


class MultiSet(DynamicSet):

    def __setitem__(self, group, values):
        """Sets a single item in a multi-set group. Each group can be queried
        by individual values, but multiple values can be stored.
        e.g. mymset['foo'] = {'bar': 2, 'bim': True} ... myset.count('bar') == 1
        """
        val = {group: True}
        val.update(values)
        self.items.append(val)

    def count_multi(self, props, key=None):
        """Count multiple properties."""
        _count = 0
        for prop in props:
            _count += self.count(prop, key=key)
        return _count

    def count(self, prop, key=None):
        """Check the count of any given property or key (either scenario works
            seamlessly for ease-of-use) and user simplicity."""
        _count = 0
        for item in self:
            # Allow any data to be set, but transparently check any hash values
            # and fail silently if the value is not a dictionary.
            try:
                if key is not None:
                    # If key is set, use that to check for the property,
                    # otherwise count based on number of properties.
                    try:
                        if item[key] == prop:
                            _count += 1
                    except KeyError:
                        # Scenario: key was given, but it doesn't exist here.
                        continue
                else:
                    if prop in item:
                        _count += 1
            except TypeError:
                continue
        if DEBUG:
            print('Count = {} for property {}'.format(_count, prop))
        return _count


if DEBUG:
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

        print_h4('Set/Frozen set items', '')
        ppr(set_adt.items)
        ppr(frozen_set_adt.items)

        dynam_set = DynamicSet.create([1, 2, 3, 4], capacity=4)
        print('Capacity', dynam_set.set_capacity(4))
        print('Room left', dynam_set.room_left())
        dynam_set.add(range(100))

        print_h4('Multiset example', 'Allowing multiple items of the same')
        multiset = MultiSet()
        multiset['cat'] = {'name': 'lily', 'type': 'persian'}
        multiset['cat'] = {'name': 'radical', 'type': 'calico', 'age': 23}
        multiset['cat'] = {'name': 'jadore', 'type': 'siamese'}
        multiset['cat'] = {'name': 'tutu', 'type': 'abyssinian'}

        assert multiset.count('cat') == 4
        assert multiset.count(23, key='age') == 1
        assert multiset.count('tutu', key='name') == 1
