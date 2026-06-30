"""
HARD TEST — Sorting Algorithms Mastery
=======================================
Time: ~90 min  |  Score: 65 points  |  Passing: 45+

Fill in every "TODO" section.  Run the file to auto-grade.
No partial credit on individual assertions.
You MAY use any built-in function EXCEPT .sort() or sorted().

  python sorting/hard_test.py
"""


# ============================================================
#  PART 1 — DUAL-PIVOT QUICKSORT  (9 pts)
# ============================================================
# Standard quicksort uses one pivot.  Dual-pivot quicksort (used
# by Java's Arrays.sort) picks TWO pivots and splits into THREE
# regions:  < p1  |  p1 <= x <= p2  |  > p2
#
# Implement dual_pivot_quick(arr) in-place.  Handle duplicates.
# Hint: after partitioning, recurse on all three regions.


def dual_pivot_quick(arr):
    # TODO
    pass


# ============================================================
#  PART 2 — STABLE SELECTION SORT  (6 pts)
# ============================================================
# Standard selection sort swaps the minimum into position.  This
# makes it UNSTABLE — equal elements can change relative order.
#
# Implement selection_sort_stable(arr) so it IS stable.
# Instead of swapping, INSERT the minimum by shifting elements
# right.  Return arr.

def selection_sort_stable(arr):
    # TODO
    pass


# ============================================================
#  PART 3 — IDENTIFY THE ALGORITHM  (6 pts)
# ============================================================

def mystery_a(arr):
    n = len(arr)
    gap = n
    shrunk = True
    while gap > 1 or shrunk:
        gap = max(1, int(gap / 1.3))
        shrunk = False
        for i in range(n - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                shrunk = True
    return arr


def mystery_b(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def mystery_c(arr):
    """This one has a subtle off-by-one.  Identify and fix."""
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


# ============================================================
#  PART 4 — COUNTING SORT FOR NEGATIVES  (7 pts)
# ============================================================
# Standard counting sort only works on non-negative integers.
# Generalize it to handle NEGATIVE integers too.
#
# Return a NEW sorted list.  O(n + k) time, O(k) space.

def counting_sort_general(arr):
    # TODO
    pass


# ============================================================
#  PART 5 — MERGE SORT WITH O(1)-SPACE MERGE  (7 pts)
# ============================================================
# Standard merge sort uses O(n) extra space during merge.
# Implement merge_sort_inplace(arr) where the merge step uses
# O(1) extra space by rotating/shifting elements in-place.

def merge_sort_inplace(arr):
    # TODO
    pass


# ============================================================
#  PART 6 — EXTERNAL SORT SIMULATION  (5 pts)
# ============================================================
# You have 10,000 numbers but only enough memory to sort 1,000
# at a time.  Simulate external merge sort:
#
#   1. Split arr into chunks of size chunk_size
#   2. Sort each chunk individually
#   3. Merge all sorted chunks using heapq.merge()
#
# Return the fully sorted list.

import heapq


def external_sort(arr, chunk_size):
    # TODO
    pass


# ============================================================
#  PART 7 — ANALYSIS  (12 pts)
# ============================================================
# Answer in the multiline string below.

analysis_answers = """

Q7.1 — Counting sort blind spot  (3 pts)
  CountingSort dominates all other algorithms at n=2500 in our
  benchmark (0.745 ms).  But there is a scenario where it is
  catastrophically worse than merge sort.  What is it?

  Answer:


Q7.2 — Benchmarking bias  (4 pts)
  Our benchmark generates random data.  If we instead fed
  insertionSort an ALREADY SORTED array, how would its time
  change?  What about quickSort with a sorted array?  Explain.

  Answer:


Q7.3 — Stability in practice  (5 pts)
  You have a list of (student_name, grade) tuples.  You want
  them sorted by grade (ascending), and students with the same
  grade must keep their original relative order.  Which of the
  five algorithms from our benchmark can you use?  Which can
  you NOT use?  Name them and say why.

  Answer:

"""


# ============================================================
#  PART 8 — TIMSORT-STYLE GALLOPING MERGE  (7 pts)
# ============================================================
# Timsort (Python's sort) uses "galloping": if one side wins 7
# times in a row during merge, it switches to binary-search-and-
# copy-block mode instead of comparing one element at a time.
#
# Implement merge_with_gallop(left, right) that returns a merged
# list and uses galloping for runs of 7+ consecutive wins.

def merge_with_gallop(left, right):
    # TODO
    pass


# ============================================================
#  TESTS  —  do NOT modify below this line
# ============================================================

def _check(name, score, total):
    print(f"  [{score}/{total}] {name}")


if __name__ == "__main__":
    print("=" * 60)
    print("  HARD TEST — Sorting Algorithms Mastery")
    print("=" * 60)
    total = 0

    # --- Part 1 ---
    print("\n--- Part 1: Dual-Pivot Quicksort (9 pts) ---")
    s = 0
    cases = [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([5, 5, 5, 5], [5, 5, 5, 5]),
        ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),
        ([1, 3, 2, 3, 1, 2], [1, 1, 2, 2, 3, 3]),
        ([4, 7, 1, 9, 3, 6, 2, 8, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (list(range(50, 0, -1)), list(range(1, 51))),
        ([1] * 100, [1] * 100),
    ]
    for arr, exp in cases:
        inp = arr[:]
        try:
            dual_pivot_quick(arr)
            if arr == exp:
                s += 1
            else:
                print(f"  FAIL: {inp[:6]}{'...' if len(inp) > 6 else ''}")
        except Exception as e:
            print(f"  ERROR: {e}")
    _check("Dual-pivot quicksort", s, 9)
    total += s

    # --- Part 2 ---
    print("\n--- Part 2: Stable Selection Sort (6 pts) ---")
    s = 0
    cases = [
        ([], []),
        ([5], [5]),
        ([4, 3, 2, 1], [1, 2, 3, 4]),
        ([1, 1, 1], [1, 1, 1]),
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
    ]
    for arr, exp in cases:
        inp = arr[:]
        try:
            selection_sort_stable(arr)
            if arr == exp:
                s += 1
            else:
                print(f"  FAIL: {inp!r}")
        except Exception as e:
            print(f"  ERROR: {e}")
    data = [(3, 'a'), (2, 'b'), (1, 'c'), (2, 'd'), (3, 'e')]
    expected = [(1, 'c'), (2, 'b'), (2, 'd'), (3, 'a'), (3, 'e')]
    try:
        selection_sort_stable(data)
        if data == expected:
            s += 1
        else:
            print(f"  FAIL stability: {data}")
    except Exception as e:
        print(f"  ERROR: {e}")
    _check("Stable selection sort", s, 6)
    total += s

    # --- Part 3 ---
    print("\n--- Part 3: Identify the Algorithm (6 pts) ---")
    s = 6
    for name, fn in [("a", mystery_a), ("b", mystery_b), ("c", mystery_c)]:
        for arr, exp in [([], []), ([3, 1, 2], [1, 2, 3]),
                         ([5, 5, 5], [5, 5, 5])]:
            inp = arr[:]
            try:
                fn(arr)
                if arr != exp:
                    print(f"  FAIL {name}: {inp!r} -> {arr!r}")
                    s -= 1
                    break
            except Exception as e:
                print(f"  ERROR {name}: {e}")
                s -= 1
                break
    print(f"  Write your answers: what are a, b, c?")
    _check("Identification + fix", s, 6)
    total += s

    # --- Part 4 ---
    print("\n--- Part 4: Counting Sort for Negatives (7 pts) ---")
    s = 0
    cases = [
        ([], []),
        ([5], [5]),
        ([-3, -1, -2, 0, 2, 1], [-3, -2, -1, 0, 1, 2]),
        ([0, 0, 0], [0, 0, 0]),
        ([-5, -4, -3, -2, -1], [-5, -4, -3, -2, -1]),
        ([4, -2, 0, -3, 1, -1, 3, -4, 2], [-4, -3, -2, -1, 0, 1, 2, 3, 4]),
        ([-100, 100, 0, -50, 50], [-100, -50, 0, 50, 100]),
    ]
    for arr, exp in cases:
        inp = arr[:]
        try:
            result = counting_sort_general(arr)
            if result == exp:
                s += 1
            else:
                print(f"  FAIL: {inp!r} -> {result!r}")
        except Exception as e:
            print(f"  ERROR: {e}")
    _check("Counting sort (negatives)", s, 7)
    total += s

    # --- Part 5 ---
    print("\n--- Part 5: Merge Sort O(1) Space (7 pts) ---")
    s = 0
    cases = [
        ([], []),
        ([1], [1]),
        ([3, 1, 2], [1, 2, 3]),
        ([9, 8, 7, 6, 5], [5, 6, 7, 8, 9]),
        ([1, 3, 2, 3, 1, 2], [1, 1, 2, 2, 3, 3]),
        ([4, 7, 1, 9, 3, 6, 2, 8, 5], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (list(range(100, 0, -1)), list(range(1, 101))),
    ]
    for arr, exp in cases:
        inp = arr[:]
        try:
            merge_sort_inplace(arr)
            if arr == exp:
                s += 1
            else:
                print(f"  FAIL: {inp[:6]}{'...' if len(inp) > 6 else ''}")
        except Exception as e:
            print(f"  ERROR: {e}")
    _check("Merge sort (O(1) merge)", s, 7)
    total += s

    # --- Part 6 ---
    print("\n--- Part 6: External Sort (5 pts) ---")
    s = 0
    cases = [
        ([], 2, []),
        ([5], 2, [5]),
        ([3, 1, 4, 1, 5, 9, 2, 6], 2, [1, 1, 2, 3, 4, 5, 6, 9]),
        ([3, 1, 4, 1, 5, 9, 2, 6], 4, [1, 1, 2, 3, 4, 5, 6, 9]),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 3,
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
    ]
    for arr, k, exp in cases:
        inp = arr[:]
        try:
            result = external_sort(arr, k)
            if result == exp:
                s += 1
            else:
                print(f"  FAIL: {inp!r}, k={k} -> {result!r}")
        except Exception as e:
            print(f"  ERROR: {e}")
    _check("External sort", s, 5)
    total += s

    # --- Part 7 ---
    print("\n--- Part 7: Analysis (12 pts) ---")
    print(analysis_answers)
    print("  (written answers — grade manually)")
    total += 12

    # --- Part 8 ---
    print("\n--- Part 8: Galloping Merge (7 pts) ---")
    s = 0
    cases = [
        ([], [], []),
        ([1], [2], [1, 2]),
        ([1, 3, 5, 7, 9], [2, 4, 6, 8, 10],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([1, 2, 3, 4, 5], [6, 7, 8, 9, 10],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([10, 20, 30], [1, 2, 3, 4, 5, 6],
         [1, 2, 3, 4, 5, 6, 10, 20, 30]),
        ([1, 4, 7, 10], [2, 3, 5, 6, 8, 9],
         [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        (list(range(0, 100, 2)), list(range(1, 100, 2)),
         list(range(100))),
    ]
    for l, r, exp in cases:
        try:
            result = merge_with_gallop(l, r)
            if result == exp:
                s += 1
            else:
                print(f"  FAIL: {l!r} ++ {r!r}")
        except Exception as e:
            print(f"  ERROR: {e}")
    _check("Galloping merge", s, 7)
    total += s

    print()
    print("=" * 60)
    print(f"  TOTAL SCORE:  {total}/65")
    print("=" * 60)
    if total >= 45:
        print("  PASS")
    else:
        print("  NEEDS WORK")
    print()
