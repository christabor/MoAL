# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def cls_dec(cls):
    class NewClass(cls):
        def __init__(self, *args, **kwargs):
            print('----------- I am the new class dec #1! -------------')
            return super(NewClass, self).__init__(*args, **kwargs)
    return NewClass


def cls_dec2(cls):
    class NewClass(cls):
        def __str__(self):
            return '----------- I am the new class dec #2! -------------'
    return NewClass


@cls_dec
@cls_dec2
class ClassPrimitive(object):

    used = 0
    points = None

    def __init__(self, *args):
        print(list(args))


if DEBUG:
    with Section('Class decorators'):
        for x in range(4):
            f = ClassPrimitive(x, x ** 2)
            print(f)
