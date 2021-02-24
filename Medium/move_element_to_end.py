"""
Simply use 2 pointers starting @ beginning and end (respectively) and ensure that the end pointer is not the
element we need to move, and if it is, move end ptr towards beginning ptr until we find a valid swap. Once
beg ptr == end ptr i.e., i == j we are done swapping and the element 'toMove' has been successfully moved to the
end of the array.
"""


def moveElementToEnd(array, toMove):
    i, j = 0, len(array) - 1
    for i in range(0, len(array) - 1):
        # move j till we find ele to swap, and guard condition
        while array[j] == toMove and i < j:
            j -= 1
        # we're done at this point, moved all occurences of toMove to end
        if i == j: break
        if array[i] == toMove:
            swap(array, i, j)
        return array


def swap(array, i, j) -> None:
    array[i], array[j] = array[j], array[i]
