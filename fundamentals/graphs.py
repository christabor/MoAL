# Mostly taken from
# interactivepython.org/runestone/static/pythonds/Trees/balanced.html

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import section
from random import choice
from string import ascii_uppercase

MAX_VERTICES = 10


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

    def view_path(self, *args, **kwargs):
        vertices = self.__getitem__(*args, **kwargs)
        if len(vertices) > 2:
            print '({}) -> {} -> ({})'.format(
                vertices[0], ' -> '.join(vertices[1:-1]), vertices[-1])

    def view(self):
        for vertex, nodes in self.nodes.iteritems():
            sub_nodes = ''
            for node in nodes:
                sub_nodes += ' --> {}'.format(node)
            print '({}){}'.format(vertex, sub_nodes)

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

    def view(self):
        arrows = {'to': '-->', 'from': '<--', 'bi-directional': '<-->'}
        for vertex, nodes in self.nodes.iteritems():
            for sub_node in nodes['key']:
                sub_nodes = ' {} {}'.format(
                    arrows[nodes['direction']], sub_node)
                print '({}){}'.format(vertex, sub_nodes)


def _seed_choice(choices, times):
    return [choice(choices) for _ in range(times)]


def _rand_path(length=4):
    return _seed_choice(ascii_uppercase, length)

section('BEGIN - Basic graph')

vertices = ['A', 'B', 'C', 'D', 'E']
graph = Graph()
for _ in range(10):
    graph[choice(vertices)] = _seed_choice(vertices, 2)

# __getitem__ style
print graph[('A', 'B')]

# Function call style
for _ in range(10):
    print
    graph.view_path((choice(vertices), choice(vertices)))
    print

for node in graph:
    print 'node (iter):', node
    print 'Node {} has degree {}'.format(node, graph.get_degree(node))

graph.view()
print 'Has multiple degrees?', graph.has_multiple_degrees()

section('BEGIN - Directed Graph')

digraph = DirectedGraph()
for _ in range(MAX_VERTICES):
    digraph[choice(ascii_uppercase)] = {
        'key': _rand_path(),
        'direction': choice(['to', 'from', 'bi-directional'])
    }

print 'digraph'
digraph.view()
digraph.view_path((choice(vertices), choice(vertices)))

section('END - Graphs')
