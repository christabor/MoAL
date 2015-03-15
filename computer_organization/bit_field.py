# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h3
from bitarray import bitarray

DEBUG = True if __name__ == '__main__' else False


class BitField(object):
    """A set of bit representations as booleans, used as a field/structure."""

    def __init__(self):
        # pypi.python.org/pypi/bitarray/
        self.fields = bitarray()

    def __getitem__(self, key):
        return self.fields.decode(key)

    def __delitem__(self, key):
        self.fields.remove(key)

    def __setitem__(self, key, bitvalue):
        code = {str(value): bitarray(True) for value in list(key)}
        self.fields.encode(code, key)

    def __str__(self):
        print('Bit field')
        for field in self.fields:
            print('Field: {}'.format(field))
        return ''


class FlagField(BitField):
    """Using bit field as a set of flags, e.g. options, boolean values, etc"""
    pass


if __name__ == '__main__':
    with Section('Computer organization - Bit field/flag field'):
        print_h3(
            'A bit field/flag field class representation',
            desc='Using bitarray C/Python library')
        user_flags = FlagField()
        user_flags['foo'] = 1
        user_flags['bar'] = 1

        print(user_flags)
