def arrayOfProducts(array):
    """
    Keep track of left prod and right prod for any given element, a[i] which denotes the product of all
    elements to the left, and right (respectively). From there, we simply need to return the product
    of the left and right for each a[i] from the original array.
    :param array:
    :return:
    """
    n = len(array)
    left_prods = [1] * n
    right_prods = [1] * n
    # calc all left prods
    for i in range(1, n):
        left_prods[i] = left_prods[i - 1] * array[i - 1]
    # calc all right prods
    for j in reversed(range(len(array) - 1)):
        right_prods[j] = right_prods[j + 1] * array[j + 1]

    return [left_prods[i] * right_prods[i] for i in range(n)]
