if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import section
from generic_helpers import run_sorting_trials
from random import randrange as rr
from random import random
from pprint import pprint as ppr

# Base merge/merge_sort implementation based off of
# http://rosettacode.org/wiki/Sorting_algorithms/Merge_sort#Python


def merge(left, right):
    results = []
    left_index, right_index = 0, 0
    # Keep checking that the current respective index for each side
    # is smaller then the number of elements in it,
    # incrementing as it moves along.
    while left_index < len(left) and right_index < len(right):
        # Determine which element is greater on each side.
        if left[left_index] <= right[right_index]:
            results.append(left[left_index])
            left_index += 1
        else:
            results.append(right[right_index])
            right_index += 1
    # Add any remaining elements to the list from each respective side.
    # Each remaining side wil be elements > results.
    results = results + left[left_index:] + right[right_index:]
    return results


def merge_sort(items, iteration=0, side=None):
    # `iteration` and `side` are used for testing purposes,
    # visualizing the recursive nature of the divide and conquer algorithm.
    _len = len(items)
    if _len < 2:
        return items
    pivot = _len // 2
    # Keep subdividing based on pivot,
    # until an empty list is all that is left.
    left = items[:pivot]
    right = items[pivot:]
    # Print each side, keeping track of recursive count to visually
    # indicate how many recursive calls were made.
    # print (side if side else '[ROOT]'), (iteration * 2) * '.', left, right
    return merge(
        merge_sort(left, iteration=iteration + 1, side='left'),
        merge_sort(right, iteration=iteration + 1, side='right'))


section('BEGIN - Merge Sort')

results = run_sorting_trials(merge_sort)
ppr(results)
section('BEGIN - Merge Sort - integers')
ppr(merge_sort([rr(1, 9999) for _ in range(20)]))
section('BEGIN - Merge Sort - floating point integers')
ppr(merge_sort([random() * float(rr(1, 9999)) for _ in range(20)]))

section('END - Merge Sort')
