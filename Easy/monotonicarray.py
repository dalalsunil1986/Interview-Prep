"""
1. Figure out if array should be MI or MD, or flat (if flat it won't be MI and shouldn't have any increases)
2. Iterate through array and check for violation based on MI or MD.
"""


def isMonotonic(array):
    n = len(array)
    # trivially monotonic if array has 1 or no elements
    if n < 2: return True
    # check if monotonic incr, decr (if flat then 2nd case handles this since shouldn't increase)
    monotonic_incr = array[0] < array[n - 1]
    for i in range(1, n):
        # if array is supposed to MI and we see a decrease or if MD and we see an increase, found violation.
        if (monotonic_incr and array[i] < array[i - 1]) or (not monotonic_incr and array[i] > array[i - 1]):
            return False

    return True
