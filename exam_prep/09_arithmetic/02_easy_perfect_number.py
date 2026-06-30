"""
ARITHMETIC - EASY 2: Perfect Number
Hint: sum all proper divisors (excluding n itself)

A perfect number equals the sum of its proper divisors (excluding itself).
Example: 6 = 1 + 2 + 3.

Write a function is_perfect(n) that returns True if n is perfect.

Examples:
  is_perfect(6)  -> True
  is_perfect(28) -> True
  is_perfect(10) -> False
"""

def is_perfect(n):
    pass


if __name__ == "__main__":
    assert is_perfect(6) == True
    assert is_perfect(28) == True
    assert is_perfect(10) == False
    assert is_perfect(1) == False
    print("All tests passed!")
