# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section


DEBUG = True if __name__ == '__main__' else False


def hamming(str1, str2):
    """Algorithm based on an old project of mine, ported from yavascript:
    christabor.github.io/etude/09-02-2014/.

    A superior algorithm exists at
    wikipedia.org/wiki/Hamming_distance#Algorithm_example,
    but copying it would defeat the purpose."""
    dist = 0
    last_longer = len(str1) < len(str2)
    first, last = (str1, str2,) if last_longer else (str2, str1,)
    for k, letter in enumerate(str1):
        try:
            if str1[k] != str2[k]:
                dist += 1
        except IndexError:
            continue
    # Add remainder between offset of each (e.g. "cat", "cats" = range(2, 3))
    for k in range(len(first), len(last)):
        dist += 1
    print('Hamming dist for `{}` and `{}` = {}'.format(str1, str2, dist))
    return dist


if __name__ == '__main__':
    with Section('Algorithms / coding theory - Hamming distance'):
        hamming('Sanguine swine', 'Dandelion wine')
        hamming('Foo', 'Foobar')
        hamming('0123', '12345')
        hamming('Grape drank', 'Ape rank')
        hamming('011011101', '110110101')
