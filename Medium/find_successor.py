# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    """
    :param tree: BST with nodes
    :node node: BST node to find in tree
    :return: node that succeedes 'node param' from performing in-order traversal on tree

    We just perform the in order traversal, and then iterate through the array
    and find the node, and return the node that was traversed directly after it.
    """
    output = []
    in_order_traverse(tree, find=node, array=output)
    found = False
    for curr_node in output:
        if found: return curr_node
        if curr_node == node:
            found = True

    return None


def in_order_traverse(tree, find, array):
    if tree.left:
        in_order_traverse(tree.left, find, array)
    array.append(tree)
    if tree.right:
        in_order_traverse(tree.right, find, array)
