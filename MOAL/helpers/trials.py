import time
from random import randrange as rr
from functools import wraps


def run_trials(func, trials=3):
    """Runs a set of trials given a function and trial number.
    The `func` in question is expected to use the test_speed decorator
    to do the actual profiling."""
    for num in range(trials):
        print('Running trial #{}'.format(num))
        func(num)
        print('------------------------\n')


def run_sorting_trials(
        sorting_func, magnitudes=[10, 100, 1000], test_output=True):
    """Runs a bunch of trials of various magnitudes with a given
    func, using randomly generated numbers.
    Returns a dict of results for later inspection.
    Tailored specifically for sorting functions, by
    generating randomly mixed sequences of numbers."""
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


def test_speed(func, *args, **kwargs):
    """Decorator that wraps a function and provides a timer
    + results output for execution profiling."""
    @wraps(func)
    def _inner(*args, **kwargs):
        divider = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print(divider)
        print('starting... {}'.format(func))
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print('function took {}s'.format(end - start))
        print(divider)
        return res
    return _inner
