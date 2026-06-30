"""
STACKS - EASY 1: Min Stack
Hint: keep a second stack that tracks the minimum at each level

Design a class MinStack that supports push, pop, top, and get_min in O(1) time.
You can inherit from the provided Stack class in stack_base.py.

Example:
  s.push(3), s.push(5), s.get_min() -> 3
  s.push(2), s.push(1), s.get_min() -> 1
  s.pop(), s.get_min() -> 2
"""

# ---- YOUR CODE HERE ----



# ---- TESTS ----
from stack_base import Stack

if __name__ == "__main__":
    s = MinStack()
    s.push(3)
    s.push(5)
    print(f"min = {s.get_min()}  expected = 3")
    s.push(2)
    s.push(1)
    print(f"min = {s.get_min()}  expected = 1")
    s.pop()
    print(f"min = {s.get_min()}  expected = 2")
    print(f"top = {s.top()}  expected = 2")
    s.pop()
    print(f"min = {s.get_min()}  expected = 3")
