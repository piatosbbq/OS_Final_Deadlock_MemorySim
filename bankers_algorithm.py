def is_safe_state(available, max_demand, allocation):
    n_processes = len(allocation)
    n_resources = len(available)

    need = [[max_demand[i][j] - allocation[i][j] for j in range(n_resources)] for i in range(n_processes)]
    finish = [False] * n_processes
    safe_sequence = []

    work = available[:]

    while len(safe_sequence) < n_processes:
        found = False
        for i in range(n_processes):
            if not finish[i] and all(need[i][j] <= work[j] for j in range(n_resources)):
                for j in range(n_resources):
                    work[j] += allocation[i][j]
                finish[i] = True
                safe_sequence.append(i)
                found = True
                break
        if not found:
            return False, []
    return True, safe_sequence
