def findMinIndex(arr):
    low=0
    high=len(arr)-1
    minIndex=-1
    while low <= high:
        # divide the range into 3 parts 
        mid1=low+(high-low)//3
        mid2=high-(high-low)//3
        # if mid1 is equal to mid2 
        if arr[mid1] == arr[mid2]:
            # move towards the center 
            low=mid1+1
            high=mid2-1
            # tentatively store mid1 as potential minimum 
            minIndex=mid1
        # if arr[mid1]< arr[mid2], the minimum lies in the left part (including  mid1)
        elif arr[mid1] < arr[mid2]:
            high=mid2-1
            # update with better condidate 
            minIndex = mid1
        # is arr[mid1] > arr[mid2], the minimum lies in the right part (including mid2)
        else :
            low = mid1 +1 
            # update with better candidate 
            minIndex = mid2
    return minIndex 

def main():
    arr=[9, 7, 1, 2, 3, 6, 10]
    idx=findMinIndex(arr)
    print(idx)
if __name__=="__main__":
    main()