# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from helpers.display import Section
from helpers.generic import swap_item
from helpers.trials import run_sorting_trials
from pprint import pprint as ppr

# Based off of algorithm from http://en.wikipedia.org/wiki/Selection_sort


def selection_sort(items):
    num_items = len(items)
    if num_items < 2:
        return items
    curr_min = 0
    for j in range(num_items):
        # Assign minimum to j, initially
        curr_min = j
        # Loop through all elements /after/ j,
        # checking to find the new smallest item.
        for i in range(j + 1, num_items):
            # Update current min if this one is smaller.
            if items[i] < items[curr_min]:
                curr_min = i
        # After the internal loop finishes,
        # check (on each outer iteration) if j is less than the new curr_min.
        # If so, then a smaller item was found and needs to be swapped.
        if curr_min != j:
            swap_item(items, j, curr_min)
    return items


if __name__ == '__main__':
    with Section('Selection Sort'):
        ppr(run_sorting_trials(
            selection_sort, magnitudes=[10, 100, 1000, 5000]))
