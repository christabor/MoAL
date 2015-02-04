# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import Section
from random import choice
from string import ascii_uppercase

MAX_VERTICES = 10
DEBUG = False


class InvalidGraphRepresentation(Exception):
    pass


class Graph:

    def __init__(self, nodes=None):
        self.nodes = nodes or {}

    def __setitem__(self, node, edges):
        self.nodes[node] = edges

    def __delitem__(self, edge):
        del self.nodes[edge]

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
        return self.view()

    def view_path(self, *args, **kwargs):
        vertices = self.__getitem__(*args, **kwargs)
        if len(vertices) > 2:
            return '({}) -> {} -> ({})'.format(
                vertices[0], ' -> '.join(vertices[1:-1]), vertices[-1])
        else:
            raise InvalidGraphRepresentation('Need more than 2 vertices.')

    def view(self):
        display = []
        for vertex, nodes in self.nodes.iteritems():
            sub_nodes = ''
            for node in nodes:
                sub_nodes += ' --> {}'.format(node)
            display.append('({}){}'.format(vertex, sub_nodes))
        return ',\n'.join(display)

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

    def __setitem__(self, *args, **kwargs):
        vertex, info = args
        self.nodes[vertex] = info

    def __str__(self):
        return self.view()

    def view(self):
        display = []
        arrows = {'to': '-->', 'from': '<--', 'bi-directional': '<-->'}
        for vertex, nodes in self.nodes.iteritems():
            for sub_node in nodes['key']:
                sub_nodes = ' {} {}'.format(
                    arrows[nodes['direction']], sub_node)
                display.append('({}){}'.format(vertex, sub_nodes))
        return ',\n'.join(display)


def _seed_choice(choices, times):
    return [choice(choices) for _ in range(times)]


def _rand_path(length=4):
    if length > 4:
        length = 4
    return _seed_choice(ascii_uppercase, length)


if DEBUG:
    with Section('Basic graph'):
        vertices = ['A', 'B', 'C', 'D', 'E']
        graph = Graph()
        # Initial seeding
        for _ in range(10):
            graph[choice(vertices)] = _seed_choice(vertices, 4)
        print 'Graph', graph[('A', 'B')]

        for _ in range(10):
            try:
                print '\n', graph.view_path(
                    (choice(vertices), choice(vertices)))
            except InvalidGraphRepresentation:
                print 'Invalid graph was generated'

        for node in graph:
            print 'Node {} has degree {}'.format(node, graph.get_degree(node))

        graph.view()
        print 'Has multiple degrees?', graph.has_multiple_degrees()


if DEBUG:
    with Section('Directed Graph'):
        digraph = DirectedGraph()
        for _ in range(MAX_VERTICES):
            digraph[choice(ascii_uppercase)] = {
                'key': _rand_path(),
                'direction': choice(['to', 'from', 'bi-directional'])
            }
        print 'digraph', digraph
        try:
            print digraph.view_path((choice(vertices), choice(vertices)))
        except InvalidGraphRepresentation:
            print 'Invalid graph was generated'
