# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from helpers.display import _cmd_title
from pprint import pprint as ppr
from helpers.adts import strlist
from data_structures.graphs.graphs import DirectedGraph
import time

# Definition, variations and example instruction set
# http://en.wikipedia.org/wiki/Pointer_machine


class PointerMachine(object):

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return type(self).__name__

    def __init__(self, word=None):
        self.DEBUG = False
        # Time delay, only used for only demonstration effect.
        self.DELAY = 0.2
        self._step = 0
        self.halted = False
        self.word = word

    def halt(self):
        if self.DEBUG:
            _cmd_title('Halting')
        self.halted = True

    def run_instruction(self, instruction):
        if self.DEBUG:
            print('Step ... #{} with instruction {} in register {}'.format(
                self._step, instruction['code'], self.curr_register))
            time.sleep(self.DELAY)
        # Prevent running if halted.
        if self.halted:
            return
        self._step += 1

    def run(self):
        raise NotImplementedError


"""[From Wikipedia:]
"At least three major varieties exist in the literature:
    * Kolmogorov-Uspenskii model (KUM, KU-machine),
    * Knuth linking automaton
    * Schönhage Storage Modification Machine model (SMM).

The SMM seems to be the most common."
http://en.wikipedia.org/wiki/Pointer_machine#Types_of_.22Pointer_Machines.22
"""


class SchonhageStorageModification(PointerMachine):

    def __init__(self, *args, **kwargs):
        super(SchonhageStorageModification, self).__init__(*args, **kwargs)
        self.DEBUG = False
        self.graph = DirectedGraph()
        if 'word' in kwargs:
            self.TEST_WORD = kwargs['word']
        else:
            self.TEST_WORD = 'Schonhage'
        self.word = strlist(list(self.TEST_WORD))  # TEST

        self.curr_key = 0
        self.curr_val = self.word[self.curr_key]
        self.output = self.curr_val

        # Setup initial graph with default word.
        self.recalculate()
        # Get node after the paths have been created.
        self.curr_node = self.graph[self.curr_key]

    def __setitem__(self, *args):
        """Adds a new node to the graph."""
        item, connections = args
        self.graph[item] = connections

    def __getitem__(self, key):
        """A wrapper that loops over the internal graph."""
        # Skip loop if possible.
        if self.curr_node['val'] == key:
            return self.curr_node
        # Check all other nodes.
        for k, node in self.graph.iteritems():
            try:
                if node['val'] == key:
                    return node
            except KeyError:
                continue

    def _show_edges(self, node):
        """A debug method to nicely show all edges for a given node key"""
        for state, edge in self.graph[node]['edges'].iteritems():
            '[SHOW EDGE] {} ... {} --> {}'.format(node, state, edge['to'])

    def recalculate(self):
        """Draws/redraws the graph, taking the current value
        and assigning the nodes / paths accordingly.
        Assigns the edge values for each node, and
        updates the value for each symbol in the word as well.

        In the example {0, 1} symbol set machine, each node can have a 0, 1,
        or both 0 and 1 edges, which allow for the instructions
        to be dictated by traversing the graph.

        In a traditional directed graph, nodes are either inbound, or outbound.
        In the SMM, the edges define the direction, but they also encode
        the state symbols that can be used to determine behavior in a way
        that operates like tape, cells, and state in a Turing machine.

        An example graph looks like this:

        graph = {
            0: ...,
            1: {'val': 'A', 'edges': {0: {'to': 0}, 1: {'to': 2},},
            2: ....
        }

        The key is the node, and is used as a pointer to other nodes.
        The edges attribute is a dictionary, keyed by each edge
        that corresponds to all symbol states (e.g. {0, 1} in the example).
        Each key points to a dictionary, representing the node to move to.
        """
        end = len(self.word)
        # Special case for single nodes.
        if end == 1:
            self.graph[0] = {
                'key': 0,
                'val': self.word,  # guaranteed to only be one character
                'edges': {0: {'to': 0}, }
            }
        else:
            for key, val in enumerate(self.word):
                self.graph[key] = {
                    'key': key,
                    'val': val,
                    'edges': {}
                }
                # The first nodes 0-edge points to itself,
                # and the 1-edge points to the next node.
                if key == 0:
                    self.graph[key]['edges'] = {
                        0: {'to': 0},
                        1: {'to': key + 1}}
                # The last nodes 0 and 1 edges
                # BOTH point to the previous node.
                elif key == end - 1:
                    self.graph[key]['edges'] = {
                        0: {'to': key - 1},
                        1: {'to': key - 1}}
                # All others; 0-edge points to the previous,
                # 1-edge points to the next.
                else:
                    self.graph[key]['edges'] = {
                        0: {'to': key - 1},
                        1: {'to': key + 1}}
        if self.DEBUG:
            prnt('Graph', self.graph.vertices, func=ppr)

    def new(self, val):
        """Adds a new value to the word"""
        # Handle recalculation by simply adding the
        # new words and calling function again.
        for token in list(val):
            self.word += token
            # Adjust edges to / from each node
            self.recalculate()
        if self.DEBUG:
            print('word with new item(s) {}'.format(self.word))
        # Make this one chain-able.
        return self

    def _get_path(self, word):
        """Returns a list of nodes representing the
        path traveled for a given word."""
        path = []
        for char in word:
            path.append(self.graph[char][1])
        return path

    def jump(self, word1, word2, jump_node):
        """Get the two paths to compare their ending nodes.
        Compare the two paths to see if they end in the same node. If so, jump.
        """
        if self._get_path(word1)[-1:] == self._get_path(word2)[-1:]:
            self.curr_node = jump_node
            self._run_step()
            if self.DEBUG:
                print('{} {} paths are equal. Jumping to node {}'.format(
                    word1, word2, jump_node))

    def set(self, node, val):
        """Sets a nodes value to the new value."""
        self.graph[node]['val'] = val
        # Recalculation to determine where nodes
        # point is done in one place, using the same technique
        # as when the graph is initially created.
        self.recalculate()

    def _update_state(self):
        # Take the 1-edge, neo
        new_node_key = self.curr_node['edges'][1]['to']
        self.curr_node = self.graph[new_node_key]
        self.curr_val = self.curr_node['val']
        self.curr_key = self.curr_node['key']

    def _run_step(self):
        if self.DEBUG:
            prnt('curr node (before):', self.curr_node, func=ppr)

        time.sleep(self.DELAY)
        # Visually update
        if self.DEBUG:
            prnt('curr node (after):', self.curr_node, func=ppr)

        self._update_state()
        if self.curr_node is not None:
            # Add to the string as the program runs.
            self.output += self.curr_val

    def traverse_word(self):
        prnt('Graph nodes beginning', self.graph.vertices, func=ppr)
        start, end = 0, len(self.word)
        while start < end:
            # Print must come before next step,
            # otterwise it will print the letters shifted.
            print('Counter: {}, Output: {}, Curr val: {}, Curr key: {}'.format(
                start, self.output, self.curr_val, self.curr_key))
            self._run_step()
            start += 1

    def run(self):
        self.traverse_word()


class KolmogorovUspenskii(SchonhageStorageModification):
    """[From Wikipedia:]
    "KUM differs from SMM in allowing only invertible pointers:
       [for every pointer from a node x to a node y, an inverse pointer
        from y to x must be present. Since outgoing pointers must be labeled
        by distinct symbols of the alphabet, both KUM and SMM graphs
        have O(1) outdegree. However, KUM pointers' invertibility restricts
        the in-degree to O(1), as well.]

    An additional difference is that the KUM was intended
    as a generalization of the Turing machine, and so it allows
    the currently "active" node to be moved around the graph.
    Accordingly, nodes can be specified by individual characters
    instead of words, and the action to be taken can be determined
    by a state table instead of a fixed list of instructions." """

    def __init__(self, *args, **kwargs):
        super(KolmogorovUspenskii, self).__init__(
            *args, word='KolmogorovUspenskii')

    def recalculate(self):
        end = len(self.word)
        # Special case for single nodes.
        if end == 1:
            self.graph[0] = {
                'key': 0,
                'val': self.word,  # guaranteed to only be one character
                # KUM always has both 0, and 1-edges, on all nodes.
                'edges': {0: {'to': 0}, 1: {'to': 0}}
            }
        else:
            for key, val in enumerate(self.word):
                self.graph[key] = {
                    'key': key,
                    'val': val,
                    'edges': {}
                }
                # The first nodes 0-edge points to itself,
                # and the 1-edge points to the next node.
                if key == 0:
                    self.graph[key]['edges'] = {
                        0: {'to': 0},
                        1: {'to': key + 1}}
                # The last nodes 0 and 1 edges
                # BOTH point to the previous node.
                elif key == end - 1:
                    self.graph[key]['edges'] = {
                        0: {'to': key - 1},
                        1: {'to': key - 1}}
                # All others; 0-edge points to the previous,
                # 1-edge points to the next.
                else:
                    self.graph[key]['edges'] = {
                        0: {'to': key - 1},
                        1: {'to': key + 1}}

                if self.DEBUG:
                    self._show_edges(key)


class KnuthLinking(PointerMachine):
    """[From Wikipedia:]
    "According to Schoenhage, Knuth noted that the SMM model
    coincides with a special type of "linking automata"
    briefly explained in volume one of 'The Art of Computer Programming'" """


class AtomisticPureLISP(PointerMachine):
    pass


class AtomisticFullLISP(PointerMachine):
    pass


class GeneralAtomistic(PointerMachine):
    pass


class JonesIOne(PointerMachine):
    pass


class JonesITwo(PointerMachine):
    pass


if __name__ == '__main__':
    with Section('Pointer Machines'):
        classes = [
            KolmogorovUspenskii,
            KnuthLinking,
            SchonhageStorageModification,
            AtomisticPureLISP, AtomisticFullLISP,
            GeneralAtomistic,
            JonesIOne, JonesITwo,
        ]

        for _class in classes:
            # Decouple abstract class / stubbing from demo by suppression.
            try:
                _cmd_title('Testing machine... {}'.format(repr(_class)))
                _class().run()
            except NotImplementedError:
                continue
