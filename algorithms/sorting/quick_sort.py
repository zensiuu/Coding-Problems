def quickSort(arr):
    # call a recursive function that takes in the array 
    quickSortHelper(arr, 0 , len(arr) - 1 )
    return arr 

# if len of list passed in is > 1 , partition the array and recursivley sort
def quickSortHelper(arr, first , last ):
    if first < last:
        splitpoint = partition(arr, first, last) # find the split point 
        # recursively call the function on the two halves of the array 
        quickSortHelper(arr, first, splitpoint -1)
        quickSortHelper(arr, splitpoint + 1 , last )

# a function to partition the array using the pivot element,
def partition(arr, first, last):
    # the pivot is the first elemznt in the array 
    pivotvalue = arr[first]
    # the first pointer is the last element in the remaining unsorted part
    leftmark = first + 1 
    # the wright pointer is the last element remaining
    rightmark = last
    done = False

    while not done :
        # move the first pointer right until the first element > pivot is found 
        while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
            leftmark = leftmark + 1 
            # move the second pivot to the left until the first element < pivot 
        while rightmark >= leftmark and arr[rightmark] >= pivotvalue:
            rightmark = rightmark -1
        if rightmark < leftmark:
            done = True
        else:
            arr[leftmark], arr[rightmark] = arr[rightmark], arr[leftmark]

    arr[first], arr[rightmark] = arr[rightmark], arr[first]
    return rightmark

if __name__ == "__main__":
    test_cases = [
        ([3, 6, 8, 10, 1, 2, 1], [1, 1, 2, 3, 6, 8, 10]),
        ([2, 1], [1, 2]),
        ([1, 2], [1, 2]),
        ([1], [1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([], []),
    ]
    for arr, expected in test_cases:
        result = quickSort(arr[:])
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {arr} -> {result} (expected {expected})")





