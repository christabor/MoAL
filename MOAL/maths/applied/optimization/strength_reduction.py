#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""


__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.trials import test_speed

DEBUG = True if __name__ == '__main__' else False


"""Strength reduction is an optimization technique that involves taking
a more 'advanced' math technique and breaking it down into simple 'dumb' tasks
that can be repeated.

For example, multiplication can be converted to lots of addition."""


@test_speed
def exp(x, power):
    # 4^3
    # ... 4 * 4 * 4
    res = x
    for num in [x] * power:
        res = num * res
    return res


@test_speed
def strengthreduced_exp(x, power):
    # Replaces an exponential operation with a multiplication + addition
    # 4^3 = 64
    # ... 4 * 4 * 4 = 64
    # ... 2 + 2 + 2 + 2 + 2 ... (32 times) = 64
    res = x
    for num in [x] * power:
        res = strengthreduced_mult(num, res)
    return res


@test_speed
def mult(x, y):
    return x * y


@test_speed
def strengthreduced_mult(x, y):
    # 2 * 4 = 8
    # ... 2 + 2 + 2 + 2 = 8
    res = 0
    for f in xrange(y):
        res += x
    return res


if DEBUG:
    with Section('Optimization - strength reduction'):
        # This is slower since the native multiplication is much much faster
        # than looping, but it demonstrates the idea.
        max = 200
        f, g = exp(4, 2), strengthreduced_exp(4, 2)
        assert f == g
        print(f, g)

        f2, g2 = mult(2, 4), strengthreduced_mult(2, 4)
        assert f2 == g2
        print(f2, g2)
