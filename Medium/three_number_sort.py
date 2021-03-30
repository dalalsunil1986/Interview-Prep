def threeNumberSort(array, order):
    """
    Simply find count of each number in the array. Then iterate over it again, seeing if the number
    in order is in the array and if so, write 'n' copies of it in the order it appears in the 'order' array
    to sort 'array' w.r.t to 'order'.
    :param array: array of nums to sort
    :param order: sorting order, i.e., 'array' should have nums in same order they appear in this array
    :return:

    Runs in O(n) time since while loop will only go over array once, and we iterate over they array once prior.
    """
    num_counts = {}
    for num in array:
        num_counts[num] = num_counts.get(num, 0) + 1
    # use to keep track of where we need to overwrite next in 'arra'y.
    i = 0
    for num in order:
        written = 0
        # not all numbers in 'order' second array are in the first one,
        # but all nums in first array ('array') are in 'order. '
        num_writes = num_counts.get(num, 0)
        # in case that num in order isn't in array, written < num_writes = False
        while i < len(array) and written < num_writes:
            array[i] = num
            i += 1
            written += 1

    return array
