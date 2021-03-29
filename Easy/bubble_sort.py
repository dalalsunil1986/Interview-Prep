def bubbleSort(array):
    """"
    Simple, just keep swapping while number of swaps changes from last iteration to the next. Runs
    in O(n^2) time. If we don't make anymore swaps on a pass through the array, then it's completely sorted.
    """
    last_num_swaps = 1
    swaps = 0
    while last_num_swaps != swaps:
        last_num_swaps = swaps
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                swap(array, i, i + 1)
                swaps += 1

    return array


def swap(array, i, j):
    array[i], array[j] = array[j], array[i]
