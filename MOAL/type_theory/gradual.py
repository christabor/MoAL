# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
import typing


DEBUG = True if __name__ == '__main__' else False

# This program won't work unless you use the `mypy`
# (http://mypy.readthedocs.org) module and run it from that executable;
# e.g. `mypy ./gradual.py`
# Issues that might arise with mypy: https://github.com/JukkaL/mypy/issues/975
# OR, use Python 3


def greet_normal(name):
    # Regular function
    print('Hello, {}'.format(name))


def greet(name: str) -> None:
    # Type annotation version
    print('Hello, {}'.format(name))


def is_odd_normal(num):
    # Regular function
    return num % 2 == 0


def is_odd(num: int) -> bool:
    # Type annotation version
    return num % 2 == 0


class IntegerMaths:

    @staticmethod
    def add(one: int, two: int) -> int:
        return one + two

    @staticmethod
    def sub(one: int, two: int) -> int:
        return one - two

    @staticmethod
    def mod(one: int, two: int) -> int:
        return one % two

    @staticmethod
    def div(one: int, two: int) -> int:
        return one // two

    @staticmethod
    def mult(one: int, two: int) -> int:
        return one * two


if DEBUG:
    with Section('Gradual (static) type system'):
        greet('Chris')
