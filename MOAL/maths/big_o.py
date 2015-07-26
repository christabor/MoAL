# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.text import gibberish
from MOAL.helpers.trials import test_speed
from MOAL.helpers.trials import run_trials
from MOAL.helpers.display import Section


dict_test = {gibberish(length=10): x for x in range(1000)}
dict_test['foo'] = 'bar'


@test_speed
def o_1():
    print('I am a O(1) function')
    print(dict_test['foo'])


@test_speed
def o_n():
    print('I am a O(n) function')
    for x in range(10, 1000):
        print(x * x)


@test_speed
def o_n2():
    print('I am a O(n^2) function')
    for x in range(10, 100):
        for y in range(10, 100):
            print('{} + {} = {}'.format(x, y, x + y))


@test_speed
def o_n_comprehension():
    print('I am a O(n) comprehension function')
    print([x * x for x in range(10, 1000)])


@test_speed
def o_n3(max_amt=30):
    _ = 0
    print('I am a O(n^3) function')
    for x in range(max_amt):
        for y in range(max_amt):
            for z in range(max_amt):
                _ = x + y + z
                # print('{} + {} + {} = {}'.format(x, y, z, x + y + z))
    print('Result: {}'.format(_))


@test_speed
def o_2n(num):
    print('I am a O(2^n) function')

    def fibo(num):
        if num <= 1:
            return num
        else:
            return fibo(num - 1) + fibo(num - 2)
    print(fibo(num))


@test_speed
def o_log_n(max_amt=1000):
    foo = max_amt
    print('I am a O(log n) function')
    while foo > 0:
        foo = foo / 2


@test_speed
def o_n_factorial(factor=10):
    # Basically a for loop nested `factor` times.
    pass


if __name__ == '__main__':
    with Section('BIG O Notation'):
        o_1()
        o_n()
        o_n2()
        o_n_comprehension()
        run_trials(o_n3, trials=20)
        run_trials(o_log_n, trials=10)
        o_n_factorial()
        o_2n(10)
