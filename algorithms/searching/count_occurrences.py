"""
Problem 1 — Count Occurrences 
Given an array [8, 5, 8, 2, 8, 3] and target 8,
 how many times does 8 appear? Write a function that returns the count
 instead of just the first index.
"""

def count_occurrences(arr, nb):
    result = 0
    for i in range(len(arr)):
        if arr[i] == nb:
            result += 1
    return result

if __name__=="__main__":
    arr=[8, 5, 8, 2, 8, 3]
    print(count_occurrences(arr, 8))
