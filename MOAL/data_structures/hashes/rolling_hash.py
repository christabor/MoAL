# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.text import gibberish2

DEBUG = True if __name__ == '__main__' else False

"""http://courses.csail.mit.edu/6.006/spring11/rec/rec06.pdf"""


def adler_32(string):
    """See: https://en.wikipedia.org/wiki/Adler-32#The_algorithm"""
    modnum = 65521
    substrings = []
    a, b = 1, 0
    for k, letter in enumerate(string):
        a = (a + ord(letter)) % modnum
        b = b + a % modnum
        substrings.append(sum([ord(c) for c in string[:k]]))
    return (b << 16) | a


def _fmt(string):
    return ''.join(map(str, string))


def calculate_rolling_hash(substring, string):
    """Get list of digit representations for reach string"""
    sublist = _fmt([ord(c) for c in list(substring)])
    end = len(substring)
    biglist = []
    for start, char in enumerate(string):
        if start == 0:
            # Get 'windows' of substrings
            res = [ord(c) for c in string[start:start + end]]
            biglist.append(_fmt(res))
            break
    # Go over remainder list, calculating each subsequent hash value,
    # based on the first version calculation, for speed.
    res = biglist[0]
    for start, char in enumerate(string):
        new = int(str(res)[:1]) * 10
        res = int(str(new) + str(string[start + end:start + end - 1]))
    return sublist, biglist


def calculate_rolling_hash_average(substring, string):
    p, s = calculate_rolling_hash(substring, string)
    return int(p) % 4096, int(''.join(map(str, s))) % 4096


if DEBUG:
    with Section('Rolling Hash / checksums'):
        assert adler_32('Wikipedia') == 300286872
        data = ''.join(map(gibberish2, range(10)))
        s1, s2 = 'Super', 'Supercalifragalisticexpialidocious'
        print(calculate_rolling_hash(s1, s2))
        print(calculate_rolling_hash_average(s1, s2))
