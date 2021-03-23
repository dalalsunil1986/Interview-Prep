# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    """
    We make use of helper method to first check if root node is balanced,
    then we recur on each child and every node in the tree to ensure those nodes
    are balanced using the is_balanced helper method with height helper method.
    """
    return is_balanced_node(tree)


def height(node):
    if not node: return -1
    return 1 + max(height(node.left), height(node.right))


def is_balanced_node(node):
    # base case, if we hit null node (e.g, recur on leaf w/ no children)
    if not node: return True
    # else, check if node is balanced, and if children are balanced
    node_balanced = abs(height(node.left) - height(node.right)) <= 1
    # then check if left child and right child are balanced all the way down the tree
    return node_balanced and is_balanced_node(node.left) and is_balanced_node(node.right)
