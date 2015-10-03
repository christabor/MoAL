# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


from MOAL.helpers.display import Section
from MOAL.type_theory.nominal_structural import StructuralType

DEBUG = True if __name__ == '__main__' else False


class Square(StructuralType):

    def __init__(self):
        self.props = {}

    def __str__(self):
        return str(self.props)

    def __setitem__(self, prop, value):
        self.props[prop] = value

    def set_size(self, h, w):
        pass


class ColoredSquare(Square):
    pass


class Rectangle(Square):

    def set_height(self, h):
        pass

    def set_width(self, w):
        pass


if DEBUG:
    with Section('SOLID - Liskov Substitution Principle'):
        # We can use the original structural ABC to access its subclasshook,
        # but it won't be structurally the same as our new inherited
        # classes, which is fine -- we just want to use the utility of
        # structural checking for all our own subclasses here.
        sqr = Square()
        # Expected to not be instance, since we modified it from the original.
        assert not isinstance(sqr, StructuralType)

        green_sqr = ColoredSquare()
        rect = Rectangle()
        green_sqr['color'] = 'green'
        rect['width'] = 100
        rect['height'] = 100
        sqr['size'] = 120

        # Sanity check
        assert isinstance(sqr, Square)
        # Since this is structurally the same, it should work.
        assert isinstance(green_sqr, Square)
        # Inherits from Square, but is not structurally an instance of it,
        # so this should not be an instance.
        assert not isinstance(rect, Square)
        assert not isinstance(rect, ColoredSquare)

        print(sqr)
        print(green_sqr)

        sqr.show_class()
        green_sqr.show_class()
