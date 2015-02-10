# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from helpers.display import Section
from helpers.trials import run_sorting_trials
from insertion_sort import insertion_sort
from quick_sort import quick_sort
from pprint import pprint as ppr


# Based off of description from http://en.wikipedia.org/wiki/Shellsort

def shell_sort(items, maxgaps=5):
    """Shell sort is described as a generalization of insertion
    and quick sort, so we use the gap strategy to divide the list
    into sub groups that are then sorted using traditional sorts."""
    num_items = len(items)
    sub_groups = []
    last_offset = 0
    # Make sure maxgaps is never greater than the number of items.
    while maxgaps > num_items:
        maxgaps -= 1
    # Prevent passing in div by zero errors.
    if maxgaps == 0:
        maxgaps = 1
    # Get the gap division number based on length and maxgaps.
    gap_sections = num_items // maxgaps
    if num_items < 2:
        return items
    for k in range(maxgaps):
        # Add the sub groups by the last_offset and the current gap
        # e.g. [0, 10], [10, 20], [20, 30]...
        sub_groups += insertion_sort(
            items[last_offset:last_offset + gap_sections])
        # Update the last offset for the next index.
        last_offset += gap_sections
    # Return the results with the typical quick sort.
    return quick_sort(sub_groups)


if __name__ == '__main__':
    with Section('Shell Sort'):
        TEST_MAGNITUDES = [4, 10, 50, 100, 500, 1000, 10000]
        # Compare helper sorting functions
        # in isolation to the hybrid shell function
        ppr(run_sorting_trials(shell_sort, magnitudes=TEST_MAGNITUDES))
        ppr(run_sorting_trials(quick_sort, magnitudes=TEST_MAGNITUDES))
        ppr(run_sorting_trials(insertion_sort, magnitudes=TEST_MAGNITUDES))
