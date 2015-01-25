import time
from random import randrange as rr
from random import choice
from string import ascii_letters


def _gibberish(length=10):
    return ''.join([choice(
        ascii_letters).replace(' ', '') for _ in range(length)])


def run_trials(func, trials=3):
    for num in range(trials):
        print 'Running trial #{}'.format(num)
        func(num)
        print '------------------------'
        print


def swap_item(items, a, b):
    copy = items[a]
    items[a] = items[b]
    items[b] = copy
    return items


def get_random_number_sets(sets=2, max_random=50):
    return [[rr(1, 9999) for _ in range(max_random)] for _ in range(sets)]


def run_sorting_trials(
        sorting_func, magnitudes=[10, 100, 1000], test_output=True):
    """Runs a bunch of trials of various magnitudes with a given
    func, using randomly generated numbers.
    Returns a dict of results for later inspection."""
    results = {
        'function': sorting_func.func_name if hasattr(
            sorting_func, 'func_name') else 'builtin'
    }
    for magnitude in magnitudes:
        start = time.time()
        items = [rr(0, 999) for _ in range(magnitude)]
        sorted_res = sorting_func(items)
        end = time.time()
        results[magnitude] = {'time': end - start}
        if test_output:
            results[magnitude]['correct'] = sorted(items) == sorted_res
    return results


def _test_speed(func, *args, **kwargs):
    def _inner(*args, **kwargs):
        divider = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print divider
        print 'starting... {}'.format(func)
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print 'function took {}s'.format(end - start)
        print divider
        return res
    return _inner


def section(title):
    print
    print '================== {} ==================='.format(title)
    print
