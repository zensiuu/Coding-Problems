"""
ARRAYS - HARD: Maximum Subarray Sum (Kadane's Algorithm)
Hint: carry a running sum, reset to 0 if it goes negative

Write a function max_subarray_sum(arr) that returns the maximum sum of
any contiguous subarray.

Examples:
  max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) -> 6  (subarray [4,-1,2,1])
  max_subarray_sum([1])                       -> 1
  max_subarray_sum([5,4,-1,7,8])             -> 23
"""

def max_subarray_sum(arr):
    pass


if __name__ == "__main__":
    assert max_subarray_sum([1]) == 1
    assert max_subarray_sum([-1]) == -1
    assert max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert max_subarray_sum([5,4,-1,7,8]) == 23
    assert max_subarray_sum([-1,-2,-3]) == -1
    print("All tests passed!")
