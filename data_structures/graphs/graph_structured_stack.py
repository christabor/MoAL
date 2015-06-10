# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from data_structures.graphs.graphs import DirectedAcyclicGraph

DEBUG = True if __name__ == '__main__' else False


class GraphStructuredStack(DirectedAcyclicGraph):

    def find_stacks(self, start, end):
        res = self._dfs(start, end)
        if DEBUG:
            print('Result of DFS: {}'.format(res))
        return res

    def find_all_stacks(self):
        """Find all full depth stacks 'auto-magically'.
        Super inefficient -- mostly for fun and experimentation.

        Note:

        A curious phenomenon? When searching for a full-depth walk,
        any walk 1 vertex less appears to be valid as well, but is skipped
        since it is not the last matching element, and is thus disregarded
        since typical walks only care about first and last nodes.
        The root vertex must be added in that case, and then contributes to
        the number of "full depth" walks.

        This may not be robust or consistent, but is an interesting
        observation I found while trying to implement the algorithm here, to
        find all potential "stacks" of a graph from one "side" to the other.
        """
        paths = []
        for vertex, data in self.vertices.iteritems():
            path = [vertex]
            current = data['edges']
            for edge in current:
                while len(current) > 0:
                    _vertex = current[0]
                    path.append(_vertex)
                    current = self.vertices[_vertex]['edges']
            paths.append(path)
        depth = len(max(paths))
        _paths = []
        # Find all full-depth walks.
        root_nodes = []
        for path in paths:
            if len(path) == depth:
                root_nodes.append(path[0])
                _paths.append(path)
        # Find those that are depth - 1, to be added, and make up
        # the difference, but only if they are adjacent to the next node
        # in each path, (i.e valid walks.)
        for path in paths:
            if len(path) == depth - 1:
                if len(root_nodes) > 0:
                    for node in root_nodes:
                        if node != path[0] and path[0] in self[node]['edges']:
                            path = [node] + path
                if path not in _paths:
                    _paths.append(path)
        return _paths

    def __str__(self):
        _paths, f = self.find_all_stacks(), ''
        for path in _paths:
            f += 'Stack: {} ... '.format(path)
            for k, nodes in enumerate(path):
                f += '{}({})'.format('' if k == 0 else '--', nodes)
            f += '\n'
        return f

if DEBUG:
    with Section('Graph Structured Stack'):
        # GSS from Wikipedia article:
        gs_stack = GraphStructuredStack({
            7: {'edges': [3, 4, 5]},
            8: {'edges': [6]},
            3: {'edges': [1]},
            4: {'edges': [1]},
            5: {'edges': [2]},
            6: {'edges': [2]},
            1: {'edges': [0]},
            2: {'edges': [0]},
            0: {'edges': []},
        })
        print('Find stacks')
        assert len(gs_stack.find_stacks(8, 0)['edges']) == 0
        assert len(gs_stack.find_stacks(7, 0)['edges']) == 0
        assert len(gs_stack.find_stacks(7, 1)['edges']) != 0
        assert len(gs_stack.find_stacks(7, 4)['edges']) != 0
        assert len(gs_stack.find_stacks(7, 3)['edges']) != 0
        assert len(gs_stack.find_stacks(7, 5)['edges']) != 0
        assert gs_stack.find_stacks(7, 6) == []
        print('Find ALL stacks')
        gs_stack.find_all_stacks()
        print(gs_stack)
