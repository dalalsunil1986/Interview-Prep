"""
We want to use solutions to smaller subproblems to approach this problem.
So we define a recurrence relation as such:

The number of ways to make change for an amount, n, given a denomination
can be expressed as:

ways[amount] = ways[amount] + ways[amount - denomination]

Because the number of combinations of coins we can use to make change
for an amount is nothing but the number of ways we could make change
for that amount taking all previous denominations into account, plus
the difference between the amount and the current denomination, since
we can use all combinations of prior denomination coins that sum to
that difference and just add the current denomination to the sum to
reach the amount.

Initially for the first denomination the ways array will have values
for each ways[amount] <= 1 since only 1 denomination, but as we iterate
through the denominations, we build up the number of ways[amount]
by using the solutions to the subproblems, ways[amount - denomination]
since as just mentioned above, we know we can make up that difference
using coins of other denominations.

Base case:
ways[0] = 1 trivially because we can make change for an amount of 0
by not using any coins, and when we iterate through and say amount = 10
and denomination = 10, the difference is 0 so we know we can use that
denomination to make change for the amount so the number of ways would
increase by 1, i.e., ways[0] since ways[0] = 1.

Used extra variables to enhance readability and understanding of the algorithm instead of just one linear for
the formula.
"""


def numberOfWaysToMakeChange(n, denoms):
    ways_change = [0] * (n + 1)
    # base case, 1 way to make change for amount of 0
    ways_change[0] = 1
    # for each denomination coin, we figure out how many ways we can make change for an amount
    # in the interval: [denom, n] then use the solutions to these subproblems for future denominations.
    for denom in denoms:
        for amount in range(0, len(ways_change)):
            if denom <= amount:
                # currently computed # of ways to make change for the amount w/ previously seen denominations
                ways_prior_denoms = ways_change[amount]
                # ways we can make change for the difference between amount and current denom coin
                ways_change_diff = ways_change[amount - denom]
                # updated number of ways is simply # ways before we saw this denom, plus # ways for (amount - denom)
                ways_change[amount] = ways_prior_denoms + ways_change_diff
                # ways_change[amount] += ways_change[amount - denom]
    return ways_change[n]
