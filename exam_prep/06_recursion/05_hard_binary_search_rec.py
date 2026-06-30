"""
RECURSION - HARD: Binary Search (Recursive)
Hint: check mid, then recurse on left or right half

Write a recursive function binary_search_rec(arr, x, left, right)
that returns the index of x in sorted arr, or -1 if not found.

Examples:
  binary_search_rec([1,3,5,7,9], 7, 0, 4) -> 3
  binary_search_rec([1,3,5,7,9], 2, 0, 4) -> -1
"""

def binary_search_rec(arr, x, left, right):
    pass


if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9]
    assert binary_search_rec(arr, 7, 0, len(arr)-1) == 3
    assert binary_search_rec(arr, 1, 0, len(arr)-1) == 0
    assert binary_search_rec(arr, 9, 0, len(arr)-1) == 4
    assert binary_search_rec(arr, 2, 0, len(arr)-1) == -1
    assert binary_search_rec([], 5, 0, -1) == -1
    print("All tests passed!")
