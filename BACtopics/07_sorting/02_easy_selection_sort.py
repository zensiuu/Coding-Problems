"""
SORTING - EASY 2: Selection Sort
Hint: find min index, swap into position

Write a function selection_sort(arr) that sorts arr in-place using
selection sort. Return arr.

Examples:
  selection_sort([3,1,2]) -> [1,2,3]
"""

def selection_sort(arr):
    pass


if __name__ == "__main__":
    assert selection_sort([]) == []
    assert selection_sort([1]) == [1]
    assert selection_sort([3,1,2]) == [1,2,3]
    assert selection_sort([9,7,5,3,1]) == [1,3,5,7,9]
    print("All tests passed!")
