# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from random import choice
from languages.formal_language_theory.grammars.context_free \
    import ContextFreeGrammar

DEBUG = True if __name__ == '__main__' else False


class ContextSensitiveGrammar(ContextFreeGrammar):

    DEBUG = True

    def __init__(self):
        self.rule_divider = ':'
        super(ContextSensitiveGrammar, self).__init__()
        self.DEBUG = ContextSensitiveGrammar.DEBUG

    @staticmethod
    def get_substr_match(rule, string):
        """Return the index of the last matching item of the two strings.
        e.g. index = 1 for '[ab]cd' and '[ab]zd'. If the index is the
        same as the length then the strings simply match.
        """
        if not len(rule) <= string:
            raise Exception('Invalid string.')
        # Degenerate case
        if rule == string:
            return len(rule)
        rule = list(rule)
        string = list(string)
        index = 0
        for k, letter in enumerate(rule):
            if rule[k] != string[k]:
                return index
            else:
                index += 1
        return index

    @staticmethod
    def simple_rule(rule, string=''):
        _rule = list(rule)
        _string = list(string)
        if ContextSensitiveGrammar.DEBUG:
            print('simple rule: {} and string: {}'.format(_rule, _string))
        # We only replace tokens that match a rule.
        # The rest remain unchanged.
        for k, char in enumerate(string):
            if char in _rule:
                _string[k] = ''.join(string).replace(' ', '')
                # Replace the token with the rules' string
                _string[k] = ContextSensitiveGrammar.simple_rule(
                    rule, string=_string)

        ret = ''.join(_string)
        if ContextSensitiveGrammar.DEBUG:
            prnt('simple rule retval: ', ret)
        return ret

    def _evaluate(self, groups, evaluation=''):
        for group in groups:
            left, right = group
            evaluation += ''.join(right)
        return evaluation

    def evaluate(self, tokens=None, evaluation=''):
        """A basic parser for a custom attribute grammar.

        One thing to note is that ambiguous grammars need to be iterated over,
        since the duplicate rules can't be mapped via dictionary key.
        Unambiguous grammars are therefore more performant,
        because the lookup is O(1) vs. O(N).
        """
        if tokens is None:
            if hasattr(self, 'tokens'):
                tokens = self.tokens
            else:
                raise ContextFreeGrammar.InvalidTokenSet
        expressions = [r[0] for r in self.rules]
        tokens = [r[1] for r in self.rules]
        groups = [[
            expressions[k],
            tokens[k].split(' ')] for k, _ in enumerate(tokens)
        ]
        prnt('Groups', groups)
        evaluation = self._evaluate(groups, evaluation='')
        new_tokens = list(evaluation)
        for token in new_tokens:
            for expression in expressions:
                if token in list(expression):
                    token = self._evaluate(groups, evaluation=evaluation)
        if ContextSensitiveGrammar.DEBUG:
            print('Final evaluation in `evaluate`: {}'.format(
                evaluation, ''.join(new_tokens)))
        return evaluation


if DEBUG:
    with Section('Grammar parser - basic'):
        """https://en.wikipedia.org/wiki/Context-sensitive_grammar#Examples"""
        _csg = ContextSensitiveGrammar
        csg_rules = [
            'S => a b c',
            'S => a S B c',
            'c B => W B',
            'W B => W X',
            'W X => B X',
            'B X => B c',
            'b B => b b',
        ]
        csg = ContextSensitiveGrammar()
        csg.set_rules(csg_rules)
        tokens = [choice(
            ['S', 'S', 'c B', 'W B', 'W X', 'B X', 'b B']) for _ in range(4)]
        prnt('Tokens:', tokens)
        csg.evaluate(tokens=tokens)
        csg.evaluate(tokens=['S'])

        # Testing/staticmethods
        _csg.simple_rule('S', 'aSaSbb$')
        _csg.simple_rule('X', 'aBcXaa')

        csg.evaluate(tokens=['S', 'B', 'B X'])

        assert len('a b c') == _csg.get_substr_match('a b c', 'a b c')
        assert len('a C d') == _csg.get_substr_match('a C d', 'a C d EE')
        assert len('a C') == _csg.get_substr_match('a C', 'a C d EE')
        assert len('a C d E') == _csg.get_substr_match('a C d E', 'a C d EE')
        assert not len('a C d') == _csg.get_substr_match('a C d E', 'a C d EE')
        assert not len('a C d') == _csg.get_substr_match('a c d', 'a C d')
