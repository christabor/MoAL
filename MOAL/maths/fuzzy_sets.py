# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from fuzzywuzzy import fuzz

DEBUG = True if __name__ == '__main__' else False


if DEBUG:
    with Section('Fuzzy sets'):
        while True:
            comp = raw_input(
                'Enter two strings for comparison '
                '(separarated by a double pipe - '
                'e.g. word one || word two) => ')
            a, b = comp.split(' || ')
            score = fuzz.ratio(a, b)
            print('[Comparison ratio] for {}, {} = {}'.format(a, b, score))
            score = fuzz.partial_ratio(a, b)
            print('[Partial ratio] for {}, {} = {}'.format(a, b, score))
            score = fuzz.token_sort_ratio(a, b)
            print('[Token sort ratio] for {}, {} = {}'.format(a, b, score))
