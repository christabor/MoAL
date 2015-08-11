# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.automata_theory.finite_state_machine import fsm

DEBUG = True if __name__ == '__main__' else False


class Rcognizer(fsm.Acceptor):

    def _xform(self, edge):
        return edge

    def recognize(self, digits):
        return 'Yes' if super(Rcognizer, self).test(digits) else 'No'


if DEBUG:
    with Section('Finite State Machine'):
        # From example:
        # en.wikipedia.org/wiki/Finite-state_machine#
        #     /media/File:Fsm_parsing_word_nice.svg
        stringrec = Rcognizer(states={
            'S1': {'transitions': {'n': 'S2', None: 'Error'}},
            'S2': {'transitions': {'i': 'S3', None: 'Error'}},
            'S3': {'transitions': {'c': 'S4', None: 'Error'}},
            'S4': {'transitions': {'e': 'Accept', None: 'Error'}},
            'Error': {'transitions': None, 'rejecting': True},
            'Accept': {'transitions': None, 'accepting': True}
        }, default='S1')
        assert stringrec.recognize('nice') == 'Yes'
        assert stringrec.recognize('nic3') == 'No'
        assert stringrec.recognize('nicee') == 'No'
        assert stringrec.recognize('_nice') == 'No'
        # Delete a node
        del stringrec['S4']
        assert stringrec.recognize('nice') == 'No'
