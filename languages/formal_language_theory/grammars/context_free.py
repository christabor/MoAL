# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from random import choice
from string import ascii_uppercase
from string import punctuation


class ContextFreeGrammar(object):

    def __init__(self):
        self.rules = []
        self.terminus = '$'
        self.mapping_token = ' => '
        self.DEBUG = False

    def __delitem__(self, rule):
        for index, rule in enumerate(self.rules):
            if rule[0] == rule:
                del self.rules[index]

    def add_rule(self, string):
        if self.mapping_token not in string:
            raise TypeError('Invalid rule representation. '
                            'Use a {} to indicate mapping.'.format(
                                self.mapping_token))
        left, right = string.split(self.mapping_token)
        self.rules.append([left, right])
        if self.DEBUG:
            print('Added rule: "{}"'.format(self.rules[::-1]))

    def _get_rule(self, token):
        for rule in self.rules:
            left, right = rule
            if left == token:
                return right
        return ''

    def evaluate_single(self, token, nonterminals, evaluation=''):
        rule = self._get_rule(token)
        spaces = ' ' * 4
        for char in rule:
            if char.endswith(self.terminus):
                print('{}Completed'.format(' ' * 4))
                return evaluation
            sub_rule = self._get_rule(char)
            print('{}Char: {}, Subrule: {}, (Parent rule: {})'.format(
                spaces, char, sub_rule if sub_rule else '[empty]', rule))
            if sub_rule:
                for sub_char in sub_rule:
                    if sub_char in nonterminals:
                        print('{}Nonterminal: {}'.format(spaces * 2, sub_char))
                        evaluation += self.evaluate_single(
                            sub_char, nonterminals, evaluation=evaluation)
                    else:
                        print('{}Terminal: {}'.format(spaces * 2, sub_char))
                        if sub_char != self.terminus:
                            evaluation += sub_char
                        else:
                            return evaluation
            else:
                evaluation += char
            curr = '[{}]'.format(
                evaluation if evaluation else '[empty]')
            print('{}{}\n'.format('.' * abs(80 - len(curr)), curr))
        return evaluation

    def evaluate(self, tokens, evaluation=''):
        """A basic parser for a custom attribute grammar.

        One thing to note is that ambiguous grammars need to be iterated over,
        since the duplicate rules can't be mapped via dictionary key.
        Unambiguous grammars are therefore more performant,
        because the lookup is O(1) vs. O(N).
        """
        nonterminals = [r[0] for r in self.rules]
        print('Ruleset: {}, Tokens: {}'.format(self.rules, tokens))
        for token in tokens:
            print('\n<{}>\n\nToken: {}'.format('=' * 80, token))
            evaluation += self.evaluate_single(token, nonterminals)
        print('\nFinal value: "{}"\n'.format(evaluation))
        return evaluation


def cp():
    return choice(punctuation)


def cu():
    return choice(ascii_uppercase)


if __name__ == '__main__':
    with Section('Grammar parser - basic'):
        cfg = ContextFreeGrammar()

        # There are two rules for the same mapping "S"; thus, it's ambiguous.
        ambig_grammar = [
            'S => <{++>U<>',
            'U => {}VV',
            'B => \\{//U\\++}',
            'V => *&&&*!$'
        ]
        ambiguous_cfg = ContextFreeGrammar()
        map(ambiguous_cfg.add_rule, ambig_grammar)
        tokens = [choice(['S', 'U', 'B', 'V']) for _ in range(10)]

        wiki_grammar = [
            'S => UV',
            'U => aBc-bBac',
            'B => caa$',
            'V => ac B bca U']

        letters = ['S', 'U', 'B', 'V']
        map(cfg.add_rule, wiki_grammar)

        def cfg1():
            prnt('CFG result', '')
            cfg.evaluate(['B', 'B', 'B', 'V', 'U'])
            cfg.evaluate(['U', 'C', 'B', 'V', 'U', 'S'])
            cfg.evaluate([choice(letters) for _ in range(10)])

        def cfg2():
            prnt('Ambiguous CFG result', ambiguous_cfg.evaluate(tokens))

        choices = {
            '1': cfg1,
            '2': cfg2
        }
        DEBUG = False
        if DEBUG:
            _choices = choices.keys()
            _choice = raw_input('Pick a CFG to run: {} ==> '.format(_choices))
            try:
                choices[_choice]()
            except KeyError:
                pass
        else:
            for func in choices:
                choices[func]()
