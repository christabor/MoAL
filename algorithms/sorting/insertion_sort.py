# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())


from helpers.display import Section
from helpers.display import prnt
from helpers.trials import run_sorting_trials


def insertion_sort(items):
    if len(items) < 2:
        return items
    for k, item in enumerate(items):
        # Keep a copy of the item and the index
        # during each iteration
        copy = items[k]
        j = k
        while j > 0 and items[j - 1] > copy:
            # Swap current element with the previous one, which is lesser
            items[j] = items[j - 1]
            # Decrement and continue until j is 0,
            # which is the beginning of the list.
            j = j - 1
        # Once the while loop is complete, update the original copy
        # index with the new index for j (which was determined
        # when j - 1 was no longer greater than copy.)
        items[j] = copy
    return items


if __name__ == '__main__':
    with Section('Insertion Sort'):
        results = run_sorting_trials(insertion_sort)
        prnt('Insertion sort results:', results)
