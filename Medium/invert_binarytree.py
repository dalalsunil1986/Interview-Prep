"""
Fairly straightforward.. just swap pointers and continue to recur down the tree until we hit the end of it. Base case
is null node.
"""


def invertBinaryTree(tree):
    helper(tree)
    return tree


def helper(node):
    if not node: return
    node.left, node.right = node.right, node.left
    helper(node.left)
    helper(node.right)


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
