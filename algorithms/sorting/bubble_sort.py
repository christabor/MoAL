# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import Section
from generic_helpers import run_sorting_trials
from pprint import pprint as ppr


def bubble_sort(items):
    num_items = len(items)
    if num_items < 2:
        return items
    while num_items > 0:
        for k in range(num_items):
            try:
                if items[k] > items[k + 1]:
                    copy = items[k]
                    copy_next = items[k + 1]
                    items[k] = copy_next
                    items[k + 1] = copy
                elif items[k] == items[k + 1]:
                    continue
            except IndexError:
                continue
        num_items -= 1
    return items


if __name__ == '__main__':
    with Section('Bubble Sort'):
        ppr(run_sorting_trials(bubble_sort, test_output=True))
