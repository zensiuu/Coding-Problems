"""
================================================================================
  ASSIGNMENT: Sorting Algorithms & Benchmarking
================================================================================

  Read each question carefully. Write your answers / code in the spaces
  provided below each question. Some questions ask you to write code —
  implement those directly in this file and run it to verify.

================================================================================
  PART 1 — CONCEPTUAL (answer in comments)
================================================================================

# Q1. In benchmarking.py, why does the `mean_sorts` function call `.unstack()`
#      at the end? What would the output look like without it?
#
# Answer: .unstack() pivots the table so each algorithm becomes a row and each
# size becomes a column — much easier to read. Without it, the output has a
# multi-level (Sort, Size) index as rows, so sizes repeat for every algorithm.


# Q2. The CountingSort algorithm has a limitation compared to the other four
#      sorts. What is it? (Hint: look at the input values and the algorithm
#      itself.)
#
# Answer: CountingSort only works on non-negative integers (or integer keys
# cannot handle negative numbers, floats, or arbitrary data. The other sorts
# are comparison-based and work on any comparable data.


# Q3. Look at the benchmarking results we got:
#
#      Size            100    250     500     750     1000    1250     2500
#      Bubblesort     0.535  3.557  17.373  33.948  56.399  98.522  484.442
#      CountingSort   0.034  0.070   0.104   0.153   0.184   0.313    0.745
#      insertionSort  0.395  2.432  12.031  17.306  33.932  61.813  199.169
#      mergeSort      0.208  0.555   1.167   2.065   3.147   4.209    7.576
#      quickSort      0.085  0.346   0.572   1.171   1.627   2.123    5.240
#
#      Which algorithm grows the fastest as input size increases?
#      Which grows the slowest?
#      Roughly how many times faster is quickSort than bubbleSort at n=2500?
#
# Answer: Bubblesort grows the fastest (0.535 → 484.442, ~905x increase).
# CountingSort grows the slowest (0.034 → 0.745, ~22x increase).
# At n=2500, quickSort (5.240 ms) is about 92x faster than bubbleSort (484.442 ms).
# 484.442 / 5.240 ≈ 92.5


# Q4. Why is CountingSort so much faster than every other algorithm here?
#      What is its time complexity, and what makes it different from the rest?
#
# Answer: CountingSort is O(n + k), where n = number of elements and
# k = max value range. It is NOT a comparison sort — it counts occurrences
# using array indices. The other four sorts are comparison-based (O(n log n)
# or O(n²)), which means they compare elements pairwise. CountingSort avoids
# comparisons entirely, making it drastically faster when k is small relative
# to n.


# Q5. The current benchmarking uses random integers in the range [0, 100].
#      If we changed the range to [0, 10000], which algorithm's performance
#      would be affected the MOST and why?
#
# Answer: CountingSort would be affected most. Its time complexity is O(n + k),
# where k = max value. Increasing the range from 100 to 10000 makes k 100x
# larger, directly increasing run time. The other four sorts are comparison-
# based — they only care about how many elements there are, not what their
# values are.


# Q6. What is the difference between a stable and unstable sorting algorithm?
#      Which of the five algorithms are stable?
#      (If you don't know, research it or trace through an example.)
#
# Answer: A stable sort preserves the relative order of equal elements; an
# unstable sort may swap them. Stable: BubbleSort, InsertionSort, MergeSort,
# CountingSort. Unstable: QuickSort (typical implementations, though it can
# be made stable with extra effort).


# Q7. InsertionSort and BubbleSort are both O(n²) algorithms.
#      Based on the data, which one is generally faster? Why might that be?
#
# Answer: InsertionSort is consistently faster. BubbleSort always does
# n(n-1)/2 comparisons — it can't stop early. InsertionSort stops shifting
# as soon as the key is in the right position, so it does far fewer
# comparisons on average, especially on partially-ordered data.


================================================================================
  PART 2 — CODING (implement the functions below)
================================================================================

import random
import time


# -------------------------------------------------------------------
#  Q8. Implement a function called `is_sorted(arr)` that returns True
#      if the array is sorted in non-decreasing order, False otherwise.
#      Do NOT use Python's built-in sorting or any library.
#
#  Example:
#      is_sorted([1, 2, 3, 4])   → True
#      is_sorted([1, 3, 2, 4])   → False
#
#  Hint: A single-element or empty array is always sorted.
# -------------------------------------------------------------------

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# -------------------------------------------------------------------
#  Q9. The current benchmarking only uses 5 trials per size, which
#      can be noisy. Write a function `benchmark_trials(algorithms, sizes, runs)`
#      that is identical to `benchmarking()` but also returns the STANDARD
#      DEVIATION alongside the mean for each algorithm at each size.
#
#      Return two DataFrames: (means, stds)
#        - means: average time per (algorithm, size)  — same as before
#        - stds:  standard deviation per (algorithm, size)
#
#      Hint: df.groupby(...)['Times'].std() works just like .mean()
# -------------------------------------------------------------------

import pandas as pd

def benchmark_trials(algorithms, sizes, runs):
    elapsed_times = []
    input_size = []
    trials = []
    sort_names = []

    for sort_algo in algorithms:
        for size in sizes:
            for run in range(runs):
                x = [random.randint(0, 100) for _ in range(size)]
                algorithm = algorithms[sort_algo]
                start_time = time.time()
                algorithm(x)
                end_time = time.time()
                time_elapsed = (end_time - start_time) * 1000
                elapsed_times.append(time_elapsed)
                trials.append(run + 1)
                input_size.append(size)
                sort_names.append(sort_algo)

    df = pd.DataFrame({
        "Sort": sort_names,
        "Size": input_size,
        "Times": elapsed_times,
        "trialNo": trials
    })
    means = df.groupby(['Sort', 'Size'])['Times'].mean().round(3).unstack()
    stds = df.groupby(['Sort', 'Size'])['Times'].std().round(3).unstack()
    return means, stds


# -------------------------------------------------------------------
#  Q10. Add a NEW sorting algorithm to the benchmark: selection sort.
#       Implement it below as `selectionSort(arr)`, then add it to the
#       algorithms dictionary at the bottom of this file and run the
#       benchmark again.
#
#  Selection sort algorithm:
#    1. Find the smallest element in the unsorted portion.
#    2. Swap it with the first unsorted element.
#    3. Move the boundary right by one and repeat.
#
#  Hint: O(n²) — similar to bubble sort but with fewer swaps.
# -------------------------------------------------------------------

def selectionSort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# -------------------------------------------------------------------
#  Q11. Write a function `compare_sorting_algorithms()` that:
#        1. Generates a random array of length 2000.
#        2. Makes 5 COPIES of it (so each algorithm gets the SAME data).
#        3. Times bubbleSort, insertionSort, mergeSort, quickSort, and
#           countingSort on their respective copies.
#        4. Prints the results in order from fastest to slowest.
#
#  Why is it important to give each algorithm the SAME data?
#
#  Hint: Use arr.copy() to make independent copies.
# -------------------------------------------------------------------

def compare_sorting_algorithms():
    arr = [random.randint(0, 100) for _ in range(2000)]

    algos = [
        ("BubbleSort", bubblesort.bubbleSort),
        ("InsertionSort", insertionSort.insertionSort),
        ("MergeSort", mergeSortAlgo.merge_sort),
        ("QuickSort", quickSort.quickSort),
        ("CountingSort", countingSort.count_sort),
    ]

    results = []
    for name, algo in algos:
        copy = arr.copy()
        start = time.time()
        algo(copy)
        elapsed = (time.time() - start) * 1000
        results.append((elapsed, name))

    results.sort()
    for elapsed, name in results:
        print(f"{name}: {elapsed:.3f} ms")

    # Same data is important because input order and values directly affect
    # comparison-based sorts (e.g. already-sorted vs reversed). Identical
    # input ensures we measure algorithm speed, not luck of the draw.


        
================================================================================
  RUNNING THE BENCHMARK (modify this section to test your answers)
================================================================================

if __name__ == "__main__":
    # Import sorting modules
    import bubblesort
    import mergeSortAlgo
    import countingSort
    import insertionSort
    import quickSort

    algorithms = {
        "Bubblesort": bubblesort.bubbleSort,
        "insertionSort": insertionSort.insertionSort,
        "mergeSort": mergeSortAlgo.merge_sort,
        "quickSort": quickSort.quickSort,
        "CountingSort": countingSort.count_sort,
    }

    # ---- Test your implementations here ----

    # Example: test is_sorted
    # print(is_sorted([1, 2, 3]))       # should be True
    # print(is_sorted([3, 1, 2]))       # should be False
    # print(is_sorted([]))              # should be True
    # print(is_sorted([42]))            # should be True

    # Example: run benchmark_trials
    # means, stds = benchmark_trials(algorithms, [100, 500, 1000], 5)
    # print("Means:\n", means)
    # print("\nStds:\n", stds)

    # Example: run selection sort benchmark (after implementing it)
    # algorithms["SelectionSort"] = selectionSort
    # from benchmarking import benchmarking
    # results = benchmarking(algorithms, [100, 500, 1000], 5)
    # print(results.groupby(['Sort', 'Size']).mean().round(3).unstack())

    # Example: compare on identical data
    # compare_sorting_algorithms()
    pass
"""
