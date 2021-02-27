# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


"""
Using 2 pointer method (fast, slow ptrs) such that our second pointer
is k nodes ahead of 1st pointer. We then move the first and second
pointers simultaneously to always maintain 2nd pointer as k nodes ahead,
until we hit the end of the list BUT we break the loop with the 
1st pointer as 1 node prior to the node we need to remove (by exiting when 2nd ptr hits tail instead of null), 
since we just update the next link(s) to effectively delete a node. 
"""


def removeKthNodeFromEnd(head, k):
    if not head or k < 0: return
    # both initially point to head
    slow = fast = head
    num_ahead = 0
    while num_ahead < k:
        fast = fast.next
        num_ahead += 1
    # if fast hits past tail (null node) before we begin to
    # move slow must be the case that k = len(list) so we need to remove head node.
    if not fast:
        head.value = head.next.value
        head.next = head.next.next
        return
    # we want to simply "delete" the node that is k away from the end so
    # we must iterate to 1 node before it, then update next ptrs.
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next.next
