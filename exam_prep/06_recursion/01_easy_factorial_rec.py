"""
RECURSION - EASY 1: Factorial (Recursive)
Hint: base case n <= 1, recursive case n * factorial(n-1)

Write a recursive function factorial_rec(n) that returns n!.

Examples:
  factorial_rec(0) -> 1
  factorial_rec(5) -> 120
"""

def factorial_rec(n):
    pass


if __name__ == "__main__":
    assert factorial_rec(0) == 1
    assert factorial_rec(1) == 1
    assert factorial_rec(5) == 120
    assert factorial_rec(10) == 3628800
    print("All tests passed!")
