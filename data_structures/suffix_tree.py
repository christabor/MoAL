# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from helpers.display import _print
from helpers.display import Section
from helpers.generic import powerset_tree
from helpers.generic import substring_list
from helpers.trials import _test_speed
from pprint import pprint as ppr
from random import choice


class BaseSuffixTree(object):

    """
    [From Wikipedia:]

    "A suffix tree is a compressed Trie containing all the
    suffixes of the given text as their keys and positions
    in the text as their values."

    "...The suffix tree for the string S of length n is
    defined as a tree such that:

    1. The tree has exactly n leaves numbered from 1 to n.
    2. Except for the root, every internal node has at least two children.
    3. Each edge is labeled with a non-empty substring of S.
    4. No two edges starting out of a node can have string-labels beginning
        with the same character.
    5. The string obtained by concatenating all the string-labels
        found on the path from the root to leaf i spells out
        suffix S[i..n], for i from 1 to n.

    -- CONSTRUCTION --

    `banana` seems to be the canonical example, so we'll keep with tradition.

    First, let's get some information about the string.

    >>> l, s = len(banana), 'banana'

    Now we can use this data to construct our tree. Note: there are some
    implementations that seem to omit the sub-substrings, but we'll cover
    both as two different classes, which we'll call shallow, and deep.
    The required storage for the deep one is significantly greater.

    Either version could be easily represented using a list or dictionary.
    See the individual classes for details.

    --- FUN FACTS (Wikipedia): ---
        "...there have been practical works for constructing disk-based
        suffix trees which scale to **(few) GB/hours.**
        The state of the art methods are TDD, TRELLIS, DiGeST, B2ST...

        ...ERA can index the entire human genome in 19 minutes on an
        8-core desktop computer with 16GB RAM. On a simple Linux cluster
        with 16 nodes (4GB RAM per node), ERA can index the entire
        human genome in less than 9 minutes."
        "
    """

    def __init__(self, word):
        """Init function."""
        self.DEBUG = False
        self.MAX_LENGTH = len(word)
        # Create initial substrings
        self.word = word
        self.tree = None
        # Generate the tree on creation.
        self._populate()

    def __str__(self):
        ppr(self.tree)
        return ''

    def __getitem__(self, key):
        return self.tree[key]

    def __setitem__(self, key, val):
        self.tree[key] = val

    def _populate():
        raise NotImplementedError


class ShallowSuffixTree(BaseSuffixTree):
    """Shallow:
    substrings(s) = [
        'banana', # s[0:]
        'anana', # s[1:]
        'nana', # s[2:]
        'ana', # s[3:]
        'na', # s[4:]
        'a', # s[5:]
    ]
    """

    @_test_speed
    def _populate(self):
        self.tree = substring_list(self.word)


class DeepSuffixTree(BaseSuffixTree):

    """The deeper tree can be up to `l` levels deep and `l` levels wide
    -- where l is the length of the initial string. For each sub-group,
    we can just copy the previous value and omit the last key,
    since it will be previous lists's length - 1."""

    @_test_speed
    def _populate(self):
        """banana_tree = {
            # [banana]
            0: {
            ....
            ...........
            .....................
                                    0: 'ana',  # You get the idea...
                                    1: {
                                        1: 'na',
                                        2: 'n'
                                    },
                                    2: 'n'
                                },
                                1: 'na',
                                2: 'n'
                            },
                            ...
                            ..
                            .
                        },
                        ..

        Lookups:
            "banana" -> banana_tree[0][0]
            "ana" -> banana_tree[0][1][2],
                     banana_tree[0][2][1],
                     banana_tree[0][3][0],
                     ..
                     .

        I'm not sure what the use of what I might call the
        "Recursive SuperSet(TM)" is, but I'm sure it has some interesting
        mathematical properties, like the fact that each subset has exactly
        1 less number of values than the parent -- but I suppose that
        is a pedestrian fact for many recursive structures.

        Another (preferably) visual way to represent this,
        is reminiscent of the example suffix tree generated
        with Ukkonen's algorithm, given in the link.

        I think it's a bit clearer and easier to understand.
        Also, interestingly enough, you can get a normal looking tree by
        tilting this one 45 degrees clockwise around the top corner - (1, 6)

        In this representation, each node is spaced by the len(subst) + 4)
        ... and the 'dimensions' for each node are = (depth, breadth)

        (1, 6)   (5, 5)  (4, 4)  (3, 3)  (2, 2)(1, 1)
        banana    anana    nana    ana    na   n$
        0 --------|--------|-------|------|----|
        |         |        ....    ...    ..   .
        $         (4, 4)  (3, 3) (2, 2) (1, 1)
                  nana    ana    na    n$
                  |-------|------|-----|
                  |       ...    ..    .
                  (3, 3) (2, 2)(1, 1)
                  ana    na    n$
                  |------|-----|
                  |      |     $
                  (2, 2) (1, 1)
                  an     n$
                  |
                 (0, 0) # This gives us another way to represent sentinels
                  a$
        """
        # Defer to a reusable function.
        self.tree = powerset_tree(self.word, terminator='$')


class GeneralizedSuffixTree(DeepSuffixTree):

    """A tree of suffix subtrees -- a suffix forest?"""

    def __init__(self, words):
        self.forest = {}
        for k, word in enumerate(words):
            self.forest[k] = DeepSuffixTree(word)

    def __str__(self):
        for k, tree in enumerate(self.forest):
            print self.forest[k]
        return ''


class UkkonenSuffixTree(BaseSuffixTree):
    """A more efficient algorithm.
    See programmerspatch.blogspot.com.au
        /2013/02/ukkonens-suffix-tree-algorithm.html for more information."""

    def __init__(self):
        raise NotImplementedError


if __name__ == '__main__':
    with Section('Suffix Tree'):
        words = ['peanut', 'butter', 'banana', 'hotdog']

        shallow = ShallowSuffixTree(words[0])
        deep = DeepSuffixTree(words[0])
        forest = GeneralizedSuffixTree(words)

        _print('Shallow suffix tree', shallow)
        _print('Deep suffix tree', deep)
        _print('Generalized suffix tree aka "suffix forest"', forest)

        DEBUG = True
        if DEBUG:
            for _ in range(100):
                keys = range(0, len(words[0]))

                def _rc(choices):
                    return choice(choices)
                try:
                    subset = deep[_rc(keys)][_rc(keys)]
                    if len(subset) > 1 and isinstance(subset, list):
                        _print('Random choice...', subset, func=ppr)
                except IndexError:
                    continue
