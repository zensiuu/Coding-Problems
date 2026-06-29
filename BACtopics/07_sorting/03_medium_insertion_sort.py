"""
SORTING - MEDIUM 1: Insertion Sort
Hint: take each element, insert it into the sorted portion

Write a function insertion_sort(arr) that sorts arr in-place using
insertion sort. Return arr.

Examples:
  insertion_sort([3,1,2]) -> [1,2,3]
"""

def insertion_sort(arr):
    pass


if __name__ == "__main__":
    assert insertion_sort([]) == []
    assert insertion_sort([1]) == [1]
    assert insertion_sort([3,1,2]) == [1,2,3]
    assert insertion_sort([5,3,6,2,1]) == [1,2,3,5,6]
    print("All tests passed!")
