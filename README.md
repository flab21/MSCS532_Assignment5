# MSCS532_Assignment5

Quicksort: Implementation, Analysis, and Randomization

## Files

- `quicksort.py` - deterministic Quicksort (Lomuto partition, last element as pivot)
- `randomized_quicksort.py` - randomized Quicksort (pivot chosen uniformly at random)
- `benchmark.py` - times both versions on random, sorted, and reverse-sorted inputs
- `Assignment5_Report.docx` - full report with design choices, complexity analysis, and results

## How to Run

Requires Python 3. No external libraries needed.

Test the deterministic version:

```
python3 quicksort.py
```

Test the randomized version:

```
python3 randomized_quicksort.py
```

Run the full benchmark (takes about 30 seconds because of the deterministic worst cases):

```
python3 benchmark.py
```

## Summary of Findings

On random inputs both versions run in O(n log n) time and the deterministic version is slightly faster since it skips the random pivot selection overhead. On sorted and reverse-sorted inputs the deterministic version degrades to O(n^2) because the last-element pivot always produces the most unbalanced split possible. At 10,000 elements, sorted input took the deterministic version about 4,636 ms while the randomized version finished in about 17 ms. Doubling the input size roughly quadrupled the deterministic version's time on sorted input, matching the quadratic prediction. Randomization does not improve the worst-case bound, but it makes the worst case depend on the algorithm's own random choices instead of the input's arrangement, so no specific input can reliably trigger it. The expected running time of the randomized version is O(n log n) on every input.

Note: both scripts raise Python's recursion limit because the deterministic version's recursion depth equals the array length on sorted inputs, which exceeds Python's default limit of 1,000.
