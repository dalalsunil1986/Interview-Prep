"""
The idea here is just to maintain best sum we've seen, and a current sum.
Best sum is -infinity intially because the best sum can be negative if all
the input numbers are negative.

So when we encounter a number array[i] and add to current sum, on the next iteration
if curr_sum + array[i + 1] < array[i + 1] then we know array[i] is NOT part of the
maximum sum subarray in this array, since we are better off with the subarray beginning
at array[i + 1], OR the subarray ending at array[i - 1] since array[i] was a large
negative number. Since array[i] cannot be part of any max sum subarray we reset
the running sum (curr_sum) to be the number array[i + 1] itself since we now
begin summing at array[i + 1].

Recursively we can express this as:

Max sum ending at index i = max(Max sum ending at array[i - 1] + array[i], array[i])
where either we add the number at index i to the running sum calculation, or begin a new
running sum calculation with index i as the beginning of a new subarray.
"""


def kadanesAlgorithm(array):
    best_sum = float('-inf')
    curr_sum = 0
    for num in array:
        # if num > curr_sum + num, we begin to consider a different subarray starting w/ num
        curr_sum = max(curr_sum + num, num)
        best_sum = max(best_sum, curr_sum)

    return best_sum


"""
Similar solution using RR expressed above but adopting more of a DP approach, but it's slower
and uses more memory, O(n) time and O(n) space, requires 2 passes
through array of length n instead of just 1 in first solution. Basically
just builds on the idea that for an element at index i, either the max
sum subarray ending at index i includes or does not include array[i] and
if max_sum_subarray[i] = array[i] this means we are restarting a search
for a max sum subarray. 
"""


def kadanesAlgorithm(array):
    # dp array
    max_sum_subarray = [0] * len(array)
    curr_sum = 0
    for idx, num in enumerate(array):
        curr_sum = max(curr_sum + num, num)
        # if curr_sum = num we are now considering a new subarray.
        max_sum_subarray[idx] = curr_sum

    return max(max_sum_subarray)
