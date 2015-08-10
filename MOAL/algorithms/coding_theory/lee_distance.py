# -*- coding: utf-8 -*-

__author__ = """Chris Tabor (dxdstudio@gmail.com)"""

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from MOAL.helpers.display import Section


DEBUG = True if __name__ == '__main__' else False


def lee_distance(str1, str2, q=6):
    print('Checking: {} / {}'.format(str1, str2))
    if len(str(str1)) != len(str(str2)):
        raise ValueError
    str1, str2 = str(str1), str(str2)
    n = len(str1)
    nums = []
    for i in range(n):
        diff1 = abs(int(str1[i]) - int(str2[i]))
        diff2 = abs(int(str1[i]) - int(str2[i]))
        res = min(diff1, q - diff2)
        print('Digit: {} = {}'.format(i, res))
        nums.append(res)
    return sum(nums)


if __name__ == '__main__':
    with Section('Algorithms / coding theory - Lee distance'):
        print('Distance: {}'.format(lee_distance(3140, 2543)))
