def bubbleSort(array):
    for passnum in range(len(array)-1,0,-1):
        # inner loop is shorted by 1 each time as another element is sorted 
        for i in range(passnum):
            # compare each loop element i with the element right beside it (i+1)
            if array[i] > array[i+1]:
                # swap out of order pairs so largest element is right of the smaller one 
                array[i], array[i+1] = array[i+1], array[i]

"""
__________________________________________________________________________

                             SHORT BUBBLE SORT 

___________________________________________________________________________
"""

def shortBubbleSort(alist):
    exchanges = True 
    passnum = len(alist)-1
    while passnum > 0 and exchanges : 
        exchanges = False 
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                exchanges =True 
                temp = alist[i]
                alist[i]= alist[i+1]
                alist[i+1]= temp
        passnum = passnum - 1