"""
Use helper function to get the integers out of the list. The head is least significant and the
tail is the most significant, so need it in reverse. Then just grab last digit of number and construct linked list of
LinkedList nodes.
"""


# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

        def __str__(self):
            return self.value


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    list_sum = get_int_list(linkedListOne) + get_int_list(linkedListTwo)
    # make last digit of sum as first node (head)
    newList = LinkedList(list_sum % 10)
    # store ptr to head
    head = newList
    # keep grabbing last digit from the sum and creating new nodes.
    while list_sum >= 10:
        list_sum //= 10
        newList.next = LinkedList(list_sum % 10)
        newList = newList.next
    return head


def get_int_list(linked_list):
    """
    Helper method to get integer out of each list.
    :param linked_list:
    :return:
    """
    as_int = []
    curr = linked_list
    while curr:
        as_int.append(str(curr.value))
        curr = curr.next
    # reverse list before getting int representation
    return int("".join(as_int[::-1]))
