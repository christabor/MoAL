# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import Section
from generic_helpers import run_sorting_trials
from random import randrange as rr
from pprint import pprint as ppr


def bogo_sort(items):
    num_items = len(items)
    # Cheating :)
    correct = sorted(items)
    while correct != items:
        rand_swap_a = rr(0, num_items)
        rand_swap_b = rr(0, num_items)
        if items[rand_swap_a] > items[rand_swap_b]:
            copy_a = items[rand_swap_a]
            copy_b = items[rand_swap_b]
            items[rand_swap_a] = copy_b
            items[rand_swap_b] = copy_a
    print items
    return items


with Section('Bogo Sort (LOL)'):
    ppr(run_sorting_trials(bogo_sort, magnitudes=[3, 5, 10]))
