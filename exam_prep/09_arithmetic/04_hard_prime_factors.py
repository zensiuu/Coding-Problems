"""
ARITHMETIC - HARD: Prime Factorization
Hint: repeatedly divide by 2, then by odd numbers

Write a function prime_factors(n) that returns a list of prime factors
of n (with repetition).

Examples:
  prime_factors(12) -> [2, 2, 3]
  prime_factors(100) -> [2, 2, 5, 5]
  prime_factors(7)  -> [7]
"""

def prime_factors(n):
    pass


if __name__ == "__main__":
    assert prime_factors(12) == [2, 2, 3]
    assert prime_factors(100) == [2, 2, 5, 5]
    assert prime_factors(7) == [7]
    assert prime_factors(1) == []
    print("All tests passed!")
