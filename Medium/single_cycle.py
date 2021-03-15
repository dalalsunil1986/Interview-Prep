def hasSingleCycle(array):
    """
    @param array: array where array[i] is jump in indices from index i
    The idea here is to use the helper function to figure out our next index
    to jump to from any given index in the array. We increment our counter
    to keep track of the number of nodes we've seen, where the actual node
    is not relevant unless we arrive at the starting node prior to visting
    the other nodes, in which case we know that we haven't visited all nodes
    in the array (if counter < n) and we've visited the first node twice.
    If we break out of the while loop i.e., visit all n nodes and end up back at
    the 0th index (node we began at) then there is a single cycle in the graph
    represented by the array. If we visit n nodes (not necessarily distinct)
    and don't arrive back at the 0th node then we know we have visited elements
    in the array more than once and haven't arrived where we began thus there
    is not a single cycle.
    """
    seen_nodes = 0
    n = len(array)
    # start at index 0
    curr_idx = 0
    while seen_nodes < n:
        curr_idx = find_neighbor(curr_idx, jump=array[curr_idx], n=n)
        seen_nodes += 1
        if curr_idx == 0 and seen_nodes < n:
            return False

    return curr_idx == 0


def find_neighbor(curr_idx, jump, n):
    neighbor = (curr_idx + jump) % n
    return neighbor if neighbor >= 0 else neighbor + n
