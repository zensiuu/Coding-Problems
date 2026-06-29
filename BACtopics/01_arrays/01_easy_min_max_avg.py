"""
ARRAYS - EASY 1: Min, Max, Average
Hint: single pass, track three values

Write functions min_arr(arr), max_arr(arr), avg_arr(arr) that return
the minimum, maximum, and average of a list of integers.
If empty, return None.

Examples:
  min_arr([3,1,4,1,5]) -> 1
  max_arr([3,1,4,1,5]) -> 5
  avg_arr([1,2,3,4])   -> 2.5
"""
# min
def minarr(arr):
    if not arr:
        return None 
    min_arr=arr[0]
    for i in range(1 , len(arr)):
        if arr[i]< min_arr :
            min_arr= arr[i]
    return min_arr
arr=[1,5,8,3,2,0,10]
result = minarr(arr)
print(f"the minimum value in the array is : " , result )

# max 
def max_arr(arr):
    if not arr:
        return None
    max_val=arr[0]
    for i in range(1, len(arr)):
        if arr[i] > max_val :
            max_val=arr[i]
    return max_val
arr=[656,64,9,64,3131,64,1,71,31,9,0,65+55,69-64,-5496541]
result = max_arr(arr)
print(f"the biggest number in the list is : ", result )

# average 
