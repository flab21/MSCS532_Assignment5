"""
MSCS 532 - Assignment 5
Randomized Quicksort implementation.
The pivot is chosen uniformly at random from the subarray, then swapped
to the last position so the same Lomuto partition logic can be reused.

Author: Frenie Labrador
"""

import random
import sys

sys.setrecursionlimit(20000)


def randomized_partition(arr, low, high):
    """Pick a random pivot index, swap it to the end, then partition."""
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]

    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def randomized_quicksort(arr, low=0, high=None):
    """Randomized quicksort. Sorts arr in place between low and high."""
    if high is None:
        high = len(arr) - 1
    if low < high:
        p = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, p - 1)
        randomized_quicksort(arr, p + 1, high)
    return arr


if __name__ == "__main__":
    test1 = [5, 2, 9, 1, 7, 3]
    test2 = [10, 9, 8, 7, 6, 5]
    test3 = [1, 2, 3, 4, 5]

    print("Before:", test1)
    randomized_quicksort(test1)
    print("After: ", test1)

    randomized_quicksort(test2)
    print("Reverse sorted input:", test2)

    randomized_quicksort(test3)
    print("Already sorted input:", test3)
