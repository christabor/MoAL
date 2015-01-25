if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import section
from generic_helpers import _test_speed
from generic_helpers import run_sorting_trials
from pprint import pprint as ppr


# Based off algorithm from http://en.wikipedia.org/wiki/Quicksort

@_test_speed
def quick_sort(items, low=None, high=None):

    def _swap(items, a, b):
        copy = items[a]
        items[a] = items[b]
        items[b] = copy
        return items

    def partition(items, low, high):
        pivot_index = (low + high) / 2
        pivot_value = items[pivot_index]
        items = _swap(items, pivot_index, high)
        store_index = low
        for k in range(low, high):
            if items[k] < pivot_value:
                items = _swap(items, k, store_index)
                store_index += 1
        items = _swap(items, store_index, high)
        return store_index

    num_items = len(items)
    if len(items) < 2:
        return items
    if low is None:
        low = 0
    if high is None:
        high = num_items - 1
    if low < high:
        partitioned = partition(items, low, high)
        quick_sort(items, low=low, high=partitioned - 1)
        quick_sort(items, low=partitioned + 1, high=high)
    print items
    return items


section('BEGIN - Quick Sort')

ppr(run_sorting_trials(quick_sort, magnitudes=[10, 100, 1000]))

section('END - Quick Sort')
