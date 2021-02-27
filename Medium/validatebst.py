"""
The key with this problem is ensuring that for any given node the inequality holds:

left_child < tree.value <= right_child

We do this by ensuring that when we recur right, the right child is at least greater than or equal to
the root, and for the left child we make ensure that it is less than the root. However, in our future
recursive calls, we ensure to pass the min and max values from the previous function call to make sure
that EVERY node in some nodes left subtree is < root_subtree and EVERY node in some nodes right subtree
is <= root subtree.
"""


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    return is_valid_BST(tree)


def is_valid_BST(tree, min_value=float('-inf'), max_value=float('inf')) -> bool:
    if not tree: return True
    if not (min_value <= tree.value < max_value): return False
    return is_valid_BST(tree.left, min_value, tree.value) and is_valid_BST(tree.right, tree.value, max_value)
