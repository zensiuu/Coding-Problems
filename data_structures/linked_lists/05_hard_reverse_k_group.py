"""
LINKED LISTS - HARD: Reverse Nodes in k-Group
Hint 1: reverse k nodes at a time, link the reversed group to the next
Hint 2: first count if there are k nodes left before reversing

Given a linked list, reverse the nodes k at a time and return the new head.
If the remaining nodes are fewer than k, leave them as-is (not reversed).

Examples:
  reverse_k_group(1->2->3->4->5, 2)  ->  2->1->4->3->5
  reverse_k_group(1->2->3->4->5, 3)  ->  3->2->1->4->5
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from linked_list_base import build_list, list_to_array

if __name__ == "__main__":
    tests = [
        ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
        ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
        ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
        ([1], 2, [1]),
        ([1, 2, 3, 4], 4, [4, 3, 2, 1]),
        ([], 3, []),
    ]
    for vals, k, expected in tests:
        head = build_list(vals)
        result = reverse_k_group(head, k)
        arr = list_to_array(result)
        ok = arr == expected
        print(f"reverse_k_group({vals!r}, {k}) = {arr!r}  {'OK' if ok else f'FAIL (expected {expected!r})'}")
