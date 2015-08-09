# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def fake_broken_func(*args, **kwargs):
    if 'foo' in kwargs and kwargs['foo'] is not None:
        print(undefined_variable)
    for arg in args:
        print(arg)


def fake_broken_func3():
    def add(y):
        return y + y
    for x in range(10):
        print(y)


def explode(var):
    raise ValueError('Ahhhh!!!')


def fake_broken_func2(number):
    if number == 0:
        print('0')
    if number > 1:
        print('> 1')
    if number > 5:
        print('> 5')
    if number > 10:
        print('> 10')
    if number > 100:
        print(explode(number))


if DEBUG:
    with Section('Fault injection'):
        # Normal
        fake_broken_func(1, 2, 3, 'foo')
        # Inject fault by testing path that will fail
        try:
            fake_broken_func(1, 2, 3, 'foo', foo='Broken!')
        except NameError:
            print('Injected exception for missing var')
        # Normal
        fake_broken_func2(0)
        fake_broken_func2(2)
        fake_broken_func2(6)
        fake_broken_func2(12)
        try:
            fake_broken_func2(101)
        except ValueError:
            print('Injected bad secondary function call')

        try:
            fake_broken_func3()
        except NameError:
            print('Injected bad scope value')
