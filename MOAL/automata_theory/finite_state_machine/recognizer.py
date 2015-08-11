# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.automata_theory.finite_state_machine import fsm

DEBUG = True if __name__ == '__main__' else False


class Recognizer(fsm.Acceptor):

    def _xform(self, edge):
        return edge

    def recognize(self, digits):
        return 'Yes' if super(Recognizer, self).test(digits) else 'No'


class RegularExpression(Recognizer):
    pass


if DEBUG:
    with Section('Finite State Machine - Recognizer'):
        # From example:
        # en.wikipedia.org/wiki/Finite-state_machine#
        #     /media/File:Fsm_parsing_word_nice.svg
        stringrec = Recognizer(states={
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

    with Section('Finite State Machine - Regular Expression'):
        base = {
            '0': 'S1', '1': 'S2',
            '2': 'S3', '3': 'S4',
            '4': 'S5', '5': 'S6',
            '6': 'S7', '7': 'S8',
            '8': 'S9', '9': 'S10',
            '': 'A',
            None: 'Error'
        }
        re_digits = RegularExpression(states={
            'S0': {'transitions': base},
            'S1': {'transitions': base},
            'S2': {'transitions': base},
            'S3': {'transitions': base},
            'S4': {'transitions': base},
            'S5': {'transitions': base},
            'S6': {'transitions': base},
            'S7': {'transitions': base},
            'S8': {'transitions': base},
            'S9': {'transitions': base},
            'S10': {'transitions': base},
            'A': {'transitions': None, 'accepting': True},
            'Error': {'transitions': None, 'rejecting': True},
        }, default='S0')
        assert re_digits.test('1')
        assert re_digits.test('0')
        assert re_digits.test('9999')
        assert re_digits.test('1234567890')
        assert re_digits.test('0987654321')
        assert not re_digits.test('qwerty')
        assert not re_digits.test('!@#$%^')
