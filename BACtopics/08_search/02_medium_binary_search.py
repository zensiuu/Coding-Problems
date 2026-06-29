"""
SEARCH - MEDIUM 1: Binary Search (Iterative)
Hint: narrow left/right boundaries in a sorted array

Write a function binary_search(arr, x) that returns the index of x in
a SORTED array using binary search (iterative). Return -1 if not found.

Examples:
  binary_search([1,3,5,7,9], 7) -> 3
  binary_search([1,3,5,7,9], 2) -> -1
"""

def binary_search(arr, x):
    pass


if __name__ == "__main__":
    assert binary_search([], 1) == -1
    assert binary_search([1], 1) == 0
    assert binary_search([1,3,5,7,9], 7) == 3
    assert binary_search([1,3,5,7,9], 2) == -1
    assert binary_search([1,3,5,7,9], 1) == 0
    assert binary_search([1,3,5,7,9], 9) == 4
    print("All tests passed!")
