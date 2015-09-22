# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class PipelineStage:
    pass


class Pipeline(object):

    def __setitem__(self, k, v):
        pass


if DEBUG:
    with Section('Hartmann Pipeline'):
        pass
