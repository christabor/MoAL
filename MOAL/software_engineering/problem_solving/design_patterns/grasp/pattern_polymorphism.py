# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class BlobOfMatter(object):

    def __str__(self):
        raise NotImplementedError


class UndifferentiatedCell(BlobOfMatter):
    """Each child class implements a __str__ method (beyond the native python)
    version, so each name is the same, but there are many different versions."""

    def __str__(self):
        return '[ Undifferentiated Cell ]'


class SkinCell(UndifferentiatedCell):

    def __str__(self):
        return 'Skin cell'


class BrainCell(UndifferentiatedCell):

    def __str__(self):
        return 'Brain cell'


class NerveCell(UndifferentiatedCell):

    def __str__(self):
        return 'Nerve cell'


if DEBUG:
    with Section('GRASP polymorphism pattern'):
        cells = [UndifferentiatedCell(), SkinCell(), BrainCell(), NerveCell()]
        for cell in cells:
            print(cell)
