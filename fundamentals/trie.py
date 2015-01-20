if __name__ == '__main__':
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from generic_helpers import section
from binary_search_trees import BinarySearchTree

# Inspired by:
# http://www.toptal.com/java/the-trie-a-neglected-data-structure


class NaiveTrie(BinarySearchTree):

    def __init__(self):
        self.path = {}
        self.is_terminal = True

    def add(self, string):
        print 'Adding string {}'.format(string)
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

    def view(self, node=None, spacer=1):
        """A quick and dirty way to view the nested nature of the tree"""
        if node is None:
            node = self
        for letter, _node in node.path.iteritems():
            print '-{}> {} {}'.format(
                '-' * spacer, letter,
                '<>' if _node.is_terminal else '')
            self.view(node=_node, spacer=spacer + 2)


section('BEGIN - Naive Trie structure')

trie = NaiveTrie()

for _ in range(2):
    trie.add('dad')
    trie.add('data')
    trie.add('cat')
    trie.add('cathartic')
    trie.add('data')
    trie.add('mountain')
    trie.add('hoe')
    trie.add('ho')
    trie.add('house')

trie.view()

section('END - Naive Trie structure')
