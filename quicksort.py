"""
MSCS 532 - Assignment 5
Deterministic Quicksort implementation.
Pivot strategy: last element of the subarray (Lomuto partition scheme).

Author: Frenie Labrador
"""

import sys

# Deterministic quicksort hits Python's default recursion limit (1000)
# on sorted or reverse-sorted inputs, so the limit is raised here.
sys.setrecursionlimit(20000)


def partition(arr, low, high):
    """Lomuto partition. Uses the last element as the pivot.

    Elements less than or equal to the pivot end up on the left,
    larger elements on the right. Returns the final pivot index.
    """
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low=0, high=None):
    """Deterministic quicksort. Sorts arr in place between low and high."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)
    return arr


if __name__ == "__main__":
    # quick sanity checks
    test1 = [5, 2, 9, 1, 7, 3]
    test2 = []
    test3 = [4]
    test4 = [3, 3, 3, 1, 2, 3]

    print("Before:", test1)
    quicksort(test1)
    print("After: ", test1)

    quicksort(test2)
    print("Empty list:", test2)

    quicksort(test3)
    print("Single element:", test3)

    quicksort(test4)
    print("With duplicates:", test4)
