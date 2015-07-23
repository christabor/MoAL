# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section
from MOAL.helpers.display import prnt
from MOAL.helpers.trials import run_trials
from random import randrange as rr
from random import choice
from pprint import pprint as ppr


class NotInGroupException(Exception):
    pass


class Probability:

    @staticmethod
    def _fmt(res, count):
        return res, count, '~{:01.1f}%'.format(res)

    @staticmethod
    def _percentages(count, divisor):
        count = float(count)
        divisor = float(divisor)
        return Probability._fmt(divisor / count * 100, count)

    @staticmethod
    def of_single(values, are_equal=True):
        if are_equal:
            return Probability._percentages(len(values), 1.0)
        else:
            raise NotImplementedError('Unequal weighting not implemented.')

    @staticmethod
    def of_group(values, subset, are_equal=True):
        if are_equal:
            for val in subset:
                if val not in values:
                    raise NotInGroupException
            return Probability._percentages(len(values), len(subset))
        else:
            raise NotImplementedError('Unequal weighting not implemented.')


def coin_flip(count=1000):
    choices = ['heads', 'tails']
    for _ in xrange(count):
        yield choice(choices)


def get_results(values, runs=100):
    results = {'values': values, 'picks': {}}
    for val in values:
        results['picks'][val] = 1

    for _ in range(runs):
        results['picks'][choice(values)] += 1
    return results


def test_coin_flip(*args):
    res = {'heads': [0, 0], 'tails': [0, 0]}
    for side in coin_flip():
        res[side][0] += 1
    res['heads'][1] = '~{}%'.format(res['heads'][0] // 10.0)
    res['tails'][1] = '~{}%'.format(res['tails'][0] // 10.0)
    print(res)
    return res


def _test(*args):
    values = [rr(1, 999) for d in range(10)]
    ppr(get_results(values))


if __name__ == '__main__':
    with Section('Probability'):
        values_rand = [rr(1, 999) for d in range(rr(1, 20))]
        prnt(
            ('Probability of a given value:', values_rand),
            Probability.of_single(values_rand))

        run_trials(_test)

        prnt(
            ('Probability of multiple given values:',
                values_rand, values_rand[:2]),
            Probability.of_group(values_rand, values_rand[:2], are_equal=True))

        prnt(
            ('Probability of multiple given values:',
                values_rand, values_rand[:4]),
            Probability.of_group(values_rand, values_rand[:4], are_equal=True))

        run_trials(test_coin_flip)
