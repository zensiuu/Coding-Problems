"""
LINKED LISTS - EASY 1: Traverse and Search
Hint: start at head, follow .next until None

Import ListNode from linked_list_base. Write two functions:

1. list_length(head)  — count the number of nodes
2. search_value(head, target) — return True if target exists in the list

Examples:
  build_list([10,20,30,40]) -> length = 4
  search for 30 -> True, search for 99 -> False
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from linked_list_base import build_list

if __name__ == "__main__":
    head = build_list([10, 20, 30, 40])
    print(f"list_length = {list_length(head)}  expected = 4")

    print(f"search 30 = {search_value(head, 30)}  expected = True")
    print(f"search 99 = {search_value(head, 99)}  expected = False")

    empty = build_list([])
    print(f"empty list length = {list_length(empty)}  expected = 0")
