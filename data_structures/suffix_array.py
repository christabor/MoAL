# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from helpers.display import Section
from helpers.display import _print
from helpers.text import words_unix_dict


class SuffixArray:

    def __init__(self, strings=None):
        self.strings = strings if strings is not None else []

    def __str__(self):
        return str(self.strings)

    def __getitem__(self, string):
        self.strings.append(string)

    def __setitem__(self, string, val):
        self.strings[string] = val

    def __delitem__(self, string):
        del self.strings[string]

    @classmethod
    def suffixes(self, string):
        return [string[k:] + '$' for k, char in enumerate(reversed(string))]

    def make_superstring(self, strings=None):
        if strings is None:
            strings = self.strings
        self.strings = [[self.suffixes(string)] for string in strings]


class PrefixArray(SuffixArray):

    @classmethod
    def prefixes(self, string):
        return [string[k:] + '$' for k, char in enumerate(string)]

    def make_superstring(self, strings=None):
        if strings is None:
            strings = self.strings
        self.strings = [[self.prefixes(string)] for string in strings]


class InfixArray(SuffixArray):
    """This is a weird experiment, not totally relevant."""

    @classmethod
    def infixes(self, string, bisector=3):
        """Returns something like
            [[ca], [t], [do], [g], [bi], [rd]]
            where the first list is the bisector slice from the left,
            and the second from the right
        """
        ia = []
        if len(string) < bisector:
            bisector = len(string)
        for k, char in enumerate(string):
            ia.append([string[bisector:] + '$', string[:bisector]])
        return ia

    def make_superstring(self, strings=None):
        if strings is None:
            strings = self.strings
        self.strings = [[self.infixes(string)] for string in strings]


class SuperSuffixArray(SuffixArray):

    def _view(self, suffixes):
        _print(suffixes[0][:-1], '')
        for k, substr in enumerate(suffixes):
            max_width = (len(suffixes[:-1]) + 30)
            spaces = '~' * max_width
            print spaces
            print ' {}{} {}... k={}'.format(
                substr, ' ' * (max_width - len(substr) - 12), len(substr), k)

    def __repr__(self):
        for suffix_group in self.strings:
            for _, suffixes in enumerate(suffix_group):
                self._view(suffixes)
        return ''

    def sort(self):
        for k, suffix_group in enumerate(self.strings):
            for j, suffixes in enumerate(suffix_group):
                self.strings[k][j] = sorted(self.strings[k][j])


if __name__ == '__main__':
    with Section('Suffix Array'):
        DEBUG = False

        word_gen = words_unix_dict()

        iarray = InfixArray()
        iarray.make_superstring(strings=[word_gen.next() for _ in range(2)])

        _print('Weird infix style substring', iarray)

        ssarray = SuperSuffixArray()
        ssarray.make_superstring(strings=[word_gen.next() for _ in range(10)])

        _print('Superstring suffix array', ssarray, func=repr)

        ssarray.sort()

        _print('SORTED Superstring suffix array', ssarray, func=repr)

        if DEBUG:
            ssarray2 = SuperSuffixArray()
            ssarray2.make_superstring(
                strings=['pneumonoultramicroscopicsilicovolcanoconiosis'])

            _print('Superstring suffix array - long', ssarray2, func=repr)
