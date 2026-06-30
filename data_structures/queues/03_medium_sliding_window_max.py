"""
QUEUES - MEDIUM: Sliding Window Maximum
Hint: use a deque that stores indices; keep the deque sorted descending by value

Given an array and a window size k, return an array of the maximum value in
each sliding window as it moves from left to right.

Examples:
  max_sliding_window([1,3,-1,-3,5,3,6,7], 3) -> [3,3,5,5,6,7]
  max_sliding_window([1,2,3,4,5], 3)          -> [3,4,5]
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from collections import deque

if __name__ == "__main__":
    tests = [
        ([1, 3, -1, -3, 5, 3, 6, 7], 3, [3, 3, 5, 5, 6, 7]),
        ([1], 1, [1]),
        ([1, -1], 1, [1, -1]),
        ([9, 11], 2, [11]),
        ([4, -2], 2, [4]),
        ([1, 2, 3, 4, 5], 3, [3, 4, 5]),
    ]
    for nums, k, expected in tests:
        result = max_sliding_window(nums, k)
        ok = result == expected
        print(f"max_sliding_window({nums!r}, {k}) = {result!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
