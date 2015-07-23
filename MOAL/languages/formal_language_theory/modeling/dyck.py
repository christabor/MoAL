# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_simple
from random import choice


DEBUG = True if __name__ == '__main__' else False


class Dyck(list):

    def __init__(self, max, left='(', right=')'):
        self._max = max
        self.rejoinder = True
        self.left = left
        self.right = right
        self.string = list('{}{}'.format(self.left, self.right) * self._max)

    def __abs__(self):
        """Returns the absolute value, as 2-tuple, where the absolute value
        |u| is represented as the count of left and right brackets."""
        lefts, rights = 0, 0
        for char in self.string:
            if char == self.left:
                lefts += 1
            elif char == self.right:
                rights += 1
        return lefts, rights

    def __str__(self):
        if self.rejoinder:
            return 'Rejoined: {}'.format(
                ' '.join(''.join(self.string).split('{}{}'.format(
                    self.right, self.left))))
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
            if chars[-1] == self.left:
                chars += self.right
            print('Dyck language subset: {}'.format(''.join(chars)))
            # Insert brackets at random locations, as this can produce
            # variations that show possible nesting.
            self.string.insert(index, '{}{}{}'.format(
                self.left, '', self.right))

    def show_equation(self, equation):
        eq = list(equation)
        eq = filter(lambda x: x.strip() in [self.right, self.left], eq)
        print(''.join(eq))
        return ''.join(eq)


if DEBUG:
    with Section('Dyck language'):
        dycklang = Dyck(12)
        dycklang.run()
        print(dycklang)
        print_simple('Absolute value:', abs(dycklang), newline=False)
        assert dycklang.is_balanced()
        assert dycklang.show_equation(
            '(2x - 3 + (7 / 2)) + ((3x x (4 - 2)) + (4x - (1 * (3 + 5))))')
