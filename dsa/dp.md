There are two ways to store the results, one is top down (or memoization) and other is bottom up (or tabulation).

## When to Use
### Optimal Substructure
Use optimal result of subproblems to receive optimal result of the whole.
e.g. find the min cost path in a weighted graph from a source to dest node. you can break this down by finding the min cost from the source node to each intermediat4e node, then find the min cost from each int node to the dest node.

### Overlapping Subproblems
The same subproblems are solved repeatedly in different parts of the problem.
e.g. computing the fibonacci series. To solve for fib(n), you must solve for fib(n - 1) and fib(n - 2).


## Examples
### Fibonacci
See [fibonacci.py](../python/fibonacci.py)


