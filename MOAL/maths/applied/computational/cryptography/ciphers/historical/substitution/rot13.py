# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def rot_n(string, n):
    """Modified, based on: http://en.literateprograms.org/Rot13_(Python)"""
    if not isinstance(n, int):
        raise TypeError

    def _handle_char(char):
        if not char.isalpha():
            return char
        dist = n if char.lower() <= 'm' else -n
        # Return character ordinal value after augmenting the position.
        return chr(ord(char) + dist)

    return ''.join([_handle_char(char) for char in list(string)])


def rot13(string):
    return rot_n(string, 13)

if DEBUG:
    with Section('Cipher - ROT13'):
        """https://en.wikipedia.org/wiki/ROT13"""
        val = 'Why did the chicken cross the road?'
        res = 'Jul qvq gur puvpxra pebff gur ebnq?'
        assert val.encode('rot13') == res
        # Convert using custom
        assert rot13(val) == res
        # Convert back
        assert rot13(rot13(val)) == val

        for n in range(13):
            print('ROT{} - {}'.format(n, rot_n(val, n)))
