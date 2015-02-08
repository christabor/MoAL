import time
from random import randrange as rr
from random import choice
from string import ascii_letters
from blessings import Terminal

term = Terminal()


def _gibberish(length=10):
    return ''.join([choice(
        ascii_letters).replace(' ', '') for _ in range(length)])


def run_trials(func, trials=3):
    for num in range(trials):
        print 'Running trial #{}'.format(num)
        func(num)
        print '------------------------'
        print


def divide_groups(items, divisions=2):
    groups = []
    num_items = len(items)
    last_offset = 0
    sections = num_items // divisions
    for i in range(num_items):
        sub_group = items[last_offset:last_offset + sections]
        if sub_group:
            groups.append(sub_group)
        # Update the last offset for the next index.
        last_offset += sections
    return groups


def swap_item(items, a, b):
    copy = items[a]
    items[a] = items[b]
    items[b] = copy
    return items


def random_number_set(min_rand=0, max_rand=9999, max_range=100):
    return [rr(min_rand, max_rand) for _ in range(max_range)]


def get_random_number_sets(sets=2, max_random=50):
    return [random_number_set(0, 9999, max_random) for _ in range(sets)]


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


# Display utilities


def _print(words, result, func=None):
    print
    print '{t.green}{t.underline}{}{t.normal}'.format(words, t=term)
    if func is not None:
        func(result)
    else:
        print result
    print


def _cmd_title(msg):
    print
    print '{t.red}{t.reverse}[{msg}]{t.normal}'.format(msg=msg.upper(), t=term)
    print


class Section:

    def __init__(self, content):
        self.separator = '=' * 10
        self.content = content

    def _print(self, prefix):
        print
        print '{t.cyan}\n= [{}]: {t.bold} {} {sep} \n{t.normal}'.format(
            prefix, self.content, t=term, sep=self.separator)

    def __enter__(self):
        self._print('BEGIN')

    def __exit__(self, exception_type, excetpion_value, traceback):
        self._print('END')
