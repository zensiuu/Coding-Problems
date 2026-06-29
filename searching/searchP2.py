def findIndex(arr, x):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return mid
        elif x > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    x = 4
    print(findIndex(arr, x))



