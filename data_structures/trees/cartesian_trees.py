# -*- coding: utf-8 -*-

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

from helpers.display import Section
from helpers.display import prnt
from data_structures.abstract.tree import Tree
from data_structures.trees.binary_search_trees import BinarySearchTree

DEBUG = True if __name__ == '__main__' else False


class InsufficientNodes(Exception):
    pass


"""From Wikipedia:

    "In computer science, a Cartesian tree is a binary tree derived
    from a sequence of numbers; it can be uniquely defined from the
    properties that it is heap-ordered and that a symmetric (in-order)
    traversal of the tree returns the original sequence.

    [they've] also been used in the definition of the treap and randomized
    binary search tree data structures for binary search problems."

Indices:  0  1  2  3  4  6   7   8   9   10  11
Numbers: [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]

An easy way to imagine it is this:
The index determines horizontal position, while the number value
determines vertical position. The smallest number is always the root,
and the largest number is always at the bottom. However, unlike a
binary search tree, left/right position does not determine how big or
small the number is. It does have the *heap property* however, where
nodes above are smaller than the ones below.

The point here is that you can recreate the entire sequence by traversing
the tree left-to-right (aka "symmetric" aka "in-order").

== Construction ============================================================

I have found a useful way to construct the tree on paper, using an
intuitive approach to visualizing the sequence, and recursively building it.

Taking the list in its entirety:

[9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]

I find it's easy to think of the list as being broken down into sub-lists,
where each sub-list has a left, pivot, and right side.

With this in mind, we can find the pivot, which is always going to the
smallest number, and then divide the list up into a sublist,
where the first index is the left, and second index is the right,
and we pop the pivot off, and add it to the `parents` list.

0. [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5] (start position)
1. [9, 3, 7], [8, 12, 10, 20, 15, 18, 5], parents = [1]
2. [[9, 7]], [[8, 12, 10, 20, 15, 18], []], parents = [1, 3, 5]
3. [[9, 7]], [[], [12, 10, 20, 15, 18]], parents = [1, 3, 5, 8]
4. [[9, 7]], [[], [[12], [20, 15, 18]]], parents = [1, 3, 5, 8, 10]
5. [[9, 7]], [[], [[12], [[20], [18]]]], parents = [1, 3, 5, 8, 10, 12]
... done!

We just keep doing this until there are no more lists left with length > 2.
Keep in mind, we need to maintain the parent/child relationship, where
pivot is the parent of the left and right child, otherwise we will just end
up with a list of lists, all of which have a single value.

Based on the order of appending, we can infer the relationship of parent
nodes from the `parents` list: [1 -> 3 -> 5 -> 8 -> 10 -> 12]

If a list has length 2, then it cannot be sub-divided. This means it's a
sibling of the current siblings.

Another intuitive way to visualize it, is to do the above procedure,
but for each pivot, draw a line up/down to the previous pivot,
and then draw lines from the current pivot to the left and right children.
At the end, you'll get an actual tree drawing!"""


class NaiveCartesianTree(BinarySearchTree):
    """We use the original BST that operates more like a tree (instantiated
    classes of 'nodes' with pointers, vs. a dictionary) to illustrate the tree
    properties. However, the non-naive version is more suitable for real usage,
    but the fact it uses a dictionary makes the general understanding harder,
    because the left/right binary nature is not intuited
    from a dictionary of references ("pseudo-pointers").
    """


class CartesianTree(Tree):
    """A more realistic (but harder to grok) implementation using our
    easier/faster/performant dictionary based implementation. The primary
    encoding algorithm lives here as a staticmethod, so that other tree
    implementations can still use it."""

    def __init__(self, seq):
        """Add sequence to self. The Online Encyclopedia of Integer Sequences
        (oeis.org) is a great place to find testing numbers.

        See oeis.org/wiki/Welcome#Some_Famous_Sequences for some examples.
        # We require a valid sequence here, so we don't have to check the length
        # in each and every function.

        Args:
            seq: A list of integers.
        Returns:
            None
        Raises:
            InsufficientNodes: if there are > 2 nodes.
        """
        if len(seq) < 2:
            raise InsufficientNodes('You need at least two nodes to start.')
        self.sequence = seq

    @staticmethod
    def case_two(seq):
        """There are two sub-types here:
        A. Left child only [2, 1]
        B. Right child only [1, 2]
        *However* In a true binary three, if the tree/sub-tree has a single
        leaf, that leaf is automatically the left child -- there is no such
        thing as *only* a right child leaf. In reality, this kind of breaks
        the rule of a binary tree. A cursory Google search hasn't yielded an
        explanation here, so we're going to differentiate between a single left
        and a single right for case two and beyond.
        Args:
            seq: A list of integers.
        Returns:
            A list, with sub-lists for left and right-children.
            e.g. [2, 3, 1, 4] -> [1, [2, 3], [4]]
        """
        if not isinstance(seq, list):
            return seq
        if len(seq) < 2:
            return seq
        return [min(seq), [max(seq)]]

    @staticmethod
    def case_n(seq):
        """There are three sub-types here:
        A. Left children only: [3, 2, 1]
        B. Right children only: [1, 2, 3]
        C. Left and right children: [2, 1, 3] (or [3, 1, 2]).
        Args:
            seq: A list of integers.
        Returns:
            A list, with sub-lists for left and right-children.
            e.g. [2, 3, 1, 4] -> [1, [2, 3], [4]]
            The list is derived from a *single* iteration -- subsequent
            iterations are done in the create method.
        """
        if not isinstance(seq, list):
            return seq
        if len(seq) < 3:
            return CartesianTree.case_two(seq)
        parent = min(seq)
        parent_index = seq.index(parent)
        left, right = seq[:parent_index], seq[parent_index + 1:]
        if not DEBUG:
            print('seq: {}, results: {}'.format(seq, [parent, left, right]))
        return [parent, left, right]

    @staticmethod
    def is_leaf_lst(res):
        """Determine if the list (e.g. [1, [2], [3]]) has no children
        or is empty, which is encoded as being a leaf node.
        Args:
            res: the result to determine leaf status from.
        Returns:
            True or False.
        """
        try:
            left, right = res[1], res[2]
        except IndexError:
            return True
        return len(left) == 0 and len(right) == 0

    @staticmethod
    def subdivide(seq, count=0):
        """Iteratively subdivides the list, using atomic, helper methods.
        Args:
            seq: (sequence) ... a list of integers.
            count: optional ... a count for profiling the recursive call stack.
        Returns:
            A list of lists, encoding the entire tree and relationship
            between parent/child and corresponding left/right nodes.
        """
        if DEBUG:
            atom = '_'
            print('|{} Starting sequence: {}'.format(count * atom, seq))
            print('Recursive call count: {}'.format(count))
        res = CartesianTree.case_n(seq)
        if DEBUG:
            print('|{} Resulting subdivision: {}'.format(count * atom, res))

        # If it's a list (otherwise it's a single integer,
        # representing the parent.) and it's not a leaf, keep chugging along
        # with the "manual" sub-divisions.
        if isinstance(seq, list) and not CartesianTree.is_leaf_lst(res):
            members = len(res)
            if members == 3:
                parent, left_child, right_child = res[0], res[1], res[2]
            elif members == 2:
                parent, left_child, right_child = res[0], res[1], []
            elif members == 1:
                parent, left_child, right_child = res[0], [], []
            else:
                parent, left_child, right_child = [], [], []
                return [parent, left_child, right_child]
        else:
            return res

        # Recursively subdivide left and right, until the above code catches
        # the sentinel values.
        count += 1
        left_child = CartesianTree.subdivide(left_child, count=count)
        count += 1
        right_child = CartesianTree.subdivide(right_child, count=count)
        if DEBUG:
            prnt(
                'Final result:',
                '{}'.format([parent, left_child, right_child]))
        # Return the entire nested root/children structure.
        return [parent, left_child, right_child]

    def encode(self):
        """Encode the objects' sequence data as a normal graph
        representative dictionary.
        Args:
            None
        Returns:
            A list of lists, indicating the tree structure.
            See :subdivide for more info.
        """
        self.sequence = CartesianTree.subdivide(self.sequence)
        self.normalize()

    def normalize(self):
        """Normalizes the sequence into a format
        usable by the base tree implementation."""
        normalized = {}
        root = self.sequence[0]

        # TODO:
        # Normalize for parent, using dictionary.

        # Encode the typical, required format to the tree structure
        # using the parent method, once normalized.
        return super(CartesianTree, self).__init__(normalized)


if DEBUG:
    with Section('Cartesian Trees'):
        # Sub-sample of primes. See oeis.org/A000043 for all of them.
        wikipedia = [9, 3, 7, 1, 8, 12, 10, 20, 15, 18, 5]
        mersenne_primes = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107]
        simple_test = [4, 3, 1, 2, 5, 6]
        cartesian_tree = CartesianTree(simple_test)

        """Basic sub-case algorithm testing."""

        # Cases [x, x]
        assert CartesianTree.case_two([1, 2]) == [1, [2]]
        assert CartesianTree.case_two([2, 1]) == [1, [2]]
        # Cases [x, x, x]
        assert CartesianTree.case_n([3, 2, 1]) == [1, [3, 2], []]
        assert CartesianTree.case_n([1, 2, 3]) == [1, [], [2, 3]]
        assert CartesianTree.case_n([3, 1, 2]) == [1, [3], [2]]
        # Cases [x, x, x, x]
        assert CartesianTree.case_n([1, 2, 3, 4]) == [1, [], [2, 3, 4]]
        assert CartesianTree.case_n([4, 3, 2, 1]) == [1, [4, 3, 2], []]
        assert CartesianTree.case_n([4, 2, 3, 1]) == [1, [4, 2, 3], []]
        assert CartesianTree.case_n([4, 3, 2, 1]) == [1, [4, 3, 2], []]
        assert CartesianTree.case_n([4, 1, 3, 2]) == [1, [4], [3, 2]]
        assert CartesianTree.case_n([4, 3, 1, 2]) == [1, [4, 3], [2]]
        assert CartesianTree.case_n([2, 1, 3, 4]) == [1, [2], [3, 4]]
        # Cases [x, x, x, x, x]
        assert CartesianTree.case_n([1, 2, 3, 4, 5]) == [1, [], [2, 3, 4, 5]]
        assert CartesianTree.case_n([5, 4, 3, 2, 1]) == [1, [5, 4, 3, 2], []]
        assert CartesianTree.case_n([5, 4, 1, 2, 3]) == [1, [5, 4], [2, 3]]
        assert CartesianTree.case_n([3, 2, 1, 5, 4]) == [1, [3, 2], [5, 4]]
        assert CartesianTree.case_n([5, 2, 1, 4, 3]) == [1, [5, 2], [4, 3]]
        # ...etc
        # Cases [x, x, x, x, x, x, x, x] (8)
        assert CartesianTree.case_n([4, 2, 3, 1, 5, 6, 7, 8]) == [
            1, [4, 2, 3], [5, 6, 7, 8]]

        cartesian_tree.encode()
        prnt('Testing re-sequence to original list', '')
        print(cartesian_tree)

        # TODO: more assertions here...
