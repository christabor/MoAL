"""Graph canonization algorithm(s).

As an ascii graph (tree, in this case.)
     a
     O
     | 1
  2 / \ 3
  b O  O c
 4 / \ 5
e O   O f

As a dict.
g = {
    'a': ['b', 'c'],
    'b': ['e', 'f'],
    'c': [],
    'e': [],
    'f': []
}

Made up canonized format. Pipes act as delimiters.
g=a>[b,c]|b>[e,f]|c>[]|f>[]|
"""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section

DEBUG = True if __name__ == '__main__' else False


def canonize_graph(graph):
    """Convert a graph into a canonized string form.

    Args:
        graph (dict): A dictionary of labels and lists of edges for the graph.

    Returns:
        str: The canonized graph string.
    """
    canonized = 'g='
    for node, edges in graph.iteritems():
        canonized += '{}>{}|'.format(node, ','.join(edges))  # Removes spaces
    return canonized


def decanonize_graph(graphstr):
    """Convert a string representation of a graph into an actual dictionary.

    Args:
        graphstr (str): The graph string in graph canonized form.

    Raises:
        ValueError: Raised if string does not start with 'g='

    Returns:
        dict: The "de-canonized" graph.
    """
    graph = {}
    if not graphstr.startswith('g='):
        raise ValueError('Invalid graph canonization format!')
    for segment in graphstr.replace(' ', '').split('|'):
        if '=' in segment:
            index = list(segment).index('=')
            segment = segment[index + 1:]
        pieces = segment.split('>')
        if len(pieces) < 2:
            continue
        node, edges = pieces
        if not edges:
            graph[node] = []
        else:
            graph[node] = [e for e in edges.split(',')]
    return graph


if DEBUG:
    with Section('Graph canonization algorithm'):
        graph = {
            'a': ['b', 'c'],
            'b': ['e', 'f'],
            'c': [],
            'e': [],
            'f': ['g', 'h', 'i'],
            'g': [],
            'h': [],
            'i': []
        }
        can = canonize_graph(graph)
        decan = decanonize_graph(can)
        assert graph == decan
        print('Original: {}\nCanonized: {}\nDecanonized: {}'.format(
            graph, can, decan))
