"""
The idea is to sort the input array, and simply see first if we have
the coin 1. If we do, we know we can make change for amount of 1. If not,
that's the minimum.

Continuing on, we then use change (some number, k) to establish the amount of change we can
make UP to and including that number. If we can make change in the interval [1, k] then
as long as this inequality holds (coin_value <= k + 1) then we can use any amount
in the interval [1, k] + coin_value to extend our interval to [1, k + coin_value] since
we can add (1 + coin_val) = k + 1, or 2 + coin_val = k + 2, ... k + coin_val.

In the event that we NEVER encounter such a coin in the array that is > k + 1 then
we know the minimum change we cannot make is 1 greater than the max change using all
of the coins in the array, since we can make any amount from [1, change] thus we can't
make change + 1 and we return that.
"""


def nonConstructibleChange(coins):
    # validate input, if no coins can't make 1 cent
    if not coins: return 1
    coins.sort()
    # if after sorting 1 isn't first coin, we can't make 1 cent of change
    if coins[0] != 1:
        return 1
    min_change = 0
    for coin in coins:
        if coin > min_change + 1:
            return min_change + 1
        # implicit else, we can now make change for ALL integers in the interval [1, min_change]
        min_change += coin
    # if we never hit the case where a coin is larger than min_change + 1 in entire array, then
    # the min change we can't make is 1 greater than
    # the max change we could make using all of the coins in the array
    return min_change + 1
