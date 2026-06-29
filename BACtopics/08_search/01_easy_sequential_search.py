"""
SEARCH - EASY 1: Sequential Search
Hint: scan from left to right, return index or -1

Write a function sequential_search(arr, x) that returns the index of x
in arr, or -1 if not found.

Examples:
  sequential_search([3,5,2,8], 2) -> 2
  sequential_search([3,5,2,8], 9) -> -1
"""

def sequential_search(arr, x):
    pass


if __name__ == "__main__":
    assert sequential_search([], 1) == -1
    assert sequential_search([3,5,2,8], 2) == 2
    assert sequential_search([3,5,2,8], 9) == -1
    assert sequential_search([5], 5) == 0
    print("All tests passed!")
