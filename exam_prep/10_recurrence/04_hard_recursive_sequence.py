"""
RECURRENCE - HARD: Recursive Sequence Generator
Hint: given U0 and formula Un = f(Un-1), generate terms

Write a function generate_sequence(u0, formula_fn, n) that generates
the first n terms of a recursively-defined sequence.
formula_fn(prev) returns the next term.

Also write find_term(u0, formula_fn, target) that returns the first n
where Un >= target (or the smallest n where Un == target).

Examples:
  def double_minus_one(prev): return 2*prev - 1
  generate_sequence(3, double_minus_one, 5) -> [3, 5, 9, 17, 33]
  find_term(3, double_minus_one, 10) -> 3  (U2=9, U3=17)
"""

def generate_sequence(u0, formula_fn, n):
    pass

def find_term(u0, formula_fn, target):
    pass


if __name__ == "__main__":
    def double_minus_one(prev): return 2*prev - 1
    assert generate_sequence(3, double_minus_one, 1) == [3]
    assert generate_sequence(3, double_minus_one, 5) == [3, 5, 9, 17, 33]
    assert generate_sequence(1, lambda x: x+2, 4) == [1, 3, 5, 7]
    assert find_term(3, double_minus_one, 10) == 3
    print("All tests passed!")
