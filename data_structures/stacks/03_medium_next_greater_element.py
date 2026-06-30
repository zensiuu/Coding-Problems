"""
STACKS - MEDIUM 1: Next Greater Element
Hint: traverse right-to-left, keep a monotonic stack of candidates

Given an array, for each element find the next element to its right that is
larger. If none exists, return -1.

Examples:
  next_greater([4,5,2,25])   -> [5,25,25,-1]
  next_greater([13,7,6,12])  -> [-1,12,12,-1]
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([], []),
        ([5], [-1]),
        ([4, 5, 2, 25], [5, 25, 25, -1]),
        ([13, 7, 6, 12], [-1, 12, 12, -1]),
        ([1, 2, 3, 4, 5], [2, 3, 4, 5, -1]),
        ([5, 4, 3, 2, 1], [-1, -1, -1, -1, -1]),
    ]
    for nums, expected in tests:
        result = next_greater(nums)
        ok = result == expected
        print(f"next_greater({nums!r}) = {result!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
