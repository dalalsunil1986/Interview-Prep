"""
The idea here is that we want to solve the subproblems of making change in the interval
of [0, n] where n is the amount we need to make change for and use the solutions to
those subproblems to solve the min number of coins needed for the amount "n".

So the minimum number of coins needed for any arbitrary amount in [0, n] say i,
is simply defined by the RR:

min_coins[i] = min(min_coins[i], 1 + min_coins[i - current_denom])

Base case is if i = 0.

In other words, the minimum number of coins we need to make change for a given amount is
the lesser of the current minimum using previous denominations, or we use the current denomination
plus the min number of coins needed to make change for the difference between the amount - current denomination.

We initialize all values @ the indices which represent amounts to be infinity because it
is possible that we are unable to make change for a given amount and we'd want to return -1
in that scenario.
"""


def minNumberOfCoinsForChange(n, denoms):
    min_num_coins = [float('inf')] * (n + 1)
    min_num_coins[0] = 0  # base case, min # ways to make change for 0 is 0.
    for denom in denoms:
        for amount in range(n + 1):
            if amount >= denom:
                min_num_coins[amount] = min(min_num_coins[amount], 1 + min_num_coins[amount - denom])

    return min_num_coins[n] if min_num_coins[n] != float('inf') else -1
