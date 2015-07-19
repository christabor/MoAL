# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_simple
from random import choice


DEBUG = True if __name__ == '__main__' else False


class Dyck(list):

    def __init__(self, max):
        self._max = max
        self.rejoinder = True
        self.string = list('[]' * self._max)

    def __abs__(self):
        """Returns the absolute value, as 2-tuple, where |u|"""
        lefts, rights = 0, 0
        for x in self.string:
            if x == '[':
                lefts += 1
            elif x == ']':
                rights += 1
        return lefts, rights

    def __str__(self):
        if self.rejoinder:
            return 'Rejoined: {}'.format(
                ' '.join(''.join(self.string).split('][')))
        return self.string

    def is_balanced(self):
        lefts, rights = abs(self)
        return lefts == rights

    def run(self):
        count = range(0, self._max * 2)
        for x in count:
            index = choice(count)
            # Truncate for visual purposes (e.g. nested brackets, etc)
            chars = self.string[0:self._max]
            # Make sure it contains both, since the form language definition
            # requires it.
            if chars[-1] == '[':
                chars += ']'
            print('Dyck language subset: {}'.format(''.join(chars)))
            # Insert brackets at random locations, as this can produce
            # variations that show possible nesting.
            self.string.insert(index, '[{}]'.format(''))

    def show_equation(self, equation):
        eq = list(equation)
        eq = filter(lambda x: x.strip() in [']', '['], eq)
        print(''.join(eq))
        return eq


if DEBUG:
    with Section('Dyck language'):
        dycklang = Dyck(12)
        dycklang.run()
        print(dycklang)
        print_simple('Absolute value:', abs(dycklang), newline=False)
        assert dycklang.is_balanced()
        assert dycklang.show_equation(
            '[2x - 3 + [7 / 2]] + [[3x x [4 - 2]] + [4x - [1 * [3 + 5]]]]')
