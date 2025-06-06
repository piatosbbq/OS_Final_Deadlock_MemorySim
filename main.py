import matplotlib.pyplot as plt
import memory_allocation as ma
import bankers_algorithm as ba

# input data requirements
memory_blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]

# Run memory allocation simulations
ff = ma.first_fit(memory_blocks.copy(), processes)
bf = ma.best_fit(memory_blocks.copy(), processes)
wf = ma.worst_fit(memory_blocks.copy(), processes)

print("First Fit Allocation:", ff)
print("Best Fit Allocation:", bf)
print("Worst Fit Allocation:", wf)

# Plot results
labels = ['P1', 'P2', 'P3', 'P4']
fig, ax = plt.subplots()
bar_width = 0.2
x = range(len(processes))

ax.bar([p - bar_width for p in x], ff, width=bar_width, label='First Fit')
ax.bar(x, bf, width=bar_width, label='Best Fit')
ax.bar([p + bar_width for p in x], wf, width=bar_width, label='Worst Fit')

ax.set_xlabel('Processes')
ax.set_ylabel('Block Index Allocated')
ax.set_title('Memory Allocation Comparison')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.savefig("process_allocation_chart.png")
plt.show()

# Banker's Algorithm Test
available = [3, 3, 2]
max_demand = [[7, 5, 3], [3, 2, 2], [9, 0, 2], [2, 2, 2], [4, 3, 3]]
allocation = [[0, 1, 0], [2, 0, 0], [3, 0, 2], [2, 1, 1], [0, 0, 2]]

safe, sequence = ba.is_safe_state(available, max_demand, allocation)
print("System is in a safe state:", safe)
if safe:
    print("Safe sequence:", sequence)

    # Visualization of the Banker's Algorithm safe sequence
    fig3, ax3 = plt.subplots(figsize=(8, 2))
    
    for i, p in enumerate(sequence):
        ax3.broken_barh([(i, 1)], (10, 9), facecolors='tab:blue')
        ax3.text(i + 0.5, 14, f'P{p}', ha='center', va='center', color='white', fontsize=10, fontweight='bold')
    
    ax3.set_ylim(5, 25)
    ax3.set_xlim(0, len(sequence))
    ax3.set_xlabel('Execution Order')
    ax3.set_yticks([])
    ax3.set_title('Banker\'s Algorithm Safe Sequence')
    ax3.grid(True, axis='x', linestyle='--', alpha=0.5)

    plt.tight_layout()
    plt.savefig("bankers_algo_sequence_chart.png")
    plt.show()
