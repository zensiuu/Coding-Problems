"""
RECURRENCE - EASY 2: Geometric Sequence
Hint: Vn = V0 * q^n

Write a function geometric_term(v0, q, n) that returns the nth term
of a geometric sequence: Vn = V0 * q^n.
Also write geometric_sum(v0, q, n) that returns the sum of the first
n terms.
Sum formula: S = V0 * (1 - q^n) / (1 - q)  (if q != 1)
If q == 1: S = n * V0

Examples:
  geometric_term(3, 2, 3) -> 24    (3,6,12,24)
  geometric_sum(3, 2, 4)  -> 45    (3+6+12+24)
"""

def geometric_term(v0, q, n):
    pass

def geometric_sum(v0, q, n):
    pass


if __name__ == "__main__":
    assert geometric_term(3, 2, 0) == 3
    assert geometric_term(3, 2, 3) == 24
    assert geometric_sum(3, 2, 1) == 3
    assert geometric_sum(3, 2, 4) == 45
    assert geometric_sum(5, 1, 3) == 15
    print("All tests passed!")
