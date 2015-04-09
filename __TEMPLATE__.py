# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class MyClass(object):
    raise NotImplementedError


if DEBUG:
    with Section('SOME MODULE TITLE'):
        pass
