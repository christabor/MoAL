# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from functools import wraps
from random import randrange as rr

DEBUG = True if __name__ == '__main__' else False


def _check(func, *args, **kwargs):
    @wraps(func)
    def inner(*args, **kwargs):
        x, y = args
        assert type(x) == type(y) and x is not y
        return func(*args, **kwargs)
    return inner


@_check
def xor_swap(x, y):
    x ^= y
    y ^= x
    x ^= y
    return x


if DEBUG:
    with Section('XOR Swap'):
        nums = [(rr(10, 999), rr(10, 999)) for _ in range(12)]
        for vars in nums:
            x, y = vars
            assert xor_swap(x, y) == y
            print('x: {}, y: {} => x: {}'.format(x, y, xor_swap(x, y)))
