"""
selection_sort that:
- Takes one list as input
- Finds the smallest element in the unsorted part
- Swaps it to the correct position
- Repeats until the list is sorted
"""

"""
for each position i from 0 to n-2:
    assume smallest is at i
    for each position j from i+1 to n-1:
        IF j is smaller than smallest:
            UPDATE smallest to j
    SWAP value at i with value at smallest
"""

"""
1 what state do i need to track?
(counters, pointers, accumulators)
IN THIS CASE: i need to track the length of the array and the smallest element in it

2 what are my LOOPS doing:
the outer loop goes from position 0 to n-2, each time filling the next sorted spot
the inner loop scans from i+1 to n-1 looking for anything smaller than min_idx

3 the loop stops when:
the outer loop has filled every position up to n-2, meaning the list is fully sorted

4 the actions are the following:
- set min_idx = i (assume current is smallest)
- scan j from i+1 to end, update min_idx if a smaller value is found
- swap whatever is at i with whatever is at min_idx

5 the final state:
the list is sorted correctly and returned
"""

# =============================================================
#  SIMPLIFIED VERSION  — fill in the blanks
# =============================================================

def selection_sort(array):
    n = len(array)

    for i in range(n - 1):
        min_idx = i

        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j

        array[i], array[min_idx] = array[min_idx], array[i]

    return array


# =============================================================
#  TESTS — fill in the blanks
# =============================================================

if __name__ == "__main__":
    test_cases = [
        ([5, 2, 8, 1], [1, 2, 5, 8]),
        ([3, 1, 4, 1, 5], [1, 1, 3, 4, 5]),
        ([1], [1]),
        ([], []),
        ([2, 1], [1, 2]),
        ([1, 2, 3], [1, 2, 3]),
    ]

    for arr, expected in test_cases:
        result = selection_sort(arr[:])
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: {arr} -> {result} (expected {expected})")
