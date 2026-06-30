"""
ARRAYS - EASY 1: Find Maximum Element
Hint: keep a running max variable, update it as you scan

Write a function max_element(arr) that returns the largest number in a list.
If the list is empty, return None.

Examples:
  max_element([])      -> None
  max_element([5])     -> 5
  max_element([1,3,2,5,4]) -> 5
"""

# ---- YOUR CODE HERE ----

def max_element(arr):
    # check ifarray is empty to avoid index error
    if not arr :
        return -1
    # step 1 : initilize max with the first element 
    max_val= arr[0]
    # step 2: iterate through the rest of the array 
    for i in range(1, len(arr)):
        # step 3: update curent element if it is greater
        if arr[i] > max_val:
            max_val=arr[i]
    return max_val

# example usage ;
nums= [55,499,13,3,5,10,9,8,9,6,2]
print(f"the larger element in the array is :", max_element(nums))




