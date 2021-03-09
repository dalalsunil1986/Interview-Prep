def twoNumberSum(array, targetSum):
    # Write your code here.
    pair_target = set()
    # nums are a and b, i.e., a + b = T
    # and number we iterate on is "a" targetSum - num = "b"
    for a in array:
        # b is needed number (a + b = target)
        b = targetSum - a
        if b in pair_target:
            # if we have the pair, return as list
            return [a, b]
        # else add num to seen set.
        pair_target.add(a)
        # if we get out of the loop we didn't find the pair.
    return []
