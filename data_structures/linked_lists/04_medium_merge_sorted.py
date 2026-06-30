"""
LINKED LISTS - MEDIUM 2: Merge Two Sorted Lists
Hint: use a dummy head node, then compare and link

Write a function merge_sorted(l1, l2) that merges two sorted linked lists
into one sorted linked list. Return the head of the merged list.

Examples:
  merge_sorted(1->3->5, 2->4->6)  ->  1->2->3->4->5->6
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from linked_list_base import build_list, list_to_array

if __name__ == "__main__":
    tests = [
        ([], [], []),
        ([1], [], [1]),
        ([], [2], [2]),
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3], [1, 2, 3], [1, 1, 2, 2, 3, 3]),
        ([5], [1, 2, 3], [1, 2, 3, 5]),
    ]
    for v1, v2, expected in tests:
        h1 = build_list(v1)
        h2 = build_list(v2)
        result = merge_sorted(h1, h2)
        arr = list_to_array(result)
        ok = arr == expected
        print(f"merge_sorted({v1!r}, {v2!r}) = {arr!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
