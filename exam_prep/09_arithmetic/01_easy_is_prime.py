"""
ARITHMETIC - EASY 1: Prime Check
Hint: check divisors from 2 to sqrt(n)

Write a function is_prime(n) that returns True if n is prime, else False.

Examples:
  is_prime(7)  -> True
  is_prime(10) -> False
"""

def is_prime(n):
    pass


if __name__ == "__main__":
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(7) == True
    assert is_prime(10) == False
    assert is_prime(97) == True
    print("All tests passed!")
