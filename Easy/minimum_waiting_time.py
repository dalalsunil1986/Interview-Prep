"""
The greedy approach is to simply sort on wait times (ascending) and
continuously schedule tasks with the shortest waiting time since we
want to minimize the total sum of waiting times as we have to add
the cumulative waiting time up to the [i-1^{th}] task we see
to the running sum when we are on task i and our total waiting time
is the sum of all the waiting times that are built up through scheduling tasks.
"""


def minimumWaitingTime(queries):
    queries.sort()
    total_wait = curr_wait = 0
    for i in range(1, len(queries)):
        # time query i has to wait to execute based on prior queries
        curr_wait += queries[i - 1]
        # total wait times of all queries increases by wait time for query i
        total_wait += curr_wait

    return total_wait
