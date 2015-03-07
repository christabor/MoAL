# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_simple
from helpers.display import prnt
from random import choice
from string import ascii_uppercase
from string import punctuation


class ContextFreeGrammar(object):

    def __init__(self):
        self.rules = []
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

    def evaluate(self, tokens):
        evaluation = ''
        for _, expression in enumerate(self.rules):
            for token in tokens:
                if token == expression[0]:
                    evaluation += expression[1]
            if self.DEBUG:
                print('rule {} {} {}'.format(
                    expression[0], self.mapping_token, expression[1]))
        return evaluation


class WikipediaCFG(ContextFreeGrammar):
    """
    From wikipedia.org/wiki/Context-free_grammar
    S => U | V
    U => TaU | TaT | UaT
    V => TbV | TbT | VbT
    T => aTbT | bTaT | [END]
    """

    def __init__(self):
        super(WikipediaCFG, self).__init__()
        self.rules = {}

    def add_rule(self, rule):
        left, right = rule.split(self.mapping_token)
        self.rules[left] = right

    def evaluate(self, tokens):
        evaluation = ''
        for rule, expression in self.rules.iteritems():
            for char in list(expression):
                try:
                    evaluation += self.rules[char]
                except KeyError:
                    if char == ';':
                        return evaluation
                    else:
                        evaluation += char
        return evaluation


if __name__ == '__main__':
    with Section('Grammar parser - basic'):
        cfg = ContextFreeGrammar()

        def cp():
            return choice(punctuation)

        def cu():
            return choice(ascii_uppercase)

        for _ in range(10):
            # Gibberish cfg rule templates
            rule_templates = [
                '{} => {}'.format(cu(), cu()),
                '{} => (({}{}))'.format(cu(), cu(), cu()),
                '{} => {}+{}'.format(cu(), cu(), cu()),
                '{} => {}_{}_{}'.format(cu(), cp(), cu(), cp()),
                '{} => {}{}'.format(cu(), cu(), cu()),
            ]
            cfg.add_rule(choice(rule_templates))

        prnt(
            'CFG evaluation result',
            cfg.evaluate([cu() for n in range(20)]))

        ambiguous_cfg = ContextFreeGrammar()
        # There are two rules for the same mapping "S"; thus, it's ambiguous.
        ambiguous_cfg.add_rule('{} => {}{}'.format('S', cu(), cp()))
        ambiguous_cfg.add_rule('{} => {}{}{}'.format('S', cu(), cp(), cp()))

        prnt(
            'Ambiguous CFG evaluation result',
            ambiguous_cfg.evaluate(['S' for _ in range(20)]))

        for rule in cfg.rules:
            del rule

        for letter in ascii_uppercase:
            cfg.add_rule('{} => <<{}>>({})'.format(letter, cu(), cp()))

        prnt('Ambiguous CFG evaluation result - nursery rhymes', '')
        print_simple(cfg.evaluate(list('THE COW JUMPED OVER THE MOON')), '')
        print_simple(cfg.evaluate(list('LITTLE BO PEEP LOST HER SHEEP')), '')
        print_simple(cfg.evaluate(
            list('THE WHEELS ON THE BUS GO ROUND AND ROUND')), '')

        wiki_cfg = WikipediaCFG()
        wiki_cfg.add_rule('S => U | V')
        wiki_cfg.add_rule('U => TaU')
        wiki_cfg.add_rule('U => TaT')
        wiki_cfg.add_rule('U => UaT')

        wiki_cfg.add_rule('V => TbV')
        wiki_cfg.add_rule('V => TbT')
        wiki_cfg.add_rule('V => VbT')

        wiki_cfg.add_rule('T => aTbT')
        wiki_cfg.add_rule('T => bTaT')
        wiki_cfg.add_rule('T => ;')
        prnt(
            'CFG evaluation result',
            wiki_cfg.evaluate(['S', 'V', 'U', 'T']))
