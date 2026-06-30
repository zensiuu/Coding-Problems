# a recursive binary search function . it returns the location of x in given 
# array arr[low..high] is present , otherwise -1

def binarySearch(arr, low , high , x):
    # check the base case 
    if high >= low :
        mid = low +(high-low)//2
        # if the element is present at the middle itself 
        if arr[mid]==x :
            return mid 
        # if element is smaller than mid , then it can only be in left subarray 
        elif arr[mid]>x:
            return binarySearch(arr,low ,mid-1, x )
        # else the element should be in the right side 
        else :
            return binarySearch(arr,mid+1,high, x )
    
    # element is not present in the array 
    else :
        return -1

if __name__=="__main__":
    arr=[2,3,4,10,40]
    x=10
    result=binarySearch(arr,0,len(arr)-1,x)
    if result!=-1:
        print("element is present at index ", result)
    else :
        print("element does not exist in the arr.")
