# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import prnt
from MOAL.helpers.display import Section
from random import randrange as rr
from random import choice


def rand_fname():
    return choice(
        ['Joe', 'Jane', 'Jimbo', 'Augustus', 'Slim', 'Max'])


def rand_lname():
    return choice(
        ['Johnson', 'Goodal', 'McCrude', 'Ceaser', 'Shady', 'Headroom'])


def rand_year():
    return rr(100, 9999)


def rand_day():
    return rr(1, 31)


def naive_bnf_parser(grammar):
    """
        Traditional Grammar example:

        <date> ::= <month> <day> <year>
        <month> ::= "January" | "February | "March" | "April" | "May" | "June"
                    | "July" | "August" | "September" | "November" | "December"
        <day> ::= 1.. | ..31
        <year> ::= 100.. | ..9999

        Here we need something that is a bit more serializable -- so we'll
        make it JSON friendly. Each parseable tokens is either a <rule> or
        syntax; rules represent containers, and can even have other rules!

        'name': {'date', 'is_rule': True, 'vals': ['month', 'day', 'year']},
        'name': {'month', 'is_rule': False, 'vals': '...'},
        'name': {'day', 'is_rule': False, 'vals': '...'},
        'name': {'year', 'is_rule': False, 'vals': '...'},

        <name> ::= <firstname> <lastname>
        <firstname> ::= 'string'
        <lastname> ::= 'string'

        'name': {'name', 'is_rule': True, 'vals': []},
        'name': {'firstname', 'is_rule': False, 'vals': '...'},
        'name': {'lastname', 'is_rule': False, 'vals': '...'},
    """
    evaluation = []

    def _add(token):
        # If it's a function, call it
        if hasattr(token['vals'], '__call__'):
            retval = token['vals']()
            evaluation.append(retval)
        # If it's a list, get a random value for this demo.
        elif isinstance(token['vals'], list):
            retval = choice(token['vals'])
            evaluation.append(retval)
        else:
            # Otherwise it's a sentinel value, so just add it.
            evaluation.append(token['vals'])

    def _process(key, token):
        proper_rule = token['is_rule'] and isinstance(token['vals'], list)
        if not proper_rule:
            _add(token)

    # Normalize list vs dict types since the function is called recursively.
    if isinstance(grammar, dict):
        for key, token in grammar.iteritems():
            _process(key, token)
    elif isinstance(grammar, list):
            for key, token in enumerate(grammar):
                _process(key, token)
    else:
        # If it's not iterable, return it as-is.
        return grammar
    return evaluation


if __name__ == '__main__':
    with Section('Backus Naur Form'):
        # Shallow rules
        date = {
            'date': {'is_rule': True, 'vals': ['month', 'day', 'year', ]},
            'month': {'is_rule': False, 'vals': ['jan', 'feb', 'march', ]},
            'day': {'is_rule': False, 'vals': rand_day},
            'year': {'is_rule': False, 'vals': rand_year}
        }
        name = {
            'name': {'is_rule': True, 'vals': ['firstname', 'lastname', ]},
            'firstname': {'is_rule': False, 'vals': rand_fname},
            'lastname': {'is_rule': False, 'vals': rand_lname},
        }
        # Deep rules
        foo = {
            'bar': {'is_rule': True, 'vals': ['bim', 'bam']},
            'bim': {'is_rule': True, 'vals': ['quux']},
            'bam': {'is_rule': False, 'vals': ['bam']},
            'quux': {'is_rule': False, 'vals': ['quux']},
        }

        for _ in range(4):
            prnt('BNF parsing result <name>', naive_bnf_parser(name))
            prnt('BNF parsing result <date>', naive_bnf_parser(date))
            prnt('BNF parsing result <foo>', naive_bnf_parser(foo))
