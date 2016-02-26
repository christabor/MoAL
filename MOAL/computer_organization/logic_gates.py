"""Logic gate representations.

Examples and truth values:

AND:
    1, 0 = 0
OR:
    1, 1 = 1
NOT:
    0 = 1
    1 = 0
NAND:
    1, 0 = 1
NOR:
    1, 0 = 0
XOR:
    1, 1 = 0

"""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""


DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from random import choice


def _and(pulse1, pulse2):
    """Calculate AND gate."""
    return 0 if not all([pulse1, pulse2]) else 1


def _or(pulse1, pulse2):
    """Calculate OR gate."""
    return 1 if any([pulse1, pulse2]) else 0


def _not(pulse):
    """Calculate NOT gate."""
    return 0 if pulse == 1 else 1


def _nor(pulse1, pulse2):
    """Calculate NOR gate."""
    return 0 if pulse1 or pulse2 else 1


def _xor(pulse1, pulse2):
    """Calculate XOR gate."""
    return 0 if pulse1 == pulse2 else 1

if DEBUG:
    with Section('Logic gates'):
        onegate = [('not', _not)]
        twogate = [('and', _and), ('or', _or), ('nor', _nor), ('xor', _xor)]
        for name, func in onegate:
            p1 = choice([0, 1])
            print('{0}: {1} = {2}'.format(name.upper(), p1, func(p1)))
        for name, func in twogate:
            p1, p2 = choice([0, 1]), choice([0, 1])
            print('{0}: {1}, {2} = {3}'.format(
                name.upper(), p1, p2, func(p1, p2)))
