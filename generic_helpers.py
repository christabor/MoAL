import time
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


def _test_speed(func, *args, **kwargs):
    def _inner(*args, **kwargs):
        divider = '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
        print divider
        print 'starting... {}'.format(func)
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print 'function took {}s'.format(end - start)
        print divider
    return _inner


def section(title):
    print
    print '================== {} ==================='.format(title)
    print
