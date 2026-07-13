"""
MSCS 532 - Assignment 5
Empirical comparison of deterministic and randomized Quicksort.

Runs both versions on random, sorted, and reverse-sorted inputs at
several sizes and prints a timing table. Each timing is the average
of 3 runs on fresh copies of the same input.

Author: Frenie Labrador
"""

import random
import time

from quicksort import quicksort
from randomized_quicksort import randomized_quicksort

SIZES = [1000, 2500, 5000, 10000]
RUNS = 3


def make_input(size, kind):
    if kind == "random":
        return [random.randint(0, size * 10) for _ in range(size)]
    if kind == "sorted":
        return list(range(size))
    if kind == "reverse":
        return list(range(size, 0, -1))
    raise ValueError("unknown input kind: " + kind)


def time_sort(sort_fn, data):
    """Average wall-clock time over RUNS runs, in milliseconds."""
    total = 0.0
    for _ in range(RUNS):
        copy = list(data)
        start = time.perf_counter()
        sort_fn(copy)
        total += time.perf_counter() - start
        # sanity check that the output really is sorted
        assert copy == sorted(data)
    return (total / RUNS) * 1000


def main():
    print(f"{'Size':>7} {'Distribution':>13} {'Deterministic (ms)':>20} "
          f"{'Randomized (ms)':>17}")
    print("-" * 62)
    for size in SIZES:
        for kind in ["random", "sorted", "reverse"]:
            data = make_input(size, kind)
            det = time_sort(quicksort, data)
            rnd = time_sort(randomized_quicksort, data)
            print(f"{size:>7} {kind:>13} {det:>20.2f} {rnd:>17.2f}")


if __name__ == "__main__":
    main()
