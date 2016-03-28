# -*- coding: utf-8 -*-

"""Functional python using functools stdlib."""

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import functools
from pprint import pprint as ppr

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.datamaker import random_person_full


DEBUG = True if __name__ == '__main__' else False


def cmp_people_lname(val1, val2):
    """Old school comparison function. LT = -1, EQ = 0, GT = 1"""
    if val1['lname'] == val2['lname']:
        return 0
    if val1['lname'] > val2['lname']:
        return 1
    else:
        return -1


def cmp_people_fname(val1, val2):
    """Old school comparison function. LT = -1, EQ = 0, GT = 1"""
    if val1['fname'] == val2['fname']:
        return 0
    if val1['fname'] > val2['fname']:
        return 1
    else:
        return -1


@functools.total_ordering
class Person(object):

    def __init__(self):
        self.person = random_person_full()

    def __eq__(self, other):
        return self.person['lname'] == other.person['lname']

    def __lt__(self, other):
        return self.person['lname'] < other.person['lname']


def _mult_tup(x, y):
    t1, t2 = y
    return t1 * t2


def _concat(x, y):
    return x + y


def greet(name, greeting='', prefix=''):
    """Greet func."""
    prefix = '{} '.format(prefix) if prefix else ''
    return '{}, {}{}'.format(greeting, prefix, name)


def helloer():
    """Helloer func."""
    return functools.partial(greet, greeting='Hello')


def halloer():
    """Halloer func."""
    return functools.partial(greet, greeting='Hallo mein freuden')


def halloer_male():
    """Halloer func."""
    return functools.partial(
        greet, prefix='Herr', greeting='Hallo mein freuden')


def halloer_female():
    """Halloer func."""
    return functools.partial(
        greet, prefix='Frau', greeting='Hallo mein freuden')


if DEBUG:
    with Section('Functional programming with itertools'):
        print_h2('cmp_to_key')
        p1 = random_person_full()
        p2 = random_person_full()

        resfirst = sorted([p1, p2], cmp_people_fname)
        reslast = sorted([p1, p2], cmp_people_lname)

        ft_resfirst = sorted(
            [p1, p2], key=functools.cmp_to_key(cmp_people_fname))
        ft_reslast = sorted(
            [p1, p2], key=functools.cmp_to_key(cmp_people_lname))

        ppr([resfirst, reslast])
        ppr([ft_resfirst, ft_reslast])

        print_h2('total_ordering')

        p1 = Person()
        p2 = Person()
        print(p1 == p2)
        print(p1 < p2)
        # Check other methods were populated automatically
        print(p1 > p2)
        print(p1 >= p2)

        print_h2('reduce')

        f = range(10, 20)
        g = range(100, 200)
        h = zip(f, g)

        print(h)
        print(functools.reduce(_mult_tup, h))

        strings = ['hello', 'world', 'how', 'are', 'you', '?']
        assert functools.reduce(_concat, strings) == 'helloworldhowareyou?'

        print_h2('partial')

        print(helloer()('Chris'))
        print(halloer()('Kristoff'))

        print(halloer_male()('Kristoff'))
        print(halloer_female()('Ada'))

        print_h2('Wraps - see various MOAL decorators for usage.')
