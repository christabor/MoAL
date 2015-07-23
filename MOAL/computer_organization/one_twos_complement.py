# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import divider
from MOAL.helpers.text import random_binary
from MOAL.computer_organization.numerical_encoding_basic import bin_to_dec
from MOAL.computer_organization.numerical_encoding_basic import dec_to_bin
from MOAL.computer_organization.data_types import BaseDataType
from random import choice


DEBUG = True if __name__ == '__main__' else False


def ones_complement(binary):
    binary = list(binary)
    for k, digit in enumerate(binary):
        binary[k] = '1' if digit == '0' else '0'
    return ''.join(binary)


def twos_complement(binary):
    """Conversion algorithm from
    cs.cornell.edu/~tomf/notes/cps104/twoscomp.html#twotwo"""
    old = binary
    binary = ones_complement(binary)
    ones = binary
    binary = BaseDataType.increment(''.join(binary))
    if DEBUG:
        print('Complements: one: {}, two: {}, (original: {})'.format(
            ''.join(ones), binary, ''.join(old)))
    dec = bin_to_dec(binary)
    sign, res = ('neg', -dec) if list(binary)[0] == '1' else ('pos', dec,)
    res_bin = dec_to_bin(res)
    if DEBUG:
        print('Final decimal is {}: {} ({})'.format(sign, res, res_bin))
    return res_bin


if __name__ == '__main__':
    with Section('Computer organization - one, two\'s complement'):
        evens = [n for n in range(2, 16) if n % 4 == 0]
        for _ in range(8):
            twos_complement(random_binary(choice(evens)))
            divider(atom='-')
