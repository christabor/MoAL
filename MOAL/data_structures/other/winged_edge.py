# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from pprint import pprint as ppr

DEBUG = True if __name__ == '__main__' else False


class WingedEdgeFace:

    def __init__(self, orient, data={}):
        self.name = orient
        self.data = data


class WingedEdgeEdge:

    def __init__(self, edge, data={}):
        self.name = edge
        self.data = data


class WingedEdgeVertex:

    def __init__(self, start, end, data={}):
        self.vertices = start, end
        self.data = data


class WingedEdgeTraversal:

    def __init__(self, pred, succ):
        self.data = pred, succ


class WingedEdge:

    def __init__(self, *args, **kwargs):
        self.faces = []
        self.edges = []
        self.vertices = []
        self.left_trav = []
        self.right_trav = []

    def add_traversal(self, *args, **kwargs):
        orient = kwargs.get('orient')
        if orient is 'left':
            self.left_trav.append(WingedEdgeTraversal(*args))
        else:
            self.right_trav.append(WingedEdgeTraversal(*args))

    def add_vertices(self, start, end):
        self.vertices.append(WingedEdgeVertex(start, end))

    def add_face(self, left, right):
        self.faces.append((WingedEdgeFace(left), WingedEdgeFace(right)))

    def add_edge(self, edge_name):
        self.edges.append(WingedEdgeEdge(edge_name))

    def __str__(self):
        ppr(self.faces)
        ppr(self.edges)
        ppr(self.vertices)
        ppr(self.left_trav)
        ppr(self.right_trav)
        return ''

if DEBUG:
    with Section('Data structure - winged edge'):
        # Information from:
        # http://www.cs.mtu.edu/~shene/COURSES/cs3621/NOTES/model/winged-e.html

        we = WingedEdge()
        map(we.add_edge, ['a', 'b', 'c', 'd', 'e', 'f'])
        we.add_vertices('A', 'D')
        we.add_vertices('A', 'B')
        we.add_vertices('B', 'D')
        we.add_vertices('B', 'C')
        we.add_vertices('C', 'D')
        we.add_vertices('A', 'C')

        we.add_face(3, 1)
        we.add_face(1, 4)
        we.add_face(1, 2)
        we.add_face(2, 4)
        we.add_face(2, 3)
        we.add_face(4, 3)

        we.add_traversal('e', 'f')
        we.add_traversal('c', 'a'),
        we.add_traversal('a', 'b')
        we.add_traversal('e', 'c'),
        we.add_traversal('c', 'd')
        we.add_traversal('d', 'b')

        we.add_traversal('b', 'c', orient='right')
        we.add_traversal('f', 'd', orient='right')
        we.add_traversal('d', 'e', orient='right')
        we.add_traversal('d', 'f', orient='right')
        we.add_traversal('b', 'a', orient='right')

        print(we)
