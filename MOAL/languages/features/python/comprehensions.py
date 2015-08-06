# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_h2
from MOAL.helpers.display import prnt
from MOAL.helpers import text as txt
from MOAL.helpers import datamaker as dm
from pprint import pprint as ppr
from random import choice

DEBUG = True if __name__ == '__main__' else False


def _nested(min=2, max=10):
    """Defer to a separate function - to keep things... relatively sane"""
    return [[x, y, x * y] for x, y in enumerate(range(min, max))]


def _handle(data):
    """Quick handler to help with nested tuple comprehensions -- arguments
    are not easily passed using `map`, so this deals with passing them as
    *args, since the map function won't do it automatically."""
    return prnt(*data)


if DEBUG:
    with Section('Python comprehensions'):
        prnt('Dictionary comprehension', {'data': {
            'human_to_robot': {
                dm.random_dna(): txt.random_binary(4) for _ in range(4)},
            'robot_to_human': {
                txt.random_binary(4): dm.random_dna() for _ in range(4)}}})

        prnt('List comprehension', [x ** 2 for x in range(10) if x % 2 == 0])
        prnt(
            'List comprehension - nested',
            [[x ** y for x in range(1, 4) if x % 2 == 0] for y in range(1, 8)])

        wtf = [[_nested(min=x), _nested(max=y)]
               for x, y in enumerate(range(1, 10))]
        print_h2('List comprehensions - triple nested')
        ppr(wtf)

        print_h2('Dictionary and list comprehensions, combined')
        dl_combined = {
            txt.gibberish2(): _nested(min=x, max=x * 2) for x in range(8)}
        ppr(dl_combined)

        print_h2('Set comprehension')
        set_comp = set([choice(range(100)) for _ in range(10)])
        ppr(set_comp)

        print_h2('Frozenset comprehension')
        frozen_set_comp = frozenset([choice(range(100)) for _ in range(10)])
        ppr(frozen_set_comp)

        print_h2('Tuple comprehension')
        tup = tuple((x, x * 2) for x in range(5))
        ppr(tup)

        print_h2('Tuple nested comprehension')
        tup_nest = tuple(tuple(
                        (x, x * 2) for x in range(5)) for _ in range(5))
        ppr(tup_nest)

        print_h2('Generator comprehension')
        gen = (('data:', [x, y, x ** y]) for x, y in enumerate(range(1, 5)))
        map(_handle, gen)

        print_h2('Generator nested comprehension')
        generators = ((('data:', [x, y, x ** y]) for x, y in enumerate(
                      range(1, 4))) for x in range(8))
        for generator in generators:
            print('Generator: {}'.format(generator))
            for data in generator:
                print('  {}'.format(data))
