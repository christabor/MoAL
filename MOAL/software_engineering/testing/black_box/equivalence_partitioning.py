# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def add(one, two):
    return one + two


def add_evens(one, two):
    if one % 2 != 0 or two % 2 != 0:
        raise ValueError('Must provide even numbers')
    return one + two


def format_name(prefix, first, last):
    if len(first) > 30 or len(last) > 30:
        raise ValueError('Name too long! :(')
    print('Name: {}. {}{}'.format(prefix, first, last))


class Environment:

    @staticmethod
    def draw(x, y):
        print('Drawing: @x {} @y {}'.format(x, y))


def draw_picture(x, y, pic, environment):
    # Pic is a picture object with two properties: height and width.
    # x and y must be valid inside of pic's dimensions.
    if x > pic['w'] or x < 0:
        raise ValueError
    if y > pic['h'] or y < 0:
        raise ValueError
    environment.draw(x, y)


def test(data=(), exception=ValueError, comment='', fn=None):
    try:
        return fn(*data)
    except exception:
        print(comment)

if DEBUG:
    with Section('Equivalence partitioning'):
        test(data=(43, 10, {'w': 100, 'h': 100}, Environment), fn=draw_picture)
        test(data=(120, 10, {'w': 100, 'h': 100}, Environment),
             fn=draw_picture,
             comment='Testing boundary: large X and large Y position')
        test(data=(43, 12, {'w': 100, 'h': 100}, Environment),
             fn=draw_picture,
             comment='Testing boundary: large X and large Y position')
        test(data=('Mr', 'Guy', 'Dude'), fn=format_name, exception=TypeError)
        test(data=('Mr',), fn=format_name, exception=TypeError,
             comment='Testing missing arguments')
        test(data=('Ms', 'Guy', 'Superlonglastnamepersonchiefbuddydudeperson'),
             fn=format_name, exception=ValueError,
             comment='Testing long name arguments')
        test(data=('Ms', 'Gal', 'Superlonglastnamepersonchiefbuddydudeperson'),
             fn=format_name, exception=ValueError,
             comment='Testing long name arguments')
        test(data=(2, 3), fn=add)
        test(data=(-2, -3), fn=add)
        test(data=('one', 'three'), fn=add, exception=TypeError,
             comment='Invalid types - strings')
        test(data=('one', None), fn=add, exception=TypeError,
             comment='Invalid types - string and None')
        test(data=(4, 2), fn=add_evens)
        test(data=(1, 2), fn=add_evens, exception=ValueError,
             comment='Invalid numbers - uneven (one)')
        test(data=(1, 3), fn=add_evens, exception=ValueError,
             comment='Invalid numbers - uneven (both)')
