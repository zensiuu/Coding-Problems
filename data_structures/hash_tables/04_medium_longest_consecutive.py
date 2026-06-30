"""
HASH TABLES - MEDIUM 2: Longest Consecutive Sequence
Hint 1: insert all numbers into a set
Hint 2: only start counting from numbers with no left neighbor (num-1 not in set)
Hint 3: O(n) time — no sorting allowed

Write a function longest_consecutive(nums) that returns the length of the
longest consecutive elements sequence.

Examples:
  longest_consecutive([100,4,200,1,3,2]) -> 4  (sequence 1,2,3,4)
  longest_consecutive([0,3,7,2,5,8,4,6,0,1]) -> 9
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([], 0),
        ([1], 1),
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
        ([1, 2, 0, 1], 3),
    ]
    for nums, expected in tests:
        result = longest_consecutive(nums)
        ok = result == expected
        print(f"longest_consecutive({nums!r}) = {result}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
