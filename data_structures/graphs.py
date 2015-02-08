# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import Section
from generic_helpers import _print
from pprint import pprint as ppr
from random import randrange
from random import choice

MAX_VERTICES = 6
MAX_EDGES = MAX_VERTICES / 2
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

    def __getitem__(self, node):
        return self.nodes[node]

    def tour(self, start, end, path=[]):
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
                    sub_paths = self.tour(node, end, path=path)
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

    def connections(self, node):
        try:
            return '({})--{}'.format(node, self.nodes[node])
        except KeyError:
            raise InvalidGraphRepresentation

    def get_vertices(self):
        vertices = [] + self.nodes.keys()
        for vals in self.nodes.values():
            vertices = vertices + vals
        return vertices

    def get_degree(self, vertex):
        slots = {}
        nodes = self.get_vertices()
        for node in nodes:
            try:
                slots[node] += 1
            except KeyError:
                slots[node] = 0
        return slots[vertex]

    def has_degree(self, degrees, vertex=None):
        try:
            return self.get_degree(vertex) == degrees
        except KeyError:
            return False

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
        # Use a set to prevent duplicated in/outgoing edges.
        self.nodes[node] = directions

    def __delitem__(self, node):
        del self.nodes[node]

    def __str__(self):
        display = []
        for vertex, nodes in self.nodes.iteritems():
            display.append('{outbound} <-- ({vertex}) <-- {inbound}'.format(
                vertex=vertex,
                inbound=list(nodes['in']),
                outbound=list(nodes['out'])))
        return ',\n'.join(display)


def _rand_edges(num_edges):
    global all_vertices
    return [choice(all_vertices) for _ in range(num_edges)]


def _test_tour_valid(graph):
    valid = False
    while not valid:
        start = choice(all_vertices)
        end = choice(all_vertices)
        res = graph.tour(start, end)
        if len(res) > 0:
            return '{}, {}: Tour results: {}'.format(start, end, res)
            valid = True

if __name__ == '__main__':
    with Section('Basic graph'):
        graph = Graph()
        # # Initial seeding
        for _ in range(5):
            graph[choice(all_vertices)] = _rand_edges(MAX_EDGES)

        _print('Generated graph', graph.nodes, func=ppr)
        _print('Tour of...', _test_tour_valid(graph))

        deg, ver = randrange(0, MAX_EDGES), choice(all_vertices)
        print 'Has degree {} ... {}? {}'.format(
            deg, ver, graph.has_degree(deg, vertex=ver))

        for _ in range(5):
            try:
                _print('connections', graph.connections(choice(all_vertices)))
            except InvalidGraphRepresentation:
                print (
                    'Invalid graph was generated -- need more than 2 vertices')
        for node in graph:
            print 'Node {} has degree {}'.format(node, graph.get_degree(node))
        _print('graph', graph)
        _print('Has multiple degrees?', graph.has_multiple_degrees())

    with Section('Directed Graph'):
        digraph = DirectedGraph()
        for n in range(MAX_VERTICES):
            digraph[n] = {
                'in': [_rand_edges(MAX_EDGES)],
                'out': [_rand_edges(MAX_EDGES)]
            }
        _print('Generated directed-graph', digraph.nodes, func=ppr)
        _print('Digraph', digraph)
        _print('Get item:', digraph[4])
        digraph[3] = {'in': [1, 2, 4], 'out': [3, 2, 5]}
        _print('Set item:', digraph[3])
        del digraph[2]
        _print('Del item:', digraph)
        _print('Tour of...', _test_tour_valid(digraph))
