# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def skew_to_dec(dec):
    res = 0
    if dec == 0 or dec == 1:
        return dec
    for n, digit in enumerate(reversed(list(str(dec)))):
        n = n + 1
        out = int(digit) * (2 ** n - 1)
        res += out
    return int(res)


if DEBUG:
    with Section('Skew Binary system'):
        # Test numbers from https://uva.onlinejudge.org/external/5/575.html
        test_nums = [
            (10120, 44),
            (200000000000000000000000000000, 2147483646),
            (10, 3),
            (1000000000000000000000000000000, 2147483647),
            (11, 4),
            (100, 7),
            (11111000001110000101101102000, 1041110737),
            (0, 0),
        ]

        for test in test_nums:
            dec, skewed = test
            print(skew_to_dec(dec))
            assert skew_to_dec(dec) == skewed
