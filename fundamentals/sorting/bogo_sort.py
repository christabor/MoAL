if __name__ == '__main__':
    from os import sys, path
    sys.path.append(
        path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))


from generic_helpers import section
from generic_helpers import _test_speed
from generic_helpers import run_sorting_trials
from generic_helpers import get_random_number_sets
from pprint import pprint as ppr


@_test_speed
def bogo_sort(items):
    return items


section('BEGIN - Bogo Sort (LOL)')

run_sorting_trials(bogo_sort, magnitudes=[5, 20, 40])

section('END - Bogo Sort (LOL)')
