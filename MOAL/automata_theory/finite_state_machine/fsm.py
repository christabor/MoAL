# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import print_error
from MOAL.helpers.display import print_info
from MOAL.helpers.display import divider

DEBUG = True if __name__ == '__main__' else False


class InvalidTransition:
    pass


class FiniteStateMachine(object):

    def __init__(self, states={}, default=None):
        self.states = states
        self.default = default
        self.current = self.default
        self.step = 0

    def __getitem__(self, state):
        return self.states[state]

    def __delitem__(self, state):
        del self.states[state]

    def __setitem__(self, state, data):
        self.states[state] = data

    def __str__(self):
        for node, data in self.states.iteritems():
            print('State {}'.format(node))
            for state, transition in data['transitions'].iteritems():
                print('  {} --> ({})'.format(state, transition))
            divider(newline=False)
        return ''

    def _get_transition(self, edge):
        try:
            return self.states[self.current]['transitions'][int(edge)]
        except KeyError:
            raise InvalidTransition

    def _get_current(self):
        return self.current, self.states[self.current]

    def transition(self, edge):
        old, old_data = self._get_current()
        self.current = self._get_transition(edge)
        new, new_data = self._get_current()
        print('{} Transition: {} ({} -> {})'.format(
            self.step * ' ', edge, old, new))


class BinaryAcceptor(FiniteStateMachine):

    def test(self, digits):
        try:
            print_info('+ TESTING: {}'.format(digits))
            _digits = list(str(digits))
            for digit in _digits:
                self.step += 1
                self.transition(digit)
            self.step = 0
            return True
        except InvalidTransition:
            print_error('Not found: {}'.format(digits))
            return False

if DEBUG:
    with Section('Finite State Machine'):
        # Example creation of
        # en.wikipedia.org/wiki/Finite-state_machine#/media/File:DFAexample.svg
        acceptor = BinaryAcceptor(
            states={
                'S1': {'transitions': {0: 'S2', 1: 'S1'}, 'val': 'End node'},
                'S2': {'transitions': {0: 'S1', 1: 'S2'}, 'val': 'Start node'}},
            default='S1')
        assert acceptor.test('01100101011')
        assert acceptor.test('11')
        assert not acceptor.test('113')
        assert acceptor.test('1110001010')
