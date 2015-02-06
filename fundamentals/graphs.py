# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import Section
from random import choice
from pprint import pprint as ppr

MAX_VERTICES = 6
MAX_EDGES = MAX_VERTICES / 2
DEBUG = False
all_vertices = [_ for _ in range(MAX_VERTICES)]


class InvalidGraphRepresentation(Exception):
    pass


class Graph:

    def __init__(self, nodes=None):
        self.nodes = nodes or {}

    def __setitem__(self, node, edges):
        self.nodes[node] = edges

    def __delitem__(self, node):
        del self.nodes[node]

    def __getitem__(self, points, path=[]):
        start, end = points
        path, paths = path + [start], []
        if start == end:
            return path
        if start in self.nodes:
            # {'start': [], '...': [], '...': []}
            for node in self.nodes[start]:
                # {'start': ['...', '...', '...']}
                # Add new node if it's not in the list already.
                if node not in path:
                    # Get new path from this node
                    sub_paths = self.__getitem__((node, end), path=path)
                    for sub_path in sub_paths:
                        paths.append(sub_path)
        return paths

    def __iter__(self):
        return iter(self.nodes)

    def __str__(self):
        display = []
        for vertex, nodes in self.nodes.iteritems():
            sub_nodes = ''
            for node in nodes:
                sub_nodes += '--({})'.format(node)
            display.append('({}){}'.format(vertex, sub_nodes))
        return ',\n'.join(display)

    def view_path(self, node):
        try:
            return '({})--{}'.format(node, self.nodes[node])
        except KeyError:
            raise InvalidGraphRepresentation

    def get_vertices(self):
        vertices = [] + self.nodes.keys()
        for vals in self.nodes.values():
            vertices = vertices + vals
        return vertices

    def get_degree(self, vertex_name):
        slots = {}
        nodes = self.get_vertices()
        for node in nodes:
            try:
                slots[node] += 1
            except KeyError:
                slots[node] = 0
        return slots[vertex_name]

    def has_multiple_degrees(self):
        nodes = self.get_vertices()
        unique = list(set(nodes))
        if len(self.nodes) != len(unique):
            return False
        return True

    def hamiltonian(self):
        pass

    def eulerian(self):
        pass


class DirectedGraph(Graph):

    def __setitem__(self, *args):
        node, directions = args
        # Prevent duplicated in/outgoing edges.
        self.nodes[node] = {
            'in': [set(directions[0])], 'out': [set(directions[1])]
        }

    def __getitem__(self, points, path=[]):
        start, end = points
        path, paths = path + [start], []
        if start == end:
            return path
        if start in self.nodes:
            # {'start': [], '...': [], '...': []}
            for node in self.nodes[start]:
                # {'start': ['...', '...', '...']}
                # Add new node if it's not in the list already.
                if node not in path:
                    # Get new path from this node
                    sub_paths = self.__getitem__((node, end), path=path)
                    for sub_path in sub_paths:
                        paths.append(sub_path)
        return paths

    def __iter__(self):
        return iter(self.nodes)


def _rand_edges(num_edges):
    global all_vertices
    return [choice(all_vertices) for _ in range(num_edges)]


if DEBUG:
    with Section('Basic graph'):
        graph = Graph()
        # Initial seeding
        for _ in range(10):
            graph[choice(all_vertices)] = _rand_edges(MAX_EDGES)
        print 'Graph\n', graph

        for _ in range(10):
            try:
                print '\n', graph.view_path(choice(all_vertices))
            except InvalidGraphRepresentation:
                print (
                    'Invalid graph was generated -- need more than 2 vertices')
        for node in graph:
            print 'Node {} has degree {}'.format(node, graph.get_degree(node))
        print graph
        print 'Has multiple degrees?', graph.has_multiple_degrees()


if DEBUG:
    with Section('Directed Graph'):
        digraph = DirectedGraph()
        for n in range(MAX_VERTICES):
            digraph[n] = [_rand_edges(MAX_EDGES), _rand_edges(MAX_EDGES)]
        print 'Generated directed-graph\n', ppr(digraph.nodes)
        print digraph
