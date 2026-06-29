"""
ARRAYS - EASY 2: Count Occurrences
Hint: linear scan with a counter

Write a function count_occurrences(arr, x) that returns how many times x
appears in arr.

Examples:
  count_occurrences([1,2,1,3,1], 1) -> 3
  count_occurrences([5,5,5], 2)    -> 0
"""
def count_occurences(arr,x):
    if not arr:
        return None 
    target = x()
    for i in range(1, len(arr)):
        if arr[i] == x :
            x += 1 
    return x

arr=[1,65,1,5,65,1,15,1,1]
x = 1
result = count_occurences(arr,x)
print("the target appeared ", result , "times ")
