# -*- coding: utf-8 -*-

# Mostly taken from
# interactivepython.org/runestone/static/pythonds/Trees/balanced.html

if __name__ == '__main__':
    from os import getcwd
    from os import sys
    sys.path.append(getcwd())

import data_structures.binary_search_trees as bst
from helpers.display import Section


class AVLTree(bst.BinarySearchTree):
    """AVL tree nodes all calculate a balance factor to determine rotations
    and keep tree in balance for best performance:

    bf = height(left_sub_tree) - height(right_sub_tree)

    -1, 0, 1 balance factors are all considered to be within balanced range.

    unbalanced tree

        (-2)
        /  \
       /    \
    (0)      (-1)
             /  \
            /    \
          (0)    (-1)
                   \
                    \
                    (0)

    """

    def _put(self, key, val, current_node):
        print('putting new node: {} {}'.format(key, val))
        if key < current_node.key:
            # Recursively check the current node
            # for a child, until we get to an empty spot to a leaf
            # that we an add a node to.
            if current_node.has_left_child():
                self._put(key, val, current_node.left_child)
            else:
                # Otherwise, create a brand new left node, making
                # this the parent, and then re-balance them.
                current_node.left_child = bst.Node(
                    key, val, parent=current_node)
                self._update_balance(current_node.left_child)
        # Same as above, for the right side.
        else:
            if current_node.has_right_child():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = bst.Node(
                    key, val, parent=current_node)
                self._update_balance(current_node.right_child)

    def _update_balance(self, node):
        print('updating balance...')
        bst.recurse_bst(self.root, None)
        # Updates the balance factor for all nodes if necessary
        bf = node.balance_factor
        # -1, 0 or 1 are considered balanced. Anything else needs a re-balance.
        if bf > 1 or bf < -1:
            self._rebalance(node)
            return
        # Adjust balance factor for nodes that do not require re-balancing.
        if node.parent is not None:
            # If this node has a parent and is a left child,
            # then increase its balance factor
            if node.is_left_child():
                node.parent.balance_factor += 1
            # If parent and right child, decrease its balance factor
            elif node.is_right_child():
                node.parent.balance_factor -= 1
            # Update BF for nodes with non-zero balance factors
            if node.parent.balance_factor != 0:
                # Keep updating and checking balance until
                # re-balance has fixed all nodes.
                self._update_balance(node.parent)

    def _rotate_left(self, rotation_root):
        print('rotating left...')
        # Rotation root is the node this transformation rotates about.
        new_root = rotation_root.right_child
        # Store a copy of the rotation root, make the rotation roots' right
        # child the original copies left child.
        rotation_root.right_child = new_root.left_child
        # If the left child exists, make its parent the rotation root.
        if new_root.left_child is not None:
            new_root.left_child.parent = rotation_root
        # Set the new roots' parent to be the
        # rotation roots' right child parent
        new_root.parent = rotation_root.parent
        # If the rotation root was the root node for the entire tree,
        # set this node as the new root.
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_left_child():
                rotation_root.parent.left_child = new_root
            else:
                rotation_root.parent.right_child = new_root
        # Swap the rotation root node with the new root and
        # update the parent reference
        new_root.left_child = rotation_root
        rotation_root.parent = new_root
        # Update all the balance factors:
        # rotation root should no longer be root, so its BF is subtracted
        # by the minimum balance factor of the new root.
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(
            new_root.balance_factor, 0)
        # The new root is now the root node, so it should be updated to
        # account for all nodes now underneath it, by finding the maximum
        # of the rotation roots' balance factor.
        new_root.balance_factor = new_root.balance_factor + 1 + max(
            rotation_root.balance_factor, 0)

    def _rotate_right(self, rotation_root):
        print('rotating right...')
        new_root = rotation_root.left_child
        rotation_root.left_child = new_root.right_child
        if new_root.right_child is not None:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right_child = new_root
            else:
                rotation_root.parent.left_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = rotation_root.balance_factor + 1 - min(
            new_root.balance_factor, 0)
        new_root.balance_factor = new_root.balance_factor + 1 + max(
            rotation_root.balance_factor, 0)

    def _rebalance(self, node):
        print('rebalancing... node with value {}, current BF = {}'.format(
            node.key, node.balance_factor))
        bst.recurse_bst(self.root, None)

        if node.balance_factor < 0:
            # If the current nodes balanace factor is < 0, and its right
            # child's balance factor is > 0, rotate both sides, right and left.
            # Otherwise, just rotate the left side, if the right child is
            # not unbalanced.
            if node.right_child is not None:
                if node.right_child.balance_factor > 0:
                    self._rotate_right(node.right_child)
                    self._rotate_left(node)
                else:
                    self._rotate_left(node)
        # If the balance factor of this node is > 0, then do the opposite
        # rotation for both child nodes.
        elif node.balance_factor > 0:
            if node.left_child is not None:
                if node.left_child.balance_factor < 0:
                    self._rotate_left(node.left_child)
                    self._rotate_right(node)
                else:
                    self._rotate_right(node)
        print('New BF for node with value {} is {}'.format(
            node.key, node.balance_factor))
        bst.recurse_bst(self.root, None)


if __name__ == '__main__':
    with Section('AVL Trees'):
        avl = AVLTree()
        bst.populate_bst(avl, count=5)
