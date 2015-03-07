# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
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
    def make_substring(cls, string):
        return [string[k:] + '$' for k, char in enumerate(reversed(string))]

    def make_superstring(self, strings=None):
        if strings is None:
            strings = self.strings
        self.strings = [[self.make_substring(string)] for string in strings]


class PrefixArray(SuffixArray):

    @classmethod
    def make_substring(cls, string):
        return [string[k:] + '$' for k, char in enumerate(string)]


class InfixArray(SuffixArray):
    """This is a weird experiment, not totally relevant."""

    @classmethod
    def make_substring(cls, string, bisector=2):
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


class SuperSuffixArray(SuffixArray):

    def _view(self, suffixes):
        prnt(suffixes[0][:-1], '')
        for k, substr in enumerate(suffixes):
            max_width = (len(suffixes[:-1]) + 30)
            spaces = '~' * max_width
            print(spaces)
            print(' {}{} {}... k={}'.format(
                substr, ' ' * (max_width - len(substr) - 12), len(substr), k))

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

        prnt('Weird infix style substring', iarray)

        ssarray = SuperSuffixArray()
        ssarray.make_superstring(strings=[word_gen.next() for _ in range(10)])

        prnt('Superstring suffix array', ssarray, func=repr)

        ssarray.sort()

        prnt('SORTED Superstring suffix array', ssarray, func=repr)

        if DEBUG:
            ssarray2 = SuperSuffixArray()
            ssarray2.make_superstring(
                strings=['pneumonoultramicroscopicsilicovolcanoconiosis'])

            prnt('Superstring suffix array - long', ssarray2, func=repr)
