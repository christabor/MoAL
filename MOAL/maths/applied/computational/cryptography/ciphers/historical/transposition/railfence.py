# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def _makerails(string, rails=2):
    if rails < 2:
        raise ValueError('Invalid number of rails.')
    chars = list(string.replace(' ', '').upper())
    _rails = {k: [] for k in range(rails)}
    current = 0
    while len(chars) > 0:
        if current == rails:
            current = 0
        _rails[current].append(chars.pop(0))
        current += 1
    return _rails


def railfence_show(string, rails=2):
    rails = _makerails(string, rails=rails)
    string = ''
    for rail, chars in rails.iteritems():
        offset = rail * '  '
        string += '{}{}'.format(offset, ' . '.join(chars) + '\n')
    return string


def railfence_encipher(string, rails=2, show=False):
    _rails = _makerails(string, rails=rails)
    encoded = ''
    for rail, chars in _rails.iteritems():
        encoded += ''.join(chars)
    if show:
        print(railfence_show(string, rails=rails))
    return encoded


if DEBUG:
    with Section('Cipher - RailFence'):
        """https://en.wikipedia.org/wiki/Rail_fence_cipher"""
        for n in range(2, 6):
            msg = 'I have a very big secret'
            encoded = railfence_encipher(msg, rails=n, show=True)
            print('Encoded with {} rows: {}'.format(n, encoded))
