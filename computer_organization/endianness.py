# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h3
from pprint import pprint as ppr

DEBUG = True if __name__ == '__main__' else False

"""'Endianness' represents byte ordering when memory is addressed in a computer
- little endian stores the *smallest* byte first, whereas the *biggest*
bit is stored first as big endian.

See betterexplained.com/articles/
    understanding-big-and-little-endian-byte-order/ for a nice overview.

Also, see linux.die.net/man/3/<function> for real network conversion functions
e.g. [htons, htons, ntohl, ntohs]

And see linux.die.net/man/3/endian for base conversion functions
e.g. [htobe16, htole16, be16toh, le16toh, htobe32, htole32, be32toh,
le32toh, htobe64, htole64, be64toh, le64toh]

Free online copy of Gulliver's travels available here:
literatureproject.com/gulliver-travel/

Character list:
cliffsnotes.com/literature/g/gullivers-travels/character-list
"""


class Endian:
    """A machine would probably never MIX little AND big endian byte ordering,
    but this is an abstraction for practicing some concepts."""

    def __init__(self):
        self.memory = {}
        self.bom = '<<BOM'
        self.start = 0

    def __setitem__(self, key, value):
        self.endian_adapter(value)

    def __contains__(self, key):
        return key in self.memory.values()

    def __getitem__(self, value):
        try:
            return self.endian_adapter(value)
        except Exception:
            return None

    def __str__(self):
        ppr(self.memory.keys())
        ppr(self.memory.values())
        return ''

    def _store(self, bits):
        self.memory[self.start] = bits
        self.start += 1

    def read_bom(self, string):
        if string.startswith(self.bom):
            return True
        return False

    def add_bom(self, string):
        bom = self.bom
        return bom + string

    def endian_adapter(self, bits, order='big'):
        if order == 'big':
            return self.store_big_endian(bits)
        else:
            return self.store_little_endian(bits)

    def store_big_endian(self, bits):
        return self._store(bits)

    def store_little_endian(self, bits):
        return self._store(bits[::-1])


if __name__ == '__main__':
    with Section('Computer organization - Byte ordering, endianness'):
        endian = Endian()
        chars_little = ['Glumdalclitch', 'Munodi', 'Struldbruggs', 'Houyhnhnms']
        chars_big = ['Lemuel Gulliver', 'Flimnap', 'Reldresal',
                     'Skyresh Bolgolam', 'Slamecksan']

        for character in chars_little:
            endian.store_little_endian(character)

        for character in chars_big:
            endian.store_big_endian(character)

        assert 'idonuM' in endian
        assert 'Glumdalclitch' not in endian
        assert 'panmilF' not in endian
        assert 'Skyresh Bolgolam' in endian
        assert endian.add_bom('Hello world') == '<<BOMHello world'
        assert endian.read_bom('<<BOMHello world')

        print_h3('Big endian', desc='memory view with big ordering')
        print(endian)

        print_h3('Little endian', desc='memory view with little ordering')
        print(endian)
