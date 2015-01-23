if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import section
from generic_helpers import run_sorting_trials
from pprint import pprint as ppr


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


section('BEGIN - Insertion Sort')

results = run_sorting_trials(insertion_sort)
print 'Insertion sort results:'
ppr(results)

section('END - Insertion Sort')
