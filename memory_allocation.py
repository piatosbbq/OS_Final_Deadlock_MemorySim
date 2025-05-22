#Memory allocation
#First fit
def first_fit(memory_blocks, processes):
    #initialize allocation list where -1 means not allocated
    allocation = [-1] * len(processes)
    
    #loop through each process
    for i, process in enumerate(processes):
        #loop through each memory block
        for j, block in enumerate(memory_blocks):
            #check if the block can hold the process
            if block >= process:
                allocation[i] = j
                memory_blocks[j] -= process
                break
    return allocation

#Best fit
def best_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        best_index = -1 #tracks the best block index, smallest suitable
        for j, block in enumerate(memory_blocks):
            if block >= process:
                if best_index == -1 or memory_blocks[j] < memory_blocks[best_index]:
                    best_index = j
        if best_index != -1:
            allocation[i] = best_index
            memory_blocks[best_index] -= process
    return allocation

#Worst fit
def worst_fit(memory_blocks, processes):
    allocation = [-1] * len(processes)
    for i, process in enumerate(processes):
        worst_index = -1 #tracks the worst block index, largest suitable
        for j, block in enumerate(memory_blocks):
            if block >= process:
                if worst_index == -1 or memory_blocks[j] > memory_blocks[worst_index]:
                    worst_index = j
        if worst_index != -1:
            allocation[i] = worst_index
            memory_blocks[worst_index] -= process
    return allocation
