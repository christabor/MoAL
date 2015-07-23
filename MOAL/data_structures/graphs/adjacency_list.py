# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from pprint import pprint as ppr


class AbstractGraphList(object):

    def __init__(self):
        # We're using a dictionary since the vertices are labeled, but the lists
        # are contained within: "a collection of unordered lists."
        self.nodes = {}


class AdjacencyList(AbstractGraphList):
    """
    [Wikipedia]
    "In graph theory and computer science, an adjacency list representation
    of a graph is a collection of unordered lists, one for each vertex
    in the graph. Each list describes the set of neighbors of its vertex.
    See "Storing a sparse matrix" for an alternative approach." """

    def __str__(self):
        divider = '-' * 40
        print(divider)
        for node, adjacent in self.nodes.iteritems():
            print('{} is adjacent to {} '.format(node, ', '.join(adjacent)))
        print(divider)
        return ''

    def __setitem__(self, node, neighbors):
        self.nodes[node] = neighbors

    def __getitem__(self, node):
        return self.nodes[node]

    def report(self, vertex):
        return self.__getitem__(vertex)


if __name__ == '__main__':
    with Section('Adjacency list'):
        AList = AdjacencyList()
        AList['A'] = ['B', 'C', 'D']
        AList['B'] = ['A', 'C', 'D']
        AList['C'] = ['A', 'B', 'D']
        AList['D'] = ['A', 'B', 'C']
        print(AList)
        ppr(AList.nodes)

        print(AList.report('B'))
