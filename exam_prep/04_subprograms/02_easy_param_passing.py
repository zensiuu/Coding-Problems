"""
SUBPROGRAMS - EASY 2: Pass by Value vs Reference
Hint: lists are mutable, integers are immutable

Write a function add_one(x) that takes an integer and returns x+1.
Write a function append_one(lst) that appends 1 to the list and
returns nothing (modifies in place).

Examples:
  add_one(5) -> 6
  lst = [1,2]; append_one(lst); lst -> [1,2,1]
"""

def add_one(x):
    pass

def append_one(lst):
    pass


if __name__ == "__main__":
    assert add_one(5) == 6
    assert add_one(-1) == 0

    lst = [1, 2]
    append_one(lst)
    assert lst == [1, 2, 1]
    print("All tests passed!")
