"""
O(n) time, O(1) space instead of using set which is O(n) space.
Map each num -> index in array, use abs so index in range: [0, n - 1]
and multiply num at that index to -1.

If we've already seen this number, then we would've multiplied
the number at index we mapped it to by -1 and originally all
integers are positive, so we must have seen the number already, return
it.
"""


def firstDuplicateValue(array):
    for num in array:
        num_mapped_idx = abs(num) - 1
        # check if seen
        if array[num_mapped_idx] < 0:
            # abs. value in case num is at an index we've multiplied by -1
            return abs(num)
        # haven't seen num yet, multiply num @ mapped index
        array[num_mapped_idx] *= -1

    return -1


"""
O(n) time and O(n) space, very straightforward.
"""


def firstDuplicateValue(array):
    seen = set()
    for num in array:
        if num in seen:
            return num
        seen.add(num)

    return -1
