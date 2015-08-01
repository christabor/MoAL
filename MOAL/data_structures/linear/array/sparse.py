# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from MOAL.helpers.datamaker import make_sparselist
from MOAL.helpers.text import gibberish2
from random import randrange as rr

DEBUG = True if __name__ == '__main__' else False


if DEBUG:
    with Section('Sparse linear data structures'):
        max = 500
        density = 0.1
        items = {rr(0, max): gibberish2() for _ in range(int(max * density))}
        splist = make_sparselist(items, max)
        prnt('Sparse list', splist)
