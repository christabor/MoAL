# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from helpers.text import uniqchars
from languages.formal_language_theory.grammars import context_free
from random import randrange as rr


class AttributeContextFreeGrammar(context_free.ContextFreeGrammar):
    """An ACFG is effectively a CFG that allows attribute properties
    to be embedded in the ruleset for later evaluation -- this is pedestrian
    to any programming language that supports data structures, but it all
    comes from these simple foundations.

    For a formal definition and examples, see
    wikipedia.org/wiki/Attribute_grammar"""

    def __init__(self):
        super(AttributeContextFreeGrammar, self).__init__()
        self.attr_token = '.'
        self.terminus = '$'  # Terminal identifier
        self.DEBUG = True

    def __getitem__(self, attr):
        if attr == 'prop':
            return self._prop
        elif attr == 'value':
            return self._value
        elif attr == 'len':
            return self._len
        elif attr == 'chars':
            return self._chars
        else:
            return ''

    def _len(self, token):
        return 'L:{}'.format(len(token))

    def _prop(self, token):
        return 'U:{}'.format(token.upper())

    def _value(self, token):
        return '(R:{})'.format(rr(len(token), 999))

    def _chars(self, token):
        return 'U:{}'.format(uniqchars(len(token)))

    def _parse_terminal(self, attr, token):
        """Parse a terminal value given a attribute and token.

        For this example, we won't get too fancy,
        just force a string on all values.
        """
        return str(self[attr](token))

    def _attr(self, semantic_rule):
        """Get the attribute name from the semantic rule.
        It comes in as a list of [object, attribute]"""
        return semantic_rule.replace(
            self.terminus, '').replace(' ', '').split(self.attr_token)[1]

    def evaluate(self, tokens, evaluation=''):
        """A basic parser for a custom attribute grammar.

        One thing to note is that ambiguous grammars need to be iterated over,
        since the duplicate rules can't be mapped via dictionary key.
        Unambiguous grammars are therefore more performant,
        because the lookup is O(1) vs. O(N).
        """
        if self.DEBUG:
            prnt('Ruleset', self.rules)
            print('\nEvaluating tokens: {}'.format(tokens))
        for token in tokens:
            for rule in self.rules:
                # Expressions are already parsed when adding: (L => R = [L, R])
                left, right = rule
                print('Current rule = {} => {}'.format(left, right))
                if token == left:
                    is_attr = self.attr_token in right
                    is_terminal = right.endswith(self.terminus)
                    if is_attr and is_terminal:
                        print('\nEvaluating terminal: `{}`'.format(token))
                        evaluation += self._parse_terminal(
                            self._attr(right), token)
                    else:
                        non_terms = list(right)
                        print('\nEvaluating non-terminal {}'.format(non_terms))
                        evaluation += self.evaluate(
                            non_terms, evaluation=evaluation)
        return evaluation


if __name__ == '__main__':
    with Section('Grammar parser - basic'):

        attribute_cfg = AttributeContextFreeGrammar()
        rule_templates = [
            'COMB => ST',
            'S => S.value $',
            'T => T.prop $',
            'X => X.len $',
            'Z => Z.chars $',
        ]
        map(attribute_cfg.add_rule, rule_templates)

        prnt(
            'Attribute CFG evaluation result',
            attribute_cfg.evaluate(['COMB', 'COMB', 'Z', 'X', 'S', 'T']))
