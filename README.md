Project Title: 
Simulating and Analyzing Deadlock and Memory Allocation Strategies in Operating Systems

This study focuses on understanding how deadlocks happen in operating systems and how different memory allocation methods can affect performance. By simulating real-world situations, the research looks at what causes processes to get stuck waiting for each other and how that can slow down or crash a system. It also compares memory allocation strategies like first-fit, best-fit, and worst-fit to see which ones use memory more efficiently. The goal is to learn how these concepts work in practice and how they can be improved to make systems faster and more reliable.

The `is_safe_state` function is an implementation of the Banker's Algorithm used in operating systems to check if a system is in a safe state, meaning no deadlock will occur. It takes in the currently available resources, the maximum demand of each process, and the resources currently allocated to each process. The function calculates how many more resources each process may still request (need), then tries to simulate a safe sequence where each process can complete using available resources. If such a sequence exists and all processes can finish without deadlock, it returns `True` along with the safe execution order. Otherwise, it returns `False`, indicating the system is in an unsafe state.

These three functions—`first_fit`, `best_fit`, and `worst_fit`—are memory allocation strategies used in operating systems for managing how processes are assigned to memory blocks. Each function takes a list of memory block sizes and a list of process sizes, then tries to allocate each process to a suitable block based on a specific strategy.

The `first_fit` function assigns each process to the first memory block that is large enough to hold it. The `best_fit` function searches for the smallest available block that can fit the process, aiming to minimize wasted space. In contrast, the `worst_fit` function allocates the process to the largest available block, trying to leave larger chunks of memory free for future allocations. All three functions return a list indicating the index of the memory block each process was assigned to, or -1 if it couldn't be allocated.


MEMBERS AND ROLES:

AZARCON, Christian Jull G.
- Researcher
- Programming & Algorithm Implementation 
- Testing Support
- Final Polishing
  
DIANO, Maxzine Arly V.
- Researcher
- Documentation & Report Writing
- Video Editing 
- Final Polishing
  
PERIN, Mariel B.
- Researcher
- Programming & Algorithm Implementation 
- Testing Support
- Final Polishing
  
RAFER, Britney P.
- Researcher
- Programming & Algorithm Implementation 
- Testing Support
- Final Polishing
  
SOTELO, Shantelle C.
- Researcher
- Documentation & Report Writing
- Video Editing 
- Final Polishing

