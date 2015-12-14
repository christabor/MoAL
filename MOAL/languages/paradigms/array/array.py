# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import divider
from numpy import *

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    with Section('Array programming'):
        a = zeros(20).reshape(5, 4).reshape(4, 5)
        print(a, a.shape)
        print(array(arange(10), dtype=complex))
        divider()
        print(ones(20).reshape(4, 5))
        print(linspace(0, 2, 10))
        print(sin(linspace(1, 4, 10)))
        divider()
        b = array([1, 10])
        print(b)
        for n in range(10):
            print(n * sin(b))
        divider()
        a = array(random.random())
        b = array(random.random())
        c = array(arange(10))
        d = dot(a, b) + c
        print(d)
        print(d.cumsum())
        divider()
        a = array(arange(0, 12).reshape(4, 3))
        print(a)
        print(a[-1, 2])
        a = column_stack((arange(4, 5), arange(4, 5)))
        print(a)
        a = arange(12).reshape(2, 6)
        print(a > 4)
        print(a * 2)
        print(a ** 2)
        b = a ** 2 + 2
        print(b, b.transpose())
