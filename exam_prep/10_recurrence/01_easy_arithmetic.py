"""
RECURRENCE - EASY 1: Arithmetic Sequence
Hint: Un = U0 + n * r

Write a function arithmetic_term(u0, r, n) that returns the nth term
of an arithmetic sequence: Un = U0 + n * r.
Also write arithmetic_sum(u0, r, n) that returns the sum of the first
n terms (U0 to U_{n-1}).
Sum formula: S = n * (2*U0 + (n-1)*r) / 2

Examples:
  arithmetic_term(2, 3, 4) -> 14   (2,5,8,11,14)
  arithmetic_sum(2, 3, 5)  -> 40   (2+5+8+11+14)
"""

def arithmetic_term(u0, r, n):
    pass

def arithmetic_sum(u0, r, n):
    pass


if __name__ == "__main__":
    assert arithmetic_term(2, 3, 0) == 2
    assert arithmetic_term(2, 3, 4) == 14
    assert arithmetic_sum(2, 3, 1) == 2
    assert arithmetic_sum(2, 3, 5) == 40
    print("All tests passed!")
