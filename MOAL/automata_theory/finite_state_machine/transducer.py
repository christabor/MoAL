# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import divider
from MOAL.helpers.display import print_h2
from MOAL.automata_theory.finite_state_machine import fsm
from string import ascii_lowercase as letters
from random import choice

DEBUG = True if __name__ == '__main__' else False


class Transducer(fsm.FiniteStateMachine):

    def __init__(self, *args, **kwargs):
        self.debug = kwargs.pop('debug') if 'debug' in kwargs else False
        # Used for stopping any non-halting auto-generated FSMs
        self.max = kwargs.pop('max') if 'max' in kwargs else 20
        super(Transducer, self).__init__(*args, **kwargs)
        self.string = ''
        self.value = ''

    def get_next_value(self, node, edge):
        if node not in self.states:
            return None
        _node = self.states[node]['transitions']
        if _node is None or edge not in _node:
            return None
        return _node[edge]

    def run_all(self):
        for node, data in self.states.iteritems():
            divider(newline=False)
            if data['transitions'] is None:
                continue
            for transition in data['transitions']:
                self.run(node=node, edge=transition)

    def run(self, node=None, edge=None):
        self.step = 0
        if node is None:
            node = self.default
        current_node = self.get_next_value(node, edge)
        if self.debug:
            print('Running - current value/node: {} -> {}'.format(edge, node))
        while current_node is not None:
            if self.step >= self.max:
                break
            edge, node = current_node.split(':')
            if self.debug:
                spaces = self.step * '  '
                print('{} New value/node: {} -> {}'.format(spaces, edge, node))
            current_node = self.get_next_value(node, edge)
            self.string += edge
            self.step += 1
        print('Final string value: {}'.format(self.string))
        val = self.string
        # Reset
        self.string = ''
        return val


def generate_transducer(nodes=10, alphabet=None):
    def _transitions(transitions_per_node, nodes):
        return {
            'transitions': {
                choice(alphabet): '{}:{}'.format(
                    choice(alphabet), choice(nodes)) for n in xrange(
                        transitions_per_node)}}

    if alphabet is None:
        alphabet = [choice(letters) for n in xrange(nodes)]
    nodes = ['S{}'.format(n) for n in xrange(nodes)]
    # Turning up `transitions_per_node` will increase the likelihood of
    # longer, more interesting strings (and non-halting states too!)
    edges = {node: _transitions(5, nodes) for node in nodes}
    return edges


def run_random_transducer(**kwargs):
    schema = generate_transducer(**kwargs)
    transducer = Transducer(states=schema, default='S0')
    transducer.run_all()


if DEBUG:
    with Section('Finite State Machine - Transducer'):
        # Recreation of http://www-01.sil.org/pckimmo/v2/doc/Figure-A3.gif
        transducer = Transducer(states={
            'S1': {'transitions': {'a': 'a:S2'}, 'val': 'Start'},
            'S2': {'transitions': {'b': 'b:S3', 'a': 'a:S4'}},
            'S3': {'transitions': {'a': 'a:S4', 'b': 'c:S2'}},
            'S4': {'transitions': None},
        }, default='S1', debug=True)
        print_h2('Running all edge transitions')
        transducer.run_all()
        # Made up
        transducer = Transducer(states={
            'S0': {'transitions': {'c': 'a:S1', 'd': 'e:S2'}, 'val': 'Start'},
            'S1': {'transitions': {'p': 'i:S3', 'h': 'o:S4'}},
            'S2': {'transitions': {'e': 'a:S3'}},
            'S3': {'transitions': {'d': 'e:S4', 'a': 'c:S0'}},
            'S4': {'transitions': None},
        }, default='S0', debug=True)
        print_h2('Running all edge transitions')
        transducer.run_all()
        # Fully automated, non-deterministic - which may lead to non-halting
        # or invalid states when testing.
        run_random_transducer()
