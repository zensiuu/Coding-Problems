"""
HASH TABLES - EASY 2: Find Duplicates
Hint: use a set to track seen elements; if already seen, it's a duplicate

Write a function find_duplicates(arr) that returns elements appearing more
than once (any order). If none, return empty list.

Examples:
  find_duplicates([1,2,2,3,3,3]) -> [2,3]  (order doesn't matter)
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([], []),
        ([1, 2, 3], []),
        ([1, 2, 2, 3, 3, 3], [2, 3]),
        (["a", "b", "a", "c", "b"], ["a", "b"]),
        ([1, 1, 1, 1], [1]),
    ]
    for arr, expected in tests:
        result = find_duplicates(arr)
        ok = sorted(result) == sorted(expected)
        print(f"find_duplicates({arr!r}) = {result!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
