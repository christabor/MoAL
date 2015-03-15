# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import print_h2
from helpers.adts import list_fill
import time

DEBUG = True if __name__ == '__main__' else False


def _check_degenerates(s1, s2):
    """
    "In mathematics, a degenerate case is a limiting case in which an element
    of a class of objects is qualitatively different from the rest of the class
    and hence belongs to another, usually simpler, class."
    -Wikipedia

    The degenerates here are strings that are equal; these are not in the class
    of strings that need comparison by Levenshtein distance.
    """
    if s1 == s2:
        return 0
    if len(s1) == 0:
        return len(s2)
    if len(s2) == 0:
        return len(s1)
    return None


def _branch(word, dist):
    # TODO: move into re-usable recursion visualization function
    # (from original drawings of an abstract diagram for recursion.)
    chars = len(word)
    word = '{}'.format('\\' + ('_' * chars * 2) + word if dist == 1 else word)
    hline = chars * '_'
    branch = '{}'.format('' * chars if dist == 1 else '{}/'.format(hline))
    return branch, word


def lev_recursive(s1, s2, l1=None, l2=None, ct=0, parent=True):
    """Recursive implementation of the Levenshtein distance algorithm.
    Algorithm from Wikipedia pseudocode:
    wikipedia.org/wiki/Levenshtein_distance#Computing_Levenshtein_distance
    Canonical math example, but not useful for real implementations.
    """
    basic = _check_degenerates(s1, s2)
    if basic is not None:
        return basic
    dist = 0
    # Get length of both strings
    if l1 is None and l2 is None:
        l1, l2 = len(s1), len(s2)
    # Return the other string if one is zero, and vice versa.
    if l1 == 0:
        return l2
    if l2 == 0:
        return l1
    # Compare last characters of both cost increases if they're not equal.
    cost = 0 if s1[::-1] == s2[::-1] else 1
    # Perform the distance function by returning three calls recursively
    # per operation, to determine the offset of the three scenarios:
    # short s1, short s2
    dist = min(
        lev_recursive(
            s1, s2, l1=l1 - 1, l2=l2, ct=ct + 1, parent=False) + 1,
        lev_recursive(
            s1, s2, l1=l1, l2=l2 - 1, ct=ct + 2, parent=False) + 1,
        lev_recursive(
            s1, s2, l1=l1 - 1, l2=l2 - 1, ct=ct + 3,
            parent=False) + cost)
    if DEBUG:
        # A visualization of the recursive call graph and the various
        # parent/child branches that result in the duplicate
        # (and unnecessary) calculations.
        word = s1[0:l1] + s2[0:l2]
        text = '"{}" and "{}" = {}'.format(s1, s2, dist)
        # Get the branch/leaf style based on whether it was the root
        # or child node in each call graph.
        branch, word = _branch(word, dist)
        # With the combination of a time delay and the branching
        # visualization, I hope to drive home the realization of how
        # terribly inefficient this algorithm is.
        time.sleep(0.01)
        branching = '{}{}{}'.format('  ' * ct, word, branch)
        print('({}) {}'.format(text, branching))
    return dist


def lev_iterative(s1, s2):
    """The iterative approach to the Levenshtein algorithm.
    Code is ported from (pseudo-code? c?) example on Wikipedia:
    wikipedia.org/wiki/Levenshtein_distance#Iterative_with_two_matrix_rows

    One important thing to note: the Levenshtein function is NOT transitive,
    so order matters! That is, lev(s1, s2) != lev(s2, s1).
    """
    basic = _check_degenerates(s1, s2)
    if basic is not None:
        return basic
    v1, v2 = list_fill(len(s2) + 1, fill=0), list_fill(len(s2) + 1, fill=0)
    len1, len2, lenv1 = len(s1), len(s2), len(v1)

    for i in range(0, len2):
        v1[i] = i

    for i in range(0, len1):
        v2[0] = i + 1
        for j in range(0, len2):
            cost = 0 if s1[i] == s2[j] else 1
            v2[j + 1] = min(v1[j] + 1, v1[j + 1] + 1, v1[j] + cost)
        for _j in range(0, lenv1):
            v1[_j] = v2[_j]

    dist = v2[len2]
    print('Levenshtein distance of "{}" and "{}" is {}'.format(s1, s2, dist))
    return dist


if __name__ == '__main__':
    with Section('Algorithms / coding theory - Levenshtein distance'):
        print_h2('Levenshtein distance', 'recursive')
        lev_recursive('mop', 'pop')

        print_h2('Levenshtein distance', 'iterative')
        pairs = [
            ('slaughter', 'laughter'), ('flower', 'power'),
            ('liliputian', 'brobdingnagian'),
            ('sitting', 'kitten'),
            ('gargantua', 'pentagruel'),
        ]
        for pair in pairs:
            lev_iterative(*pair)
