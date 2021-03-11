def taskAssignment(k, tasks):
    """
    The idea here is to simply pair the tasks that take the longest time with those that take the shortest time, since
    we have exactly k workers, and 2k tasks and the minimum amount of time to complete the 2k tasks is considered to be
    the length of time for the pair max(tasks[i] +  tasks[j]) over all i != j. Thus, we want to pair tasks that take
    the longest time with those that take the shortest time to minimize the sum of any given pair (task[i], task[j])
    but we also need to keep track of the indices which we do with the initial dictionary prior to sorting the tasks
    list.
    :param k: number of workers
    :param tasks: list of tasks where task[i] is time taken to complete task[i]
    :return: list of k task assignments for the k workers.
    """
    original_indices = {}
    for idx, task in enumerate(tasks):
        original_indices.setdefault(task, []).append(idx)

    tasks.sort()
    i, j = 0, len(tasks) - 1
    task_list = []
    while i <= j:
        # ensure to pop out indices because time for tasks need not be unique and we can't reuse index from orig. list
        task1idx, task2idx = original_indices[tasks[i]].pop(), original_indices[tasks[j]].pop()
        task_list.append([task1idx, task2idx])
        i += 1
        j -= 1
        return task_list
