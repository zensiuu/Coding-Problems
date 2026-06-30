"""
LINKED LISTS - EASY 2: Reverse a Linked List
Hint: use three pointers (prev, curr, next) or recursion

Write a function reverse_list(head) that reverses a singly linked list
and returns the new head.

Examples:
  reverse_list(1->2->3->4->5)  ->  5->4->3->2->1
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from linked_list_base import build_list, list_to_array

if __name__ == "__main__":
    tests = [
        ([], []),
        ([1], [1]),
        ([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]),
        ([1, 2], [2, 1]),
    ]
    for vals, expected in tests:
        head = build_list(vals)
        result = reverse_list(head)
        arr = list_to_array(result)
        ok = arr == expected
        print(f"reverse_list({vals!r}) = {arr!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
