# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h4
from collections import namedtuple

DEBUG = True if __name__ == '__main__' else False


class InvalidStringLength:
    pass


class AnalyticContextFreeGrammar:
    pass


class TDPLAnalyticCFG(AnalyticContextFreeGrammar):
    """For a formal definition and examples, see
    wikipedia.org/wiki/Top-down_parsing_language"""

    @staticmethod
    def adjacent_intersection(str1, str2):
        matches, index = 0, 0
        if len(str1) > len(str2):
            raise InvalidStringLength
        for letter in str1:
            if str2[index] != letter:
                return matches
            matches += 1
            index += 1
        return matches

    @staticmethod
    def intersection(str1, str2):
        matches, index = 0, 0
        others = list(str2)
        for letter in str1:
            if letter in others:
                matches += 1
            index += 1
        return matches

    @staticmethod
    def evaluate(start, rules, terminals):
        # index = 0
        start = list(start)
        for token in start:
            if token in rules:
                if token in terminals:
                    raise Exception
                start += rules[token]
        return ''.join(start)

    @staticmethod
    def _evaluate_all(start, rules=[], terminals=[]):
        """Non-recursive simple function, for first iteration."""
        lefts = rules.keys()
        copy = ''
        for token in list(start):
            if token in lefts:
                if rules[token] in terminals:
                    # Break out, as we are done with all evaluations
                    return copy
                token = rules[token]
                copy += token
        return copy

    @staticmethod
    def evaluate_with_defaults(
        start, nonterminals=['a', 'x', 'B', 'S', '#', 'b'],
            terminals=['!'], ruleset=None):
        if not ruleset:
            ruleset = {
                'B': 'a',
                'S': 'ba',
                'a': 'Sx',
                'x': '!',
                '#': '!'
            }
        Tdpl = namedtuple('TDPL', ['nonterminals', 'terminals', 'ruleset'])
        tdpl = Tdpl(
            nonterminals=set(nonterminals),
            terminals=set(terminals),
            ruleset=ruleset
        )
        terminals = getattr(tdpl, 'terminals')
        ruleset = getattr(tdpl, 'ruleset')
        return TDPLAnalyticCFG._evaluate_all(
            start, rules=ruleset, terminals=terminals)

    @staticmethod
    def test_grammar(times, start, **kwargs):
        # Run it n times, so we limit any infinite regresses
        pumped = ''
        for x in xrange(times):
            if DEBUG:
                print('Start: {}'.format(start))
                print('pumped string: {}'.format(pumped))
            start = TDPLAnalyticCFG.evaluate_with_defaults(start, **kwargs)
            pumped += start
        return start, pumped


if DEBUG:
    with Section('Analytic CFG - Top Down Parsing Language (TPDL)'):
        # We'll use a more formal mapping of data
        #   (wikipedia.org/wiki/Top-down_parsing_language
        #       #Definition_of_a_TDPL_grammar)
        tdpl = TDPLAnalyticCFG

        assert tdpl.adjacent_intersection('laughter', 'slaughter') == 0
        assert tdpl.adjacent_intersection('cats', 'catholic') == 3
        assert tdpl.adjacent_intersection('crate', 'crater') == 5

        assert tdpl.intersection('rad', 'radio') == 3
        assert tdpl.intersection('crud', 'crude') == 4
        assert tdpl.intersection('drawing', 'drowning') == 6

        # Degenerate cases - single iteration
        assert tdpl.evaluate_with_defaults('B') == 'a'
        assert tdpl.evaluate_with_defaults('S') == 'ba'
        assert tdpl.evaluate_with_defaults('a') == 'Sx'
        assert tdpl.evaluate_with_defaults('x') == ''
        assert tdpl.evaluate_with_defaults('#') == ''

        tdpl.test_grammar(10, 'B')
        kwargs = {
            'terminals': ['#'],
            'nonterminals': ['l', 'o'],
            'ruleset': {
                'o': 'l',
                'l': 'oL',
                'L': 'O',
                'O': 'l',
            }
        }

        tdpl.test_grammar(5, 'xo', **kwargs)
        kwargs = {
            'terminals': [],
            'nonterminals': ['0', '1'],
            'ruleset': {
                '1': '010',
                '0': '101',
            }
        }

        tdpl.test_grammar(5, '1', **kwargs)
        wikipedia_kwargs = {
            'ruleset': {
                'S': 'AS/T',
                'T': 'BS/E',
                'A': 'a',
                'B': 'b',
                'E': '',  # Epsilon string
            }
        }
        tdpl.test_grammar(10, 'S', **wikipedia_kwargs)

        # NOTE: For simplicity, slashes are not implemented as fallbacks,
        # as seen in the example.
        for left, right in wikipedia_kwargs['ruleset'].iteritems():
            print_h4('Testing wikipedia example '
                     'with starting rule: {}'.format(left))
            tdpl.test_grammar(10, left, **wikipedia_kwargs)

        wikipedia_kwargs2 = {
            'ruleset': {
                'S': 'OT/E',
                'T': 'SU/F',
                'U': 'CS/F',
                'O': '{',
                'C': '}',
                'E': 'ε',
                'F': 'f',
            }
        }
        for left, right in wikipedia_kwargs2['ruleset'].iteritems():
            print_h4('Testing wikipedia example 2 '
                     'with starting rule: {}'.format(left))
            tdpl.test_grammar(10, left, **wikipedia_kwargs2)
