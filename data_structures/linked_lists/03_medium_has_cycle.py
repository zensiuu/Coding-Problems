"""
LINKED LISTS - MEDIUM 1: Detect Cycle
Hint: Floyd's algorithm — slow pointer moves 1 step, fast moves 2 steps

Write a function has_cycle(head) that returns True if the linked list has
a cycle, False otherwise.

Examples:
  1->2->3->4->5 (no cycle)           -> False
  1->2->3->4->5->2 (5 points back)   -> True
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from linked_list_base import ListNode, build_list

if __name__ == "__main__":
    head = build_list([1, 2, 3, 4])
    print(f"no cycle = {has_cycle(head)}  expected = False")

    head = build_list([1, 2, 3, 4, 5])
    head.next.next.next.next.next = head.next
    print(f"has cycle = {has_cycle(head)}  expected = True")

    single = ListNode(1)
    print(f"single no cycle = {has_cycle(single)}  expected = False")

    single.next = single
    print(f"single with cycle = {has_cycle(single)}  expected = True")

    print(f"empty = {has_cycle(None)}  expected = False")
