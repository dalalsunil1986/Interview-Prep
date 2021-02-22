"""
Store root first. We are guaranteed to either go left, or go right.
Once we choose a direction, see if current node we're on is closer
than value of root of the subtree and adjust accordingly. On first
pass we just check root against itself but on all other iterations
we're checking against a new node. Placing this at the top of the
while loop ensures we don't attempt to deref a null node if we've
traversed onto one within the loop (instead of checking after traversal
at bottom of the loop.)

O(log n) time since BST (assuming balanced) else O(n) and O(1) space.
"""


def findClosestValueInBst(tree, target):
    # store root val initially, will use to store closest node val
    closest_val = tree.value
    while tree:
        if abs(target - closest_val) > abs(target - tree.value):
            closest_val = tree.value
        if target >= tree.value:
            tree = tree.right
        else:
            tree = tree.left

    return closest_val


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
