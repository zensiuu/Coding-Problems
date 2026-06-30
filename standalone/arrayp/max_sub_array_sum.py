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
    if not arr:
        raise ValueError("array must contain at least one number! ")
    max_sum=arr[0]
    current_sum=0
    for value in arr :
        current_sum += value
        if current_sum > max_sum :
            max_sum=current_sum
        if current_sum < 0:
            current_sum=0
    return max_sum 

def test_max_subarray_sum():
    arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
    expected=6
    result=max_subarray_sum(arr)
    assert result == expected , f"expected: {expected} , got {result}"
test_max_subarray_sum()
print("Test passed !")