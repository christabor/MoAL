# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import _print
from pprint import pprint as ppr
from random import randrange
from copy import deepcopy
from random import choice

# wikipedia.org/wiki/Glossary_of_graph_theory
# and cs.hmc.edu/~keller/courses/cs60/s98/examples/acyclic

MAX_VERTICES = 6
MAX_EDGES = MAX_VERTICES / 2
all_vertices = range(0, MAX_VERTICES)


class InvalidGraphRepresentation(Exception):
    pass


class Graph(object):

    def __len__(self):
        return len(self.vertices.keys())

    def __init__(self, vertices=None):
        self.vertices = vertices or {}

    def __contains__(self, vertex):
        return vertex in self.vertices

    def __setitem__(self, vertex, edges):
        self.vertices[vertex] = edges

    def __delitem__(self, vertex):
        # Remove entire node
        if vertex not in self.vertices:
            return
        del self.vertices[vertex]
        # Remove other references.
        for _vertex in self.vertices:
            if vertex in self.vertices[_vertex]:
                self.vertices[_vertex].remove(vertex)

    def __getitem__(self, vertex):
        return self.vertices[vertex]

    def __iter__(self):
        return iter(self.vertices)

    def __str__(self):
        display = []
        for vertex, vertices in self.vertices.iteritems():
            display.append('{outbound} <-- ({vertex})'.format(
                vertex=vertex, outbound=vertices))
        return ',\n'.join(display)

    def all_vertices(self, unique=True):
        """Return all vertices in the graph, including duplicate
        references; remove duplicates if `unique` is true."""
        vertices = self.vertices.keys()
        for vals in self.vertices.values():
            vertices = vertices + vals
        return list(set(vertices)) if unique else vertices

    def degree(self, vertex):
        """Return the number of edges for a given vertex.
        Only allows string/integer/tuple vertices."""
        if isinstance(vertex, int) \
                or isinstance(vertex, str) \
                or isinstance(vertex, tuple):
            return len(self.vertices[vertex]) if vertex in self.vertices else 0
        return 0

    def has_degree(self, vertex, degrees):
        return self.degree(vertex) == degrees

    def has_multiple_degrees(self, vertex):
        return self.degree(vertex) > 1

    def is_open(self, start, end):
        return not self.is_closed(start, end)

    def is_closed(self, start, end):
        """A walk is considered closed if the first and last
        vertices are the same, open if not. This is also known as a cycle."""
        if start == end:
            return True
        res = self.walk(start, end, test_cycle=True)
        if len(res) == 0:
            return True
        return res[0] == res[::-1]

    def is_leaf(self, vertex):
        """A leaf vertex is a vertex with no outbound edges."""
        return self.degree(vertex) == 0

    def walk(self, start, end, path=[], test_cycle=False):
        path = path + [start]
        paths = []

        if test_cycle:
            end = start

        if start == end and not test_cycle:
            return path

        if test_cycle and path[::-1] == start:
            return paths

        if start in self.vertices.keys():
            for vertex in self.vertices[start]:
                # Add new vertex if it's not in the list already.
                if vertex not in path:
                    # Get new path from this vertex
                    paths += self.walk(
                        vertex, end, path=path, test_cycle=test_cycle)
        return paths

    def is_cycle(self, vertex):
        return self.walk(vertex, None, test_cycle=True)

    def is_acycle(self, vertex):
        return not self.is_cycle(vertex)

    def is_cyclic(self):
        return not self.is_acyclic()

    def is_acyclic(self):
        """A graph is acyclic if:
        * It has no vertices to begin with.
            [OR]
        * If continual removal of leaf nodes and
            updating of arcs leaves no vertices.
        If there is a non-leaf node left, the graph IS cyclic.
        """
        # A graph with no vertices is automatically acyclic.
        if len(self.vertices) == 0:
            return True
        # A graph with NO leaf nodes is cyclic.
        leaves = len([self.is_leaf(vertex) for vertex in self.vertices])
        # Keep a backup of the original graph.
        graph_copy = deepcopy(self.vertices)
        if leaves == 0:
            return False
        _print('Directed Acyclic graph check', '')
        while len(self.vertices.keys()) > 1:
            vertices = self.vertices.keys()
            # Skip ahead if there's only one vertex left.
            start = choice(vertices)
            print('Checking cycle... start={}, {}'.format(start, self.vertices))
            # Otherwise, keep checking cycles and deleting nodes.
            if self.is_cycle(start):
                return False
            else:
                self.__delitem__(start)
        # Restore backup
        nodes_left = len(self.vertices.values()[0])
        acyclic = True if nodes_left == 0 else False
        print('All cycles checked. Graph {} acyclicity = {}'.format(
            self.vertices, acyclic))
        self.vertices = graph_copy
        # If a cycle wasn't already found above, it's guaranteed to be acyclic.
        return acyclic

    def is_trail(self, start, end):
        """A trail is a walk in which all the edges are distinct."""
        res = self.walk(start, end)
        return len(res) == len(set(res))

    def is_bipartite(self, start, end):
        pass

    def tour_hamiltonian(self):
        pass

    def tour_eulerian(self):
        pass


class DirectedGraph(Graph):
    pass


class CyclicGraph(Graph):
    pass


class DirectedCyclicGraph(DirectedGraph, CyclicGraph):
    pass


class DirectedAcyclicGraph(DirectedGraph, CyclicGraph):
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


if __name__ == '__main__':
    with Section('Basic graph'):
        graph = Graph({
            0: [1, 2],
            1: [2, 0],
            2: [0]
        })
        assert len(graph.walk(0, 3)) == 0  # non-existent node
        assert len(graph.walk(2, 1)) == 3  # unreachable node
        assert graph.is_closed(1, 2)  # Cycle
        assert graph.is_closed(0, 0)  # Trivial cycle
        assert graph.is_closed(2, 1)  # Cycle

        _print('Generated graph', graph.vertices, func=ppr)
        deg, vertex = randrange(0, MAX_EDGES), choice(all_vertices)
        print('Has degree {} ... {}? {}'.format(
            deg, vertex, graph.has_degree(deg, vertex)))

        for vertex in graph:
            print('Vertex {} has degree {}'.format(
                vertex, graph.degree(vertex)))
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
        digraph = DirectedGraph({
            1: [2],
            2: [3, 4],
            3: [],  # intentionally empty
            4: [5, 6],
            5: [6],
            6: [3]
        })
        deg_test = [(1, 1), (2, 2), (3, 0), (4, 2), (5, 1), (6, 1)]
        for degs in deg_test:
            assert digraph.has_degree(*degs)
        assert digraph.is_acyclic()
        digraph[6] = [3, 4]  # Create cyclic graph
        digraph[4] = [5]

        dcg = DirectedCyclicGraph({
            1: [2, 3, 1],
            2: [1, 3, 2],
            3: [1, 2, 3]
        })
        assert dcg.is_cyclic()
