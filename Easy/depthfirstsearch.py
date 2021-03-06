"""
The idea is to just use the method to recur on each child in the children [] list and append the child immediately
to the output array, then begin exploring the children of that child, and the children of that child.. etc. until we
exhaust exploring all of the children and append them to the output array. Have to ensure to call the method on each
node since it's a class method for the Node class.

The base case is when we hit a node such that self.children = [] since the for loop won't execute and we'll simply
return to the last node we were exploring (since some child of it had no children) and explore its next child.
"""


# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # append name of node we're exploring, then immediately explore first child of that node (append its name, then
        # explore it's children i.e., take its children's first child and keep exploring)
        array.append(self.name)
        for child in self.children:
            child.depthFirstSearch(array)

        return array
