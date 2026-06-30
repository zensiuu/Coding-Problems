"""
MINI CODING TEST — targets the specific bugs found in assignment.py

Each question is a stripped-down version of the original. No imports needed
beyond what's given. Write your code below each function stub and run this
file to check your answers.
"""

import random
import time

# =============================================================
#  1.  is_sorted  (fix yours)
# =============================================================
# Your original had:
#   - unreachable 'pass' before the real code
#   - `arr[i+1] >= i`  (comparing a value to an index)
#   - wrong indentation on the 'return True'
#
# Fix it so all 6 assertions pass.

def is_sorted(arr):
    # TODO: write correct implementation here
    pass


# =============================================================
#  2.  selectionSort  (implement correctly)
# =============================================================
# Your original used:
#   for i in range(arr):       ← iterates over VALUES, not indices
#   arr[i+1] > arr[i]          ← this is bubble-sort logic, not selection sort
#
# Correct algorithm:
#   1. For each position i from 0 to n-1:
#      a. Assume the smallest unsorted element is at index i
#      b. Scan the rest of the array (j = i+1 .. n-1) to find the actual minimum
#      c. Swap arr[i] with arr[min_idx]

def selectionSort(arr):
    # TODO: implement correct selection sort
    pass


# =============================================================
#  3.  benchmark_trials  (implement correctly)
# =============================================================
# Your original just had `df.groupby(...)['Times'].std()` as a loose
# expression and the placeholder "(HELP)".
#
# This function is identical to benchmarking() from benchmarking.py
# except it returns two DataFrames: (means, stds).

import pandas as pd

# Un-comment the imports below once you have your function ready:
# import bubblesort
# import mergeSortAlgo
# import countingSort
# import insertionSort
# import quickSort

def benchmark_trials(algorithms, sizes, runs):
    # TODO: build a DataFrame like benchmarking() does,
    #       then group by ['Sort', 'Size'] and return
    #       (means, stds)  — two DataFrames.
    pass


# =============================================================
#  4.  compare_sorting_algorithms  (implement correctly)
# =============================================================
# Your original had:
#   - nested def inside another def
#   - invalid comprehension: `random.randint(...)for ...`
#   - `arr.copy(5)`  (copy() takes no arg)
#   - `for i in rangr(...)`  (typo + wrong logic)
#
# Implement:
#   1. Generate ONE random array of length 2000, values 0-100
#   2. Make 5 COPIES with .copy()
#   3. Time each algorithm on its own copy
#   4. Print results sorted fastest → slowest

# Un-comment after implementing:
# import bubblesort
# import mergeSortAlgo
# import countingSort
# import insertionSort
# import quickSort

def compare_sorting_algorithms():
    # TODO: implement
    pass


# =============================================================
#  TESTS  —  run this file to see how you did
# =============================================================

def _test_is_sorted():
    points = 0
    cases = [
        ([], True),
        ([5], True),
        ([1, 2, 3], True),
        ([3, 2, 1], False),
        ([1, 3, 2], False),
        ([1, 1, 2, 2], True),
    ]
    for arr, expected in cases:
        result = is_sorted(arr)
        ok = result == expected
        points += ok
        print(f"  is_sorted({arr!r}) = {result}  "
              f"{'OK' if ok else f'FAIL (expected {expected})'}")
    print(f"  --> {points}/{len(cases)} correct\n")


def _test_selection_sort():
    cases = [
        [],
        [5],
        [3, 1, 2],
        [9, 8, 7, 6],
        [1, 2, 3, 4],
        [4, 2, 4, 2, 1],
    ]
    points = 0
    for arr in cases:
        inp = arr[:]
        result = selectionSort(arr[:])
        ok = result == sorted(inp)
        points += ok
        print(f"  selectionSort({inp!r}) = {result!r}  "
              f"{'OK' if ok else f'FAIL (expected {sorted(inp)!r})'}")
    print(f"  --> {points}/{len(cases)} correct\n")


if __name__ == "__main__":
    print("=" * 54)
    print("  MINI CODING TEST")
    print("=" * 54)

    print("\n--- 1. is_sorted ---")
    _test_is_sorted()

    print("--- 2. selectionSort ---")
    _test_selection_sort()

    print("--- 3. benchmark_trials ---")
    print("  (run manually with a small example to verify)\n")

    print("--- 4. compare_sorting_algorithms ---")
    print("  (run manually and check that output is sorted by time)\n")
