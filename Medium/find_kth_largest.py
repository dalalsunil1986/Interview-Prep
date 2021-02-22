# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


"""
Solution 1: 

Simple in order traversal, we know that the list will be sorted
in ascending order and we just return the node at index:
	(number of nodes) - k to account for 0 indexing. 2nd Solution
involves a reverse in order traversal.
"""


def findKthLargestValueInBst(tree, k):
    nodes = []
    in_order(tree, nodes)
    print(nodes)
    return nodes[len(nodes) - k]


def in_order(node: BST, nodes: list) -> None:
    if not node: return
    in_order(node.left, nodes)
    nodes.append(node.value)
    in_order(node.right, nodes)


"""
Solution 2: Uses a reverse in-order traversal. 
"""


def findKthLargestValueInBst(tree, k):
    nodes = []
    reverse_in_order(tree, nodes, k)
    # kth largest is at index k - 1 w/ 0 indexing.
    return nodes[k - 1]


def reverse_in_order(node: BST, nodes: list, k: int) -> None:
    # have to have len(nodes) == k here as well in case we just
    # appended node and called node.left to avoid unnecessary recursion
    if not node or len(nodes) >= k: return
    reverse_in_order(node.right, nodes, k)
    # before exploring other side of subtree, return if we found
    # the k largest nodes since kth value is in the list, and nodes
    # could've been appended when exploring right side (so may not need
    # to append root of subtree and then go left)
    if len(nodes) >= k: return
    nodes.append(node.value)
    reverse_in_order(node.left, nodes, k)
