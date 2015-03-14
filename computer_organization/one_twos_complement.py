# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import divider
from computer_organization.numerical_encoding_basic import bin_to_dec
from computer_organization.data_types import BaseDataType
from random import choice


DEBUG = True if __name__ == '__main__' else False


def ones_complement(binary):
    binary = list(binary)
    for k, digit in enumerate(binary):
        binary[k] = '1' if digit == '0' else '0'
    return binary


def twos_complement(binary):
    """Conversion algorithm from
    cs.cornell.edu/~tomf/notes/cps104/twoscomp.html#twotwo"""
    old = binary
    binary = ones_complement(binary)
    ones = binary
    binary = BaseDataType.increment(''.join(binary))
    print('Complements: one: {}, two: {}, (original: {})'.format(
        ''.join(ones), binary, ''.join(old)))
    dec = bin_to_dec(binary)
    sign, res = ('neg', -dec) if list(binary)[0] == '1' else ('pos', dec,)
    print('Final decimal is {}: {}'.format(sign, res))


def random_binary(bits):
    if bits % 4 != 0:
        raise ValueError('Need even bit length!')
    binary = ''
    for _ in range(bits):
        binary += str(choice([1, 0]))
    return binary


if __name__ == '__main__':
    with Section('Computer organization - one, two\'s complement'):
        evens = [n for n in range(2, 16) if n % 4 == 0]
        for _ in range(8):
            twos_complement(random_binary(choice(evens)))
            divider(atom='-')
