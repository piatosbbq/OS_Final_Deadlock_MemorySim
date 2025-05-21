def first_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        for j, block in enumerate(memory_blocks):
            if block >= process:
                allocation[i] = j
                memory_blocks[j] -= process
                break
    return allocation

def best_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        best_index = -1
        for j, block in enumerate(memory_blocks):
            if block >= process:
                if best_index == -1 or memory_blocks[j] < memory_blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            memory_blocks[best_index] -= process
    return allocation

def worst_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        worst_index = -1
        for j, block in enumerate(memory_blocks):
            if block >= process:
                if worst_index == -1 or memory_blocks[j] > memory_blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            memory_blocks[worst_index] -= process
    return allocation
