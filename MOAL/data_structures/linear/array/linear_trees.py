# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


class NTree:

    def __init__(self, npg):
        self.items = []
        self.nodes_per_group = npg

    def __str__(self):
        return str(self.items)

    def __setitem__(self, key, value):
        if len(value) != self.nodes_per_group:
            raise ValueError(
                'Invalid number of nodes. Nodes per '
                'group should be: {}'.format(self.nodes_per_group))
        self.items.insert(key, value)

if DEBUG:
    with Section('Array - linear trees (trees represented as arrays)'):
        linear_quadtree = NTree(4)
        linear_octree = NTree(8)

        linear_quadtree[0] = [1, 2, 3, 4]
        try:
            linear_quadtree[1] = [2, 3, 4]
        except ValueError:
            print('[Raised exception as expected]')
        linear_quadtree[4] = [5, 6, 7, 8]
        print(linear_quadtree)

        linear_octree[0] = [1, 2, 3, 4, 5, 6, 7, 8]
        try:
            linear_octree[1] = [2, 3, 4]
        except ValueError:
            print('[Raised exception as expected]')
        linear_octree[4] = [9, 10, 11, 12, 13, 14, 15, 16]
        print(linear_octree)
