"""
STACKS - HARD: Largest Rectangle in Histogram
Hint 1: for each bar, find the first smaller bar to its left and right
Hint 2: use a stack of indices to track increasing heights

Given an array of heights, find the largest rectangle that can be formed.

Examples:
  largest_rectangle([2,1,5,6,2,3])  -> 10
  largest_rectangle([1,2,3,4,5])    -> 9
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([], 0),
        ([5], 5),
        ([1, 2, 3, 4, 5], 9),
        ([2, 1, 5, 6, 2, 3], 10),
        ([2, 4], 4),
        ([1, 1, 1, 1], 4),
    ]
    for heights, expected in tests:
        result = largest_rectangle(heights)
        ok = result == expected
        print(f"largest_rectangle({heights!r}) = {result}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
