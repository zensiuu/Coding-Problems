"""
RECURSION - EASY 2: GCD (Euclidean Algorithm)
Hint: gcd(a,b) = a if b=0 else gcd(b, a%b)

Write a recursive function gcd(a, b) that returns the greatest common
divisor of a and b.

Examples:
  gcd(48, 18) -> 6
  gcd(7, 13)  -> 1
"""

def gcd(a, b):
    pass


if __name__ == "__main__":
    assert gcd(48, 18) == 6
    assert gcd(7, 13) == 1
    assert gcd(0, 5) == 5
    assert gcd(100, 25) == 25
    print("All tests passed!")
