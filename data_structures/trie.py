# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import Section
from string import ascii_lowercase
from string import punctuation
from random import choice
from binary_search_trees import BinarySearchTree

# Inspired by:
# http://www.toptal.com/java/the-trie-a-neglected-data-structure


class NaiveTrie(BinarySearchTree):

    def __init__(self, is_root=False, alphabet=None):
        if is_root and alphabet is not None:
            self.path = {token: NaiveTrie() for token in alphabet}
        else:
            self.path = {}
        self.is_root = is_root
        self.is_terminal = True

    def add(self, string):
        char = string[0]
        if char in self.path:
            # If the character exists in the path,
            # just get a reference to that node to continue with.
            node = self.path[char]
        else:
            # Create a new starting point for this
            # string if none exist in the path.
            node = NaiveTrie()
            # Allow a way to "terminate" since some words
            # can be substrings of others.
            # This is naive and doesn't create new branches
            # for substring words, which would be better.
            # See https://www.youtube.com/watch?v=jXAHLqQthKw for
            # examples of a more robust Trie
            self.is_terminal = False
            self.path[char] = node

        # Continue adding the remaining letters recursively
        # until the string is empty.
        if len(string) > 1:
            remains = string[1:]
            # Add the remains to the node in question - important!
            node.add(remains)
        if self.is_terminal:
            self.path['_'] = NaiveTrie()

    def view(self, node=None, spacer=1):
        """A quick and dirty way to view the nested nature of the tree"""
        if node is None:
            node = self
        for letter, _node in node.path.iteritems():
            print '-{}> {} {}'.format(
                '.' * spacer, letter,
                'NULL' if _node.is_terminal else '')
            self.view(node=_node, spacer=spacer + 2)


if __name__ == '__main__':
    with Section('Naive Trie structure - basic'):
        trie = NaiveTrie()
        trie2 = NaiveTrie(is_root=True, alphabet=ascii_lowercase)
        trie3 = NaiveTrie(is_root=True, alphabet=punctuation)

        words = [
            'data', 'dad', 'dada', 'dadism', 'cat', 'cathartic', 'ho', 'house', ]

        # Traditional setup + full width nodes for entire alphabet
        for word in words:
            trie.add(word)
            trie2.add(word)
            trie3.add(''.join([choice(punctuation) for _ in range(5)]))

        trie.view()

    with Section('Naive Trie structure - N-ary , N = alphabet'):
        trie2.view()

    with Section('Naive Trie structure - N-ary , N = alphabet, new alphabet'):
        trie3.view()
