"""
Using 2 pointer technique to find larger of the two values in array from beginning vs. end since there may be negative
numbers, and filling the output array accordingly.
"""


def sortedSquaredArray(array):
    n = len(array)
    sorted_squares = [0] * n
    i, j = 0, n - 1
    to_fill = n - 1
    while i <= j:
        left, right = abs(array[i]), abs(array[j])
        if right > left:
            sorted_squares[to_fill] = right ** 2
            j -= 1
        else:
            sorted_squares[to_fill] = left ** 2
            i += 1
        to_fill -= 1

    return sorted_squares
