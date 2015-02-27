# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import _print
from pprint import pprint as ppr
from random import randrange
from random import choice

# wikipedia.org/wiki/Glossary_of_graph_theory

MAX_VERTICES = 6
MAX_EDGES = MAX_VERTICES / 2
all_vertices = range(0, MAX_VERTICES)


class InvalidGraphRepresentation(Exception):
    pass


class Graph:

    def __len__(self):
        return len(self.vertices.keys())

    def __init__(self, vertices=None):
        self.vertices = vertices or {}

    def __setitem__(self, node, edges):
        self.vertices[node] = edges

    def __delitem__(self, node):
        del self.vertices[node]

    def __getitem__(self, node):
        return self.vertices[node]

    def __iter__(self):
        return iter(self.vertices)

    def __str__(self):
        display = []
        for vertex, vertices in self.vertices.iteritems():
            display.append('{outbound} <-- ({vertex})'.format(
                vertex=vertex,
                outbound=vertices))
        return ',\n'.join(display)

    def walk(self, start, end, path=[]):
        path = path + [start]
        paths = []
        if start == end:
            return path
        if start in self.vertices:
            for node in self.vertices[start]:
                # Add new node if it's not in the list already.
                if node not in path:
                    # Get new path from this node
                    paths += self.walk(node, end, path=path)
        return paths

    def connections(self, node):
        try:
            return '({})--{}'.format(node, self.vertices[node])
        except KeyError:
            raise InvalidGraphRepresentation

    def all_vertices(self):
        vertices = self.vertices.keys()
        for vals in self.vertices.values():
            vertices = vertices + vals
        return list(set(vertices))

    def degree(self, node):
        return len(self.vertices[node]) if node in self.vertices else 0

    def has_degree(self, node, degrees):
        return self.degree(node) == degrees

    def has_multiple_degrees(self, node):
        return self.degree(node) > 1

    def is_open(self, start, end):
        return not self.is_closed(start, end)

    def is_closed(self, start, end):
        """A walk is considered closed if the first and last
        vertices are the same, open if not."""
        if start == end:
            return True
        res = self.walk(start, end)
        return res[0] == res[::-1]

    def is_trail(self, start, end):
        """A trail is a walk in which all the edges are distinct."""
        res = self.walk(start, end)
        return len(res) == len(set(res))

    def tour_hamiltonian(self):
        pass

    def tour_eulerian(self):
        pass


class DirectedGraph(Graph):
    pass


def _rand_edges(num_edges):
    global all_vertices

    def _graph(num_edges):
        return [choice(all_vertices) for _ in range(num_edges)]
    edges = set(_graph(num_edges))

    # Since it's random, force unique graph
    while len(edges) < num_edges:
        edges = set(_graph(num_edges))
    return list(edges)


def _test_walk_valid(graph):
    valid = False
    while not valid:
        start = choice(all_vertices)
        end = choice(all_vertices)
        res = graph.walk(start, end)
        if len(res) > 0:
            return 'walk of {}, {} = {}'.format(start, end, res)
            valid = True

if __name__ == '__main__':
    with Section('Basic graph'):
        graph = Graph()
        # Initial seeding
        for _ in range(5):
            graph[choice(all_vertices)] = _rand_edges(MAX_EDGES)

        test_graph = Graph({
            0: [1, 2],
            1: [2, 0],
            2: [0]
        })
        print(test_graph.walk(1, 2))
        assert len(test_graph.walk(0, 3)) == 0  # non-existent node
        assert len(test_graph.walk(2, 1)) == 3
        assert not test_graph.is_closed(1, 2)
        assert test_graph.is_closed(0, 0)

        _print('Generated graph', graph.vertices, func=ppr)
        _print('walk of...', _test_walk_valid(graph))

        deg, vertex = randrange(0, MAX_EDGES), choice(all_vertices)
        print('Has degree {} ... {}? {}'.format(
            deg, vertex, graph.has_degree(deg, vertex)))

        for _ in range(5):
            try:
                _print('connections', graph.connections(choice(all_vertices)))
            except InvalidGraphRepresentation:
                print(
                    'Invalid graph was generated -- need more than 2 vertices')
        for node in graph:
            print('Node {} has degree {}'.format(node, graph.degree(node)))
        _print('graph', graph)
        _print('Has multiple degrees?', graph.has_multiple_degrees(1))

    with Section('Directed Graph'):
        digraph = DirectedGraph()
        for n in range(MAX_VERTICES):
            digraph[n] = _rand_edges(MAX_EDGES)
        _print('Generated directed-graph', digraph.vertices, func=ppr)
        _print('Digraph', digraph)
        _print('Get item:', digraph[4])
        digraph[3] = [3, 2, 5]
        _print('Set item:', digraph[3])
        del digraph[2]
        _print('Del item:', digraph)
        _print('walk of...', _test_walk_valid(digraph))

        test_digraph = DirectedGraph({
            0: [1, 2],
            1: [2, 0],
            2: [0]
        })
        print(test_digraph)
