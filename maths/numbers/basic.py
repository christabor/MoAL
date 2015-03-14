# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from random import randrange as rr
from fractions import Fraction
from decimal import Decimal
from decimal import getcontext


def wholes(max_nums):
    for n in range(0, max_nums):
        yield n
    raise StopIteration


def naturals(max_nums):
    for n in range(1, max_nums):
        yield n
    raise StopIteration


def integers(max_nums):
    for n in range(0, max_nums):
        yield n, -n
    raise StopIteration


def rationals(max_nums):
    """Doesn't cover entirety of the rationals, just an example subset"""
    for n in range(0, max_nums):
        try:
            rand_example = rr(0, max_nums ** n)  # Make things interesting
            yield float(n) / float(rand_example), n, Fraction(n, rand_example)
        except ZeroDivisionError:
            yield 0,
    raise StopIteration


def irrationals(max_nums):
    """Doesn't cover entirety of the irrationals, just an example subset"""
    getcontext().prec = 20
    for n in range(1, max_nums):
        res = Decimal(n).sqrt()
        if len(str(res)) > 1:  # Rationals will be rounded off
            yield res
    raise StopIteration


def reals(max_nums):

    def _range(generator):
        for n in generator:
            print(n)

    yield (_range(wholes(max_nums)),
           _range(naturals(max_nums)),
           _range(integers(max_nums)),
           _range(rationals(max_nums)),
           _range(irrationals(max_nums)))
    yield '\n'

if __name__ == '__main__':
    with Section('Basic number sets'):
        MAX_NUMS_PER_EXAMPLE = 10

        prnt('Naturals', '')
        for n in naturals(MAX_NUMS_PER_EXAMPLE):
            print(n)

        prnt('Integers', '')
        for n in integers(MAX_NUMS_PER_EXAMPLE):
            print(n)

        prnt('Rationals', '')
        for n in rationals(MAX_NUMS_PER_EXAMPLE):
            print(n)

        prnt('Irrationals', '')
        for n in irrationals(MAX_NUMS_PER_EXAMPLE):
            print(n)

        prnt('Reals', '')
        for n in reals(MAX_NUMS_PER_EXAMPLE):
            print(n)
