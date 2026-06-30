"""
HASH TABLES - EASY 1: Frequency Count
Hint: use a dict: for each element, dict[element] = dict.get(element, 0) + 1

Write a function freq_count(arr) that returns a dict with each element as
key and its count as value.

Examples:
  freq_count([1,2,2,3,3,3]) -> {1:1, 2:2, 3:3}
  freq_count(["a","b","a"]) -> {"a":2, "b":1}
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
if __name__ == "__main__":
    tests = [
        ([], {}),
        ([1], {1: 1}),
        ([1, 2, 2, 3, 3, 3], {1: 1, 2: 2, 3: 3}),
        (["a", "b", "a"], {"a": 2, "b": 1}),
        ([1, 1, 1, 1], {1: 4}),
    ]
    for arr, expected in tests:
        result = freq_count(arr)
        ok = result == expected
        print(f"freq_count({arr!r}) = {result!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
