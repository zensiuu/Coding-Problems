"""
ARRAYS - EASY 2: Reverse an Array In-Place
Hint: swap elements from both ends moving inward (two-pointer technique)

Write a function reverse_array(arr) that reverses the input list in-place.
Do NOT return a new list — modify arr directly. Return arr for convenience.

Examples:
  reverse_array([])          -> []
  reverse_array([1,2,3,4])  -> [4,3,2,1]
"""

# ---- YOUR CODE HERE ----
















"""
"Function to check whether any pair exists"
"whose sum is equal to the given target value "
def two_sum(arr,target):
    n = len(arr)

    "Iterate through each element in the array "
    for i in range(n):
        "for each element arr[i], check every other element arr[j]  that comes after it  "
        for j in range(i+1,n):
            # check if the sum of the current is equal to the target 
            if arr[i]+arr[j]==target:
                return True 
    return False 

arr =[0,-1,2,-3,1]
target=-3
# create the two sum function and print the result 
if two_sum(arr, target):
    print("true")
else:
    print("false")
"PYTHON SYMULATION FOR THE TWO POINTER TECHNIQUE O(n) time and O(1) space "
# Function to check whether any pair exists 
# whose sum is equal to the given target value 
def two_sum(arr, target):
    # sort the array 
    left, right =0 , len(arr)-1
    # Iterate while left pointer is less than right 
    while left < right :
        sum=arr[left]+arr[right]
        # check if the sum matches the target 
        if sum == target :
            return True 
        elif sum < target :
            left += 1 # move left pointer to the right 
        else:
            right-=1  # move right pointer to the left 
            # if no pair is found 
    return False 

arr=[-3,-1,0,1,2]
target = 5
# call the two_sum function and print the result 
if two_sum(arr, target):
    print("ture ")
else :
    print("false")


"""
