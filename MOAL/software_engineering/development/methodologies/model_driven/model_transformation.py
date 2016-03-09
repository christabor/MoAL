"""Model transformation."""

# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

DEBUG = True if __name__ == '__main__' else False

if DEBUG:
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section, divider
import re
from pprint import pprint as ppr


def evaluate_model(model, **ruleset):
    """Considered an 'endogenous' model transformation.

    The rules and models are evaluated in Python.
    """
    errors = []
    for rulename, rule in ruleset.items():
        if rulename in model:
            value = str(model[rulename])
            if not re.match(rule, value):
                errors.append({
                    'rule': rulename,
                    'value': value,
                    'error': 'Rule did not match expected format!',
                    'format': rule
                })
    if errors:
        return errors


def check_model(model, **ruleset):
    """Evaluate the model and prints results."""
    res = evaluate_model(model, **ruleset)
    if res:
        map(ppr, res)
    else:
        print('No results -- model is error free!')
    divider('.')


if DEBUG:
    with Section('Model transformation - utility'):
        goodmodel = dict(
            fname='Chris',
            lname='Tabor',
        )
        badmodel = dict(
            fname=3,
            lname=12222,
        )

        check_model(
            goodmodel,
            fname=r'[a-zA-Z]{1,50}',
            lname=r'[a-zA-Z]{1,50}')

        check_model(
            badmodel,
            fname=r'[a-zA-Z]{1,50}',
            lname=r'[a-zA-Z]{1,50}')
