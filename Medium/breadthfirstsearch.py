# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    # sol 1
    def breadthFirstSearch(self, array):
        """
        Sol 1: This method uses a deque whereas the other uses a list, but pop front is O(n) with list and O(1) with
        a deque and here we just append node name when we pop out of queue (i.e., when we visit it). This way is in line
        with the conventional implementation of BFS with adding node to "seen" list as soon as we visit it, one-by-one
        instead of adding all the children of a node when we visit it.

        Sol 2: We instead add all of the children of a node to the output array as soon as we visit it instead of adding
        each child one by one when we visit them (i.e., when they are popped). This works because we add the root
        initially, and then ALL of its children on first iteration, then all children of left child on next iteration,
        then all children of mid/right child on next iteration, etc.
        :param array:
        :return:
        """
        bfs_queue = deque()
        bfs_queue.append(self)
        while bfs_queue:
            # node visited, add to array after popping
            curr_node = bfs_queue.popleft()
            array.append(curr_node.name)
            # put all children nodes of current node in queue to visit
            bfs_queue.extend(curr_node.children)
        return array

    # sol 2
    def breadthFirstSearch(self, array):
        bfs_queue = [self]
        array.append(self.name)
        while bfs_queue:
            node = bfs_queue.pop(0)
            array.extend([node.name for node in node.children])
            bfs_queue.extend(node.children)
        return array
