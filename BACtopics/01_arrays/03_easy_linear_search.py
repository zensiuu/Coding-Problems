"""
ARRAYS - EASY 3: Linear Search (Sequential Search)
Hint: scan from left to right, return index or -1

Write a function linear_search(arr, x) that returns the index of x
in arr, or -1 if not found.

Examples:
  linear_search([5,3,8,1], 8) -> 2
  linear_search([5,3,8,1], 9) -> -1
"""

def linear_search(arr, x):
    if not arr :
        return -1
    target =x 
    for i in range(len(arr)):
        if arr[i] == target :
            return i 
    return -1

if __name__ == "__main__":
    assert linear_search([], 5) == -1
    assert linear_search([5,3,8,1], 3) == 1
    assert linear_search([5,3,8,1], 8) == 2
    assert linear_search([5,3,8,1], 9) == -1
    assert linear_search([1,1,1], 1) == 0   # first occurrence
    print("All tests passed!")












