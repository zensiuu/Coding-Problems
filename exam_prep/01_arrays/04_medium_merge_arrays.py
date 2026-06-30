"""
ARRAYS - MEDIUM 1: Merge Two Sorted Arrays
Hint: two-pointer technique, compare heads of each array

Write a function merge_sorted(a, b) that merges two already-sorted lists
into one sorted list.

Examples:
  merge_sorted([1,3,5], [2,4,6]) -> [1,2,3,4,5,6]
  merge_sorted([], [1,2])        -> [1,2]
"""

def merge_sorted(a, b):
    if not list  :
        return -1
    

if __name__ == "__main__":
    assert merge_sorted([],[]) == []    
    assert merge_sorted([], []) == []
    assert merge_sorted([1,2,3], []) == [1,2,3]
    assert merge_sorted([], [4,5,6]) == [4,5,6]
    assert merge_sorted([1,3,5], [2,4,6]) == [1,2,3,4,5,6]
    assert merge_sorted([1,1,2], [1,3]) == [1,1,1,2,3]
    print("All tests passed!")
